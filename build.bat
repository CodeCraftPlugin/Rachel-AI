@echo off
setlocal
set "build_exe=%~1"
:build_exe
python setup.py build
:setup-ai
py -m venv env
call "env\Scripts\activate.bat"
pip install -r requirements.txt
if "%build_exe%"=="true" (
    call :build_exe
    call :setup-ai
    
)

echo Setting up the file...
call :setup-ai
echo Done!
call py main.py

echo Process completed.
pause