"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
import sys
args = len(sys.argv) - 1
position = 1
while (args >= position):
    print("Parameter %i: %s" % (position, sys.argv[position]))
    position = position + 1
print(sys.argv[0] + " is the script name.")
print("There is/are %i CLI argument(s)." %(args))

"""
passing python 03_modules.py "arg1" "arg2" returns:
Parameter 1: arg1
Parameter 2: arg2
03_modules.py is the script name.
There is/are 2 CLI argument(s).
"""
# Print out the OS platform you're using:
# YOUR CODE HERE

print(sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE

print(sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE

print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE

print(os.getlogin())