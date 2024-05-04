import os
import subprocess as sp

paths = {
    'notepad': "C:\Windows\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'word': "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk",
    
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])

def open_word():
    os.startfile(paths['word'])

