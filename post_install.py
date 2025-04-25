import os
import sys
import subprocess

def add_to_path():
    path_to_add = os.path.join(sys.prefix, 'Scripts')
    
    if os.name == 'nt':
        # Windows
        current_path = os.environ.get('PATH', '')
        if path_to_add.lower() not in current_path.lower():
            print(f"Please manually add {path_to_add} to your system PATH.")
            print("You can do this from: Settings -> Environment Variables -> PATH -> Edit")
    else:
        # Unix-based systems
        bashrc_path = os.path.expanduser('~/.bashrc')
        export_line = f'\nexport PATH="$PATH:{path_to_add}"\n'
        try:
            with open(bashrc_path, 'a') as bashrc:
                bashrc.write(export_line)
            print(f"Added {path_to_add} to PATH in {bashrc_path}. Please restart your terminal or run 'source ~/.bashrc'.")
        except Exception as e:
            print(f"Failed to update {bashrc_path}: {e}")

if __name__ == '__main__':
    add_to_path()
