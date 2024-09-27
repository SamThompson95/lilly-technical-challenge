# This script sets up and runs a Python virtual environment for the project.
# 
# Steps:
# 1. Checks if the "venv" directory (virtual environment) does not exist.
# 2. If the "venv" directory does not exist:
#    a. Creates a new virtual environment in the "venv" directory.
#    b. Activates the virtual environment.
#    c. Installs the required Python packages from "requirements.txt".
#    d. Runs the "main.py" script.
# 3. If the "venv" directory already exists:
#    a. Activates the virtual environment.
#    b. Runs the "main.py" script.
#!/bin/bash

if [ ! -d "venv" ]; then
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python main.py
fi
else
    source venv/bin/activate
    python main.py
fi
