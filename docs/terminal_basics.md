# Terminal & Command Line Basics for Beginners

## What is a Terminal?

A **terminal** (also called **command line**, **shell**, or **console**) is a text-based interface to interact with your computer. Instead of clicking icons, you type commands.

| Term | Meaning |
|------|---------|
| **Terminal** | The application/window where you type commands |
| **Shell** | The program that interprets your commands (e.g., Bash, Zsh, PowerShell) |
| **CLI** | Command Line Interface — any text-based interface |
| **GUI** | Graphical User Interface — the visual interface you normally use |

### How to Open a Terminal

| OS | How |
|----|-----|
| **Windows** | Search "cmd" or "PowerShell" or "Terminal" in Start Menu |
| **macOS** | Spotlight (Cmd+Space) → type "Terminal" |
| **Linux** | Ctrl+Alt+T (most distros) |

---

## Essential Commands

### Navigating the File System

| Action | Windows (CMD) | Linux / macOS (Bash) |
|--------|--------------|----------------------|
| Print current directory | `cd` | `pwd` |
| List files | `dir` | `ls` |
| List with details | `dir` | `ls -la` |
| Change directory | `cd folder_name` | `cd folder_name` |
| Go up one level | `cd ..` | `cd ..` |
| Go to home directory | `cd %USERPROFILE%` | `cd ~` |
| Clear screen | `cls` | `clear` |

### File & Folder Operations

| Action | Windows (CMD) | Linux / macOS (Bash) |
|--------|--------------|----------------------|
| Create a folder | `mkdir my_folder` | `mkdir my_folder` |
| Create a file | `type nul > file.txt` | `touch file.txt` |
| Copy a file | `copy a.txt b.txt` | `cp a.txt b.txt` |
| Move / rename | `move a.txt b.txt` | `mv a.txt b.txt` |
| Delete a file | `del file.txt` | `rm file.txt` |
| Delete a folder | `rmdir /s folder` | `rm -r folder` |
| View file contents | `type file.txt` | `cat file.txt` |

> **WARNING: Delete commands are irreversible!** Unlike dragging files to the Recycle Bin / Trash, `del`, `rm`, `rmdir`, and `rm -r` **permanently delete** files and folders with **no way to recover them**. Always double-check the file/folder name before pressing Enter. **Never** run `rm -rf /` or `del /s /q C:\` — this can destroy your entire system.

### Useful Shortcuts (in Terminal)

| Shortcut | Action |
|----------|--------|
| `Tab` | Auto-complete file/folder names |
| `Up Arrow` | Recall previous command |
| `Ctrl+C` | Cancel running command |
| `Ctrl+L` | Clear screen (Bash) |

---

## Understanding File Paths

A **path** is the address of a file or folder on your computer.

### Absolute vs Relative Paths

```
# Absolute path — starts from the root
Windows:  C:\Users\Alice\Documents\project\main.py
Linux:    /home/alice/documents/project/main.py

# Relative path — starts from your current location
./main.py          # file in current directory
../data/input.csv  # go up one level, then into data/
```

### Path Separators

| OS | Separator | Example |
|----|-----------|---------|
| Windows | `\` (backslash) | `C:\Users\Alice\file.txt` |
| Linux / macOS | `/` (forward slash) | `/home/alice/file.txt` |

> Python accepts `/` on all platforms, so you can always use forward slashes in Python code.

---

## Python from the Command Line

### Check Python Installation

```bash
python --version        # or python3 --version
pip --version           # Python package manager
```

### Run a Python Script

```bash
python my_script.py     # Run a script
python -i my_script.py  # Run and stay in interactive mode
```

### Python Interactive Mode (REPL)

```bash
python                  # Start interactive Python
>>> print("Hello!")     # Type Python code directly
>>> 2 + 3
5
>>> exit()              # Leave interactive mode
```

### Install Packages with pip

```bash
pip install numpy           # Install a package
pip install -r requirements.txt  # Install from a file
pip list                    # Show installed packages
```

---

## Conda Basics

[Conda](https://docs.conda.io/) is an environment and package manager. It keeps project dependencies isolated.

### Why Use Environments?

Different projects may need different Python versions or packages. Environments prevent conflicts.

```
Project A: Python 3.9, numpy 1.21
Project B: Python 3.11, numpy 1.26
→ Each project has its own isolated environment
```

### Common Conda Commands

```bash
conda --version                        # Check conda installation

# Environment management
conda create -n myenv python=3.9       # Create environment
conda activate myenv                   # Activate environment
conda deactivate                       # Deactivate environment
conda env list                         # List all environments
conda env remove -n myenv              # Delete environment (WARNING: irreversible!)

# Package management
conda install numpy                    # Install a package
conda list                             # List installed packages
```

---

## Git Basics

[Git](https://git-scm.com/) is a **version control system** — it tracks changes to your code over time.

### Why Git?

- **Undo mistakes**: Go back to any previous version
- **Collaboration**: Multiple people can work on the same project
- **Backup**: Your code history is saved

### Core Concepts

```
Working Directory  →  Staging Area  →  Repository
   (your files)       (git add)       (git commit)
```

### Essential Git Commands

```bash
# Setup (one-time)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Starting a project
git clone <url>          # Download a remote repository
git init                 # Initialize git in current folder

# Daily workflow
git status               # Check what changed
git add file.py          # Stage a file for commit
git commit -m "message"  # Save staged changes with a description
git push                 # Upload commits to remote (GitHub)
git pull                 # Download latest changes from remote

# Viewing history
git log --oneline        # Show commit history (short)
git diff                 # Show unstaged changes
```

### Typical Workflow

```bash
# 1. Pull latest changes
git pull

# 2. Edit your files...

# 3. Check what changed
git status

# 4. Stage and commit
git add main.py
git commit -m "Add sorting function"

# 5. Push to remote
git push
```

---

## Text Editors vs IDEs

| Tool | Type | Best For |
|------|------|----------|
| **VS Code** | Editor / Light IDE | General programming, many languages |
| **PyCharm** | Full IDE | Python-specific development |
| **Jupyter Notebook** | Interactive notebook | Data science, learning, prototyping |
| **Vim / Nano** | Terminal editors | Quick edits on servers |

### VS Code Tips

- **Open terminal**: `` Ctrl+` `` (backtick)
- **Open folder**: `File → Open Folder` (always open the project folder, not individual files)
- **Extensions**: Install "Python" extension by Microsoft
- **Run code**: Right-click → "Run Python File in Terminal"

---

## Common Beginner Mistakes

### 1. "python is not recognized"
Python is not in your system PATH. Reinstall Python and check "Add to PATH" during installation, or use `conda activate` to load your environment first.

### 2. "No such file or directory"
You are in the wrong directory. Use `pwd` (or `cd` on Windows) to check where you are, then `cd` to the correct folder.

### 3. "Permission denied"
On Linux/macOS, you may need `chmod +x script.py` or prefix with `sudo`.

> **WARNING:** `sudo` runs commands with administrator privileges. **Never** run `sudo` with a command you don't fully understand — it can modify or delete critical system files.

### 4. Mixing up terminal and Python
```bash
# This is a TERMINAL command (do NOT type in Python):
python my_script.py

# This is PYTHON code (do NOT type in terminal directly):
print("hello")
```

If you see `>>>`, you are inside Python. Type `exit()` to go back to the terminal.

### 5. Forgetting to save
Always save your file (Ctrl+S) before running it in the terminal.

---

## Quick Reference Card

```
+--------------------------------------------------+
|              SURVIVAL COMMANDS                    |
+--------------------------------------------------+
| pwd / cd           → Where am I?                 |
| ls / dir           → What's here?                |
| cd folder          → Go into folder              |
| cd ..              → Go back                     |
| python file.py     → Run Python script           |
| pip install X      → Install package X           |
| conda activate env → Activate environment        |
| git status         → What changed?               |
| git add + commit   → Save a checkpoint           |
| git push           → Upload to GitHub            |
| Ctrl+C             → Stop everything!            |
+--------------------------------------------------+
```
