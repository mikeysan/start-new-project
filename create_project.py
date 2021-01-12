import sys
import os

'''
    USAGE: python create_project.py [folder-name]
'''

# I am extracting the local username from the path to make it easier to change
# TODO: Change the value of local_user to match your system login name
# TODO: Change the value of github_user to match your GitHub user name
local_user = 'sspade'
github_user = 'mikeysan'

# Change current working directory of this script to match where you would like to create your 
# new project folder
# CHANGE THIS LINE TO MATCH YOUR USE CASE

# TODO: Change path to match your environment
chgDir = os.chdir(f'/home/{local_user}/Documents/development')
# An example of how to set this in Windows
# 
# chgDir = os.chdir(f'C:\\Users\\{local_user}\\Documents\\development')

# This script expects an argument that will be the folder name to create
foldername = str(sys.argv[1])
# Set the current working directory; from the scripts perspective based on what we set above
path = os.getcwd()
# Set new folder name and path
_dir = path + '/' + foldername

def createFolder():
    """
    1. Create a new project folder
    2. Initialize git on the new folder
    3. Create a README.md file
    4. Change default branch to main
    """
    try:
        os.mkdir(_dir)
        os.chdir(_dir)
        os.system('git init')
        os.system(f'echo "# {foldername}" > README.md')
        os.system('git add README.md')
        os.system('git commit -m "first commit"')
        os.system('git branch -M main')

        print(f'{foldername} created locally')
        
    except:
        print(f"create {foldername} failed")


createFolder()

# This section can be better/cleaner
# Confirm that we new folder was created and we have access to it
# then do a few things based on that information
if os.path.dirname(_dir):
    print("New Project folder created and ready")
    try:
        os.system(f'gh repo create {foldername} -y --public ')
        os.system(f'git remote add origin https://github.com/{github_user}/{foldername}')
        os.system('git push -u origin main')
    except:
        print("You may not have GitHub CLI installed\n")
        print("Install gh or push changes manually")


# Launch VS Code once everything is done.
os.system('code .')
