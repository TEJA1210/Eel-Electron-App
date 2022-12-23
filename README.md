# Eel-Electron-App
It is an example demo app for the integration of eel and electron app. ;-)

Change the mode in eel.start() function call to False or None.
So that no browser will be opened when you run the main.py

Now in main.js import python-shell and execute the main.py file from javascript main.js file.

Change mainWindow.loadURL = "http://localhost:8000/home.html" 

when running the main.py file it creates this host and hosts the contents in the ui folder that is the folder that you mentioned in ee.init("ui")

This is how we can open eel app in elecctron.

I hope this is helpful. Thank you
