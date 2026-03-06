#!/bin/bash
# ==============================================================
#  OOP 2026 - One-click Environment Setup (macOS)
#
#  This script:
#    1. Downloads and installs Miniconda
#    2. Initializes conda in shell profile
#    3. Creates conda env (OOP) and installs packages
#    4. Git clones the practice repository
#    5. Runs environment verification tests
#
#  Usage: bash setup_macos.sh
# ==============================================================

set -e

echo ""
echo "=================================================="
echo "  OOP 2026 Environment Setup (macOS)"
echo "=================================================="
echo ""

# ---- Configuration ----
INSTALL_DIR="$HOME/miniconda3"
ENV_NAME="OOP"
PYTHON_VER="3.9"
REPO_URL="https://github.com/ElionLAB/OOP_2026_Practice.git"
WORK_DIR="$HOME/OOP_2026_Practice"
CONDA_EXE="$INSTALL_DIR/bin/conda"
ENV_PYTHON="$INSTALL_DIR/envs/$ENV_NAME/bin/python"

# Detect architecture
ARCH=$(uname -m)
if [ "$ARCH" = "arm64" ]; then
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh"
else
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
fi
INSTALLER="$TMPDIR/Miniconda3-latest-MacOSX.sh"

# ---- Step 1: Install Miniconda ----
echo "[1/5] Checking Miniconda..."

if [ -f "$CONDA_EXE" ]; then
    echo "      - Already installed. Skipping."
else
    echo "      - Detected architecture: $ARCH"
    echo "      - Downloading Miniconda..."
    curl -fsSL -o "$INSTALLER" "$MINICONDA_URL"

    echo "      - Installing Miniconda..."
    bash "$INSTALLER" -b -p "$INSTALL_DIR"
    rm -f "$INSTALLER"
    echo "      - Done."
fi

# ---- Step 2: Initialize conda in shell ----
echo ""
echo "[2/5] Initializing conda..."

# Make conda available in this session
eval "$("$CONDA_EXE" shell.bash hook)"

VER=$("$CONDA_EXE" --version 2>&1)
echo "      - $VER"

# Detect shell and init
CURRENT_SHELL=$(basename "$SHELL")
if [ "$CURRENT_SHELL" = "zsh" ]; then
    PROFILE="$HOME/.zshrc"
else
    PROFILE="$HOME/.bash_profile"
fi

if grep -q "conda initialize" "$PROFILE" 2>/dev/null; then
    echo "      - conda already initialized in $PROFILE."
else
    echo "      - Running conda init ($CURRENT_SHELL)..."
    "$CONDA_EXE" init "$CURRENT_SHELL" > /dev/null 2>&1
    echo "      - Added conda to $PROFILE."
fi

# ---- Step 3: Conda env + packages ----
echo ""
echo "[3/5] Setting up conda env ($ENV_NAME)..."

if [ -f "$ENV_PYTHON" ]; then
    echo "      - Env already exists."
else
    echo "      - Creating env (Python $PYTHON_VER)..."
    "$CONDA_EXE" create -n "$ENV_NAME" python="$PYTHON_VER" -y -q
fi

# Check core packages
if "$CONDA_EXE" run -n "$ENV_NAME" python -c "import pytest, bs4, PIL" 2>/dev/null; then
    echo "      - Core packages already installed."
else
    echo "      - Installing packages (beautifulsoup4, pytest, pillow, ipykernel)..."
    "$CONDA_EXE" install -n "$ENV_NAME" beautifulsoup4 pytest pillow ipykernel -y -q
fi

# git
if "$CONDA_EXE" run -n "$ENV_NAME" git --version >/dev/null 2>&1; then
    echo "      - git already installed."
else
    echo "      - Installing git..."
    "$CONDA_EXE" install -n "$ENV_NAME" git -y -q
fi

# tox
if "$CONDA_EXE" run -n "$ENV_NAME" python -c "import tox" 2>/dev/null; then
    echo "      - tox already installed."
else
    echo "      - Installing tox..."
    "$CONDA_EXE" run -n "$ENV_NAME" pip install tox -q
fi

echo "      - Registering Jupyter kernel..."
"$CONDA_EXE" run -n "$ENV_NAME" python -m ipykernel install --user \
    --name "$ENV_NAME" --display-name "Python 3 (OOP)" > /dev/null 2>&1

# ---- Step 4: Clone repository ----
echo ""
echo "[4/5] Cloning repository..."

GIT_CMD="$INSTALL_DIR/envs/$ENV_NAME/bin/git"
if [ ! -f "$GIT_CMD" ]; then
    GIT_CMD="git"
fi

if [ -d "$WORK_DIR/.git" ]; then
    echo "      - Repository exists. Pulling latest..."
    cd "$WORK_DIR"
    "$GIT_CMD" pull origin main
    cd -  > /dev/null
elif [ -d "$WORK_DIR" ]; then
    echo "      - Folder exists but not a git repo. Check: $WORK_DIR"
else
    echo "      - Cloning..."
    "$GIT_CMD" clone "$REPO_URL" "$WORK_DIR"
fi

# ---- Step 5: Run tests ----
echo ""
echo "[5/5] Running tests..."
echo ""

cd "$WORK_DIR"
"$CONDA_EXE" run -n "$ENV_NAME" python tests/test_setup.py
TEST_RESULT=$?
cd - > /dev/null

echo ""
if [ $TEST_RESULT -eq 0 ]; then
    echo "=================================================="
    echo "  Setup completed successfully."
    echo "=================================================="
    echo ""
    echo "  Next steps:"
    echo "    1. Open folder in VSCode: $WORK_DIR"
    echo "    2. Cmd+Shift+P > Python: Select Interpreter"
    echo "       Select: Python 3.9.x ('OOP': conda)"
    echo "    3. In terminal: conda activate OOP"
    echo ""
    echo "  * Restart your terminal or run: source $PROFILE"
else
    echo "=================================================="
    echo "  Setup finished but some tests failed."
    echo "  Check the output above."
    echo "=================================================="
fi
echo ""
