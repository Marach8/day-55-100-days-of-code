# The os Library

Today's lesson is going to use the `os` library to create folders and navigate around them.


Previously, we've used `os` to clear the screen.

Here are a few other things that it can do: 

## List a file

👉 `listdir()` will allow you to list all  the files:

```python
import os

print(os.listdir()) # Lists all the files in the current directory. Useful for checking that a file is in the folder we think it is.

files = os.listdir()
if "quickSave.txt" not in files:
  print("Error: Quick Save not found.")
#Checks if a file is in a directory and outputs an error if not.

```
## Create a folder

👉 Try this code with `os.mkdir()`:

```python
import os

os.mkdir("Hello") # Creates a folder called 'Hello'

```
## Renames a file
👉 `os.rename()` takes 2 arguments: the file to rename and the new name. 

```python
import os

os.rename("myname.txt", "NEW.o") 

```
*Hint: You would need a file called "myname.txt" already uploaded to the file tree in order to change the file name.*

The ability to create and manage files & folders is really useful, especially for backups.

### ...Which brings us to today's challenge!