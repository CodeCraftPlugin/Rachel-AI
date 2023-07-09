from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [],'build_exe': 'build'}

base = 'console'

executables = [
    Executable('main.py', base=base, 
               target_name = 'Rachel-Ai.exe',
               icon="images/icon.ico"
               )
]

setup(name='Rachel-Ai',
      version = '1.0',
      description = 'An AI assistant That can open programs use the web etc',
      options = {'build_exe': build_options},
      executables = executables)
