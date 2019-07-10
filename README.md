# Mover
Python Script to move or copy files from source to destination based on CSV file.

# Requirements
- Source folder which contines the files.
- Labels CSV file to lookup the destination
- Destination folder to create and move the files to.

# Usage
Usage: mover.py [-h] [-f LABELS] [-src SOURCE] [-dst DESTINATION]
                [-cls CLASSES] [-opr OPERATION] [-ext EXTENSTIONS]

optional arguments:
  -h, --help            show this help message and exit
  -f LABELS, --labels LABELS
                        CSV file which contains file-label pairs
  -src SOURCE, --source SOURCE
                        Source folder of the files
  -dst DESTINATION, --destination DESTINATION
                        Destination folder which will have the sub-folders.
                        Program will create sub-folders if does not exist.
  -cls CLASSES, --classes CLASSES
                        Possible classes (labels) e.g. 0,1
  -opr OPERATION, --operation OPERATION
                        Should the files copied or moved (copy/move)
  -ext EXTENSTIONS, --extenstions EXTENSTIONS
                        One or multiple extenstions e.g. jpg or jpg,png
