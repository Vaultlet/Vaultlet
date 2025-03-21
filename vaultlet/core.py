import os
import subprocess
import keyring

VAULTLET_VERSION = "1.0.0"

def run_with_secrets(app_name, command):
    keys = keyring.get_password(app_name, "__keys__")
    if not keys:
        print(f"[vaultlet] No keys found for app: {app_name}")
        return

    for key in keys.split(","):
        secret = keyring.get_password(app_name, key)
        if secret:
            os.environ[key] = secret
        else:
            print(f"[vaultlet] Warning: No secret found for key '{key}'.")

    result = subprocess.run(command, env=os.environ)
    exit(result.returncode)

def set_secret(app_name, key, value):
    keyring.set_password(app_name, key, value)

    existing_keys = keyring.get_password(app_name, "__keys__")
    keys = set(existing_keys.split(",")) if existing_keys else set()
    keys.add(key)
    keyring.set_password(app_name, "__keys__", ",".join(sorted(keys)))
    print(f"[vaultlet] ✅ Set secret for '{key}' under app '{app_name}'")

def list_secrets(app_name):
    keys = keyring.get_password(app_name, "__keys__")
    if not keys:
        print(f"[vaultlet] No secrets stored under app '{app_name}'.")
        return
    print(f"[vaultlet] 🔐 Secrets under '{app_name}':")
    for key in sorted(keys.split(",")):
        print(f"  - {key}")

def unset_secret(app_name, key):
    try:
        keyring.delete_password(app_name, key)
    except keyring.errors.PasswordDeleteError:
        print(f"[vaultlet] ⚠️  Key '{key}' not found.")
        return

    keys = keyring.get_password(app_name, "__keys__")
    if keys:
        key_list = set(keys.split(","))
        key_list.discard(key)
        keyring.set_password(app_name, "__keys__", ",".join(sorted(key_list)))
    print(f"[vaultlet] ❌ Removed key '{key}' from app '{app_name}'")
