# virtual environment in python programming

# Create a virtual encironment
    # python -m venv myenv
# Activate the virtual environment(Linux/MacOs)
    # source myenv\bin\activate
# Activate the virtual environment(Windows)
    # myenv\Scripts\activate.bat
# Deactivate the virtual environment
    # deactivate
# Output the list of  installed pacakages and their versions to a file
    # pip freeze > requirements.txt
# Install the pacakages listed in the requirements.txt file
    # pip install -r requirements.txt


import  pandas as p
print(p.__version__)
