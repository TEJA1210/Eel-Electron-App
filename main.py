import eel

eel.init('ui')

@eel.expose
def printJava():
    return "Welcome to Eel-Electron app!"



eel.start('home.html', mode = False)