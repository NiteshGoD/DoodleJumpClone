@echo off
set VENV_DIR=g_env
reg query "hkcu\software\Python"
if ERRORLEVEL 1 GOTO :NOPYTHON
GOTO :HASPYTHON
:NOPYTHON
    echo Download and Install Python from the python.org
    exit /B 0
::Check if virtualenv folder exists
:HASPYTHON
for /f "tokens=1,2 delims= " %%i in ('python --version') do (
    set PYTHON_VERSION=%%i
    set PYTHON_VERSION_NUMBER=%%j
)
echo your current python version is %PYTHON_VERSION_NUMBER%
if not exist %VENV_DIR% (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
)

::Activate the virtual Environment
call %VENV_DIR%\Scripts\activate && pip install -r requirements.txt || echo cannot start virtual environment

:: Install packages
::pip install -r requirements.txt

::Run your python program
python main.py
