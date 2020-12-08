import sys
from cx_Freeze import setup, Executable

setup(
    name = "ACC Simple Setup Manager",
    version = "0.1",
    description = "ACC Simple Setup Manager",
    executables = [Executable("main.py", base = "Win32GUI",targetName="acc_simple_setup_manager.exe",icon="icon.ico")])