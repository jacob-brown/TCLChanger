#########
# Opening tkinter apps built with pyinstaller on MacOS

# Jacob Brown
# 2019-09-06
# Pyinstaller: 3.5
# Python: 3.6.4

# to build with pyinstaller exclude --onefile as Resources/tcl is absent
    # rather than --windowed
    # Resources/tcl will be generated, allowing editing of init.tcl

# Script automatically changes the init.tcl file to a previous version (3.5) of Tcl
# allows opening of the app 

import os

# function for finding and writing over the init.tcl file
def find_change_tcl():
    # find the location
    for folderName, subfolders, filenames in os.walk('dist'):
        if '.app' in folderName: 
            for filename in filenames:
                if filename == 'init.tcl':
                    fileTCL = str(folderName + '/' + filename)

    with open(fileTCL,'r') as f:
        dfAll=f.readlines()

    with open(fileTCL,'w') as f:
        for line in dfAll:
            if 'package require -exact Tcl' in line:                              
                f.writelines("package require -exact Tcl 3.5.9\n") # rollback to 3.5.9 rather than 3.6 
            else:
                f.writelines(line)



# error for absent files and incorrect directories
try:
    find_change_tcl()
except ValueError:
    print("Directory not correct, missing, or init.tcl is absent\n Ensure --onefile is not present.")
    input()    
    import sys
    sys.exit(1)     # exit the program

