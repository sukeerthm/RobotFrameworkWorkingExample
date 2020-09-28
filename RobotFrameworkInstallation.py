import subprocess
import sys

def install_python_library(library):
    print ('Installing Package --' + library)
    subprocess.check_call([sys.executable, '-m', 'pip','install', '--upgrade', library])
    print ('Installtion Completed --' + library)

install_python_library('robotframework==3.2.1') 
install_python_library('robotframework-ride')
install_python_library('robotframework-seleniumlibrary==3.3.1')
install_python_library('webdrivermanager')
install_python_library('robotframework-pabot')
