import sys
import os

# Building block to add more checks to our main script.
if sys.platform.startswith('win'):
    print("You are on a Windows system")
elif sys.platform.startswith('linux'):
    print("You are on Linux")
elif sys.platform.startswith('darwin'):
    print("You are on a Mac OS")
else:
    print("We could not identify your Operating system")