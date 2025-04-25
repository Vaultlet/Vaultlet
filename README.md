# Vaultlet – Secure environment variable injection using Windows Credential Manager
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/F1F61CA6GG)
## What?

Secrets like `AWS_SECRET_ACCESS_KEY` or `DB_PASSWORD` are commonly set via environment variables.

A common (and unsafe) approach is to store them in files like `.env`, `.bashrc`, or `.zshrc`.

**Vaultlet** offers a safer alternative: it stores secrets securely in **Windows Credential Manager**, and injects them into your environment only when explicitly requested.

Vaultlet is inspired by [`envchain`](https://github.com/sorah/envchain), but designed specifically for **Windows** users and developers.

> Don't leave secrets lying around — inject them securely only when needed.

---

## Requirements

- **Windows 10/11**
- **Python 3.7 or higher**
- Credential storage is handled using the `keyring` Python package (Vaultlet installs it for you)

---

## Installation

### From Source

1. Clone this repository:
    ```powershell
    git clone https://github.com/Vaultlet/Vaultlet.git
    cd vaultlet
    ```

2. Install in editable mode:
    ```powershell
    pip install -e .
    ```

3. Add executables to PATH (only needs to be done once):
    ```powershell
    python post_install.py
    ```

    > **Note:** You may need to open a new terminal window after running `post_install.py`.

4. You'll now have access to both:
    ```powershell
    vaultlet    # main command
    vl          # optional short alias
    ```

---

## Usage

### Store environment variables

```powershell
vaultlet --set aws-dev "AWS_ACCESS_KEY_ID" "your-access-key-id"
vl --set aws-dev "AWS_SECRET_ACCESS_KEY" "your-secret-access-key"
```

### List stored keys

```powershell
vaultlet --list aws-dev
vl --list aws-dev
```

### Remove a stored key

```powershell
vaultlet --unset aws-dev "AWS_SECRET_ACCESS_KEY"
```

### Inject secrets into a subprocess
```powershell
vaultlet aws-dev python your_script.py
vl aws-dev powershell
vl aws-dev aws sts get-caller-identity
```
Secrets are loaded from Windows Credential Manager, injected into the environment, and cleaned up after the subprocess exits.

## Checking If It Worked
### 1. List the keys

```powershell
vl --list aws-dev
```
Expected Output:

```powershell
[vaultlet] 🔐 Secrets under 'aws-dev':
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY
```
---
### 2. Check inside your app/script

Example: `print_env.py`

```python
import os

print("Access Key:", os.environ.get("AWS_ACCESS_KEY_ID"))
print("Secret Key:", os.environ.get("AWS_SECRET_ACCESS_KEY"))
```
Run it:

```powershell
vl aws-dev python print_env.py
```
---
### 3. PowerShell Environment Check

```powershell
Write-Output "AWS_ACCESS_KEY_ID: $env:AWS_ACCESS_KEY_ID"
Write-Output "AWS_SECRET_ACCESS_KEY: $env:AWS_SECRET_ACCESS_KEY"
```
Start a PowerShell session with secrets:

```powershell
vaultlet aws-dev powershell
```
---
### 4. AWS Identity Check (with AWS CLI)

```powershell
vl aws-dev aws sts get-caller-identity
```
---

## 🧩 Features

- ✅ Native support for Windows Credential Manager
- ✅ No .env files or secrets in source control
- ✅ CLI-based secret injection
- ✅ Easy secret management: --set, --list, --unset
- ✅ Supports multiple "namespaces" (e.g. aws-dev, db-prod)

## Author
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/F1F61CA6GG)

📧 stevenli6186@gmail.com

## License
MIT License