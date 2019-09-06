# TCLChanger
Script for changing TCL version when building tkinter apps with pyinstaller - MacOS

* Place TCLChnager.py in the same directory as the app.py 
* run `$ pyinstaller --windowed app.py` **Iportant: don't include --onefile, as the file structure will be un-editable**
* run `$ python TCLChanger.py`
* You should now be able to open the app

`dist/test.app/Contents/Resources/tcl/init.tcl` will be edited, changing `package require -exact Tcl 8.6.7` to `package require -exact Tcl 8.5-`
