import sys
import os

# Building block to add more checks to our main script.
if sys.platform.startswith('win'):
    print("You are on a Windows system")
    print("Enter your full development path\n")
    print("For example: C:\\Users\\phil4\\Documents\\development\n")
    path = os.chdir(input(r'Enter path: '))
    # the next two lines are just to check that we were successful in changing the current working directory
    #TODO: Will need to add an if statement to test that before moving on again
    changeWorkingPath = os.getcwd()
    print(changeWorkingPath)
elif sys.platform.startswith('linux'):
    print("You are on Linux")
elif sys.platform.startswith('darwin'):
    print("You are on a Mac OS")
else:
    print("We could not identify your Operating system")
