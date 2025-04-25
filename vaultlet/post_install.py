import os
import sys
import subprocess

def add_to_path():
    path_to_add = os.path.join(sys.prefix, 'Scripts')
    if os.name == 'nt':
        # Windows
        subprocess.call(['setx', 'PATH', f'%PATH%;{path_to_add}'])
    else:
        # Unix-based systems
        bashrc_path = os.path.expanduser('~/.bashrc')
        with open(bashrc_path, 'a') as bashrc:
            bashrc.write(f'\nexport PATH=$PATH:{path_to_add}\n')
        subprocess.call(['source', bashrc_path])

if __name__ == '__main__':
    add_to_path()
