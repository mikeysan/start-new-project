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
    # We will do the same thing here too
    # enter a development path for Linux as input
    # example: /home/spade/development
    print("Enter your full development path\n")
    print("For example: /home/spade/development\n")
    path = os.chdir(input(r'Enter path: '))
    changeWorkingPath = os.getcwd()
    print(changeWorkingPath)

elif sys.platform.startswith('darwin'):
    print("You are on a Mac OS")
else:
    print("We could not identify your Operating system")
