from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import sys
import os

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        subprocess.call([sys.executable, 'post_install.py'])

setup(
    name='vaultlet',
    version='1.0.0',
    description='Securely inject env vars using Windows Credential Manager',
    author='Steven Li',
    author_email='stevenli6186@gmail.com',
    license='MIT',
    packages=find_packages(include=['vaultlet', 'vaultlet.*']),
    install_requires=[
        'keyring',
    ],
    entry_points={
        'console_scripts': [
            'vaultlet=vaultlet.__main__:main',
            'vl=vaultlet.__main__:main',
        ],
    },
    cmdclass={
        'install': PostInstallCommand,
    },
)