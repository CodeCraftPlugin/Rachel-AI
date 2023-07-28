@echo off
setlocal
set build_exe=%1
set justmakeexe = %2

if "%build_exe%"=="true" (
    call :build_exe
    call :setup-ai
    goto :eof   
)
if "%justmakeexe%"=="true" (
    call :build_exe
    goto :eof
)

echo Setting up the file...
call :setup-ai
echo Done!
call py main.py
echo Process completed.
pause
goto :eof

:build_exe
python setup.py build
goto :eof
:setup-ai
py -m venv env
call "env\Scripts\activate.bat"
call pip install -r requirements.txt  --index-url https://download.pytorch.org/whl/cu118
goto :eof