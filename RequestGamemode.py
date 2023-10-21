from gturtle import *
import gpanel as gp

def gamemodeDialog():
    gamemode = None
    
    screenW = gp.getScreenWidth()
    screenH = gp.getScreenHeight()
    
    fullscreen = CheckEntry("Fullscreen?", True)
    fullscreenEntryPane = EntryPane(fullscreen)
    notFullscreenWidth = IntEntry("Screenwidth :", x)
    notFullscreenHeight = IntEntry("Screenheight :", y)
    ScreenResolution = EntryPane("Screen resolution", notFullscreenWidth, notFullscreenHeight)

    oneDeviceRadio = RadioEntry("Play with a Friend on this Device")
    onlinePlayerRadio = RadioEntry("Play online with your Friends")
    aiEnemyRadio = RadioEntry("Play against AI")
    closeButton = ButtonEntry("Play now")
    gamemodePane = EntryPane(oneDeviceRadio, onlinePlayerRadio, aiEnemyRadio)
    closePane = EntryPane(closeButton)
    chooseGamemode = EntryDialog(fullscreenEntryPane, ScreenResolution, gamemodePane, closePane)
    chooseGamemode.setTitle("Choose your gamemode")
    
    while not chooseGamemode.isDisposed():
        if fullscreen.getValue():
            notFullscreenWidth.setEnabled(False)
            notFullscreenHeight.setEnabled(False)
            notFullscreenWidth.setValue(x)
            notFullscreenHeight.setValue(y)
        if not fullscreen.getValue():
            notFullscreenWidth.setEnabled(True)
            notFullscreenHeight.setEnabled(True)
        if closeButton.isTouched():
            close = True
            if oneDeviceRadio.getValue():
                gamemode = 0
            elif onlinePlayerRadio.getValue():
                gamemode = 1
            elif aiEnemyRadio.getValue():
                gamemode = 2
            else:
                close = False
            if close and type(notFullscreenWidth.getValue()) is int and type(notFullscreenHeight.getValue()) is int:
                if (notFullscreenWidth.getValue() >= 400 and notFullscreenWidth.getValue() <= x) and (notFullscreenHeight.getValue() >= 400 and notFullscreenHeight.getValue() <= y):
                    chooseGamemode.dispose()
                    x = notFullscreenWidth.getValue()
                    y = notFullscreenHeight.getValue()
                else:
                    notFullscreenWidth.setValue(x)
                    notFullscreenHeight.setValue(y)
    
    return gamemode, screenW, screenH
