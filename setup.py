import sys
from cx_Freeze import setup, Executable

target = [Executable("game1.py",icon="game_icon.ico")]

setup(
    name="Surakshit Karo",
    version="1.0",
    author="CodeKillerX",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["res/","audio/"]}},
    executables = target)
