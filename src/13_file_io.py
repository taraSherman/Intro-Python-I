"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
import sys
import os
with open(os.path.join(sys.path[0], 'foo.txt'), 'r') as f:
    print(f.read())

print('Is the file closed?')
print(f.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
import sys
import os
with open(os.path.join(sys.path[0], 'bar.txt'), 'w') as f:
    f.write("Nobody expects the Spanish Inquisition!\nSpam!Spam!Spam!Spam!Spam!Spam!\nI cut down trees, I skip and jump, I like to press wild flowers. I put on women's clothing and hang around in bars.")

with open(os.path.join(sys.path[0], 'bar.txt'), 'r') as f:
    print(f.read())
    
print('Is the file closed?')
print(f.closed)
