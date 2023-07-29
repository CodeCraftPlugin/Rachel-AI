from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ['characterai','whisper_mic','AppOpener'], 'excludes': [],'build_exe': 'build_windows','include_files':['greetings.mp3']}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, target_name = 'ChatBot.exe',icon="images/icon.ico")
]

setup(name='ChatBot',
      version = '1.0.0',
      description = 'It is a Personality based speech to text chat bot',
      options = {'build_exe': build_options},
      executables = executables)
