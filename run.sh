#!/bin/bash

# Define the path to the virtual environment
VENV_PATH="./venv"

# Check if the virtual environment exists
if [ ! -d "$VENV_PATH" ]; then
    echo "Error: Virtual environment not found at $VENV_PATH."
    echo "Please set up the virtual environment by running ./install.sh"
    exit 1
fi

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Run the Python script with any arguments passed to run.sh
python main.py "$@"

# Deactivate the virtual environment
deactivate
