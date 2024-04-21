#!/bin/bash

# Define the path to the virtual environment, change "venv" to your desired path
VENV_PATH="./venv"

# Create a virtual environment if it doesn't exist
if [ ! -d "$VENV_PATH" ]; then
    python3 -m venv "$VENV_PATH"
    echo "Created virtual environment in $VENV_PATH."
else
    echo "Virtual environment already exists in $VENV_PATH."
fi

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Upgrade pip to the latest version
pip install --upgrade pip

# Install required packages from the requirements.txt file
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate
