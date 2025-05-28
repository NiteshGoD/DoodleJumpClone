#!/usr/bin/bash
#check for python interpreter
#check for virtual_env 
#if not make virtual_env

if command -v python3 &> /dev/null; then
    echo "python 3 is installed"
else
    echo "python 3 is not installed"
    echo "Download and install python from python.org"
    exit 1 #exiting with error because no python script
fi

VENV_DIR="g_env"
CURRENT_WORKING_DIRECTORY=$(pwd)
#create virtualenv if it doesn't exist
if [ ! -d "$CURRENT_WORKING_DIRECTORY/$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

#Activate it, upgrade pip and install packages
source "$VENV_DIR/bin/activate" && pip install --upgrade pip && pip install -r requirements.txt

#install packages
#pip install --upgrade pip
#pip install -r requirements.txt

#Running the program
python main.py