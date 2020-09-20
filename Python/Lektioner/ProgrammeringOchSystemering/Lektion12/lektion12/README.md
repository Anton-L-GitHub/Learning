# Lesson 12 - Troubleshooting, error handling and debugging

## Setup

1. Create a virtual environment
2. Install requirements

### Virtual environment (venv)

see <https://docs.python.org/3/library/venv.html>

Linux / OSX

```sh
python -m venv .venv  # could also be python3
source .venv/Scripts/activate
```

Windows - cmd.exe

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

Windows - PowerShell

```PowerShell
# You  On Microsoft Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the user. You can do this by issuing the following PowerShell command:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

py -m venv .venv
.\.venv\Scripts\Activate.ps1

```

### Install requirements.txt

```bat
pip install -r requirements.txt
```
