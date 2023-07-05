from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'console'

executables = [
    Executable('main.py', base=base, target_name = 'rachel')
]

setup(name='Rachel-AI',
      version = '1.0.0',
      description = 'An AI Assistant that can do alot of stuff',
      options = {'build_exe': build_options},
      executables = executables)
