from gturtle import *
import gpanel as gp
import sys

if __name__ == "__main__":
    sys.exit("Starte Gamemode.py, um das Spiel zu starten")


def gamemodeDialog():
    gamemode = None
    
    screenW = gp.getScreenWidth()
    screenH = gp.getScreenHeight()
    
    fullscreen = CheckEntry("Fullscreen?", False)
    fullscreenEntryPane = EntryPane(fullscreen)
    notFullscreenWidth = IntEntry("Screenwidth :", 800)
    notFullscreenHeight = IntEntry("Screenheight :", 800)
    ScreenResolution = EntryPane("Screen resolution", notFullscreenWidth, notFullscreenHeight)

    oneDeviceRadio = RadioEntry("Play with a Friend on this Device")
    onlinePlayerRadio = RadioEntry("Play online with your Friends")
    botEnemyRadio = RadioEntry("Play against bot")
    closeButton = ButtonEntry("Play now")
    gamemodePane = EntryPane(oneDeviceRadio, onlinePlayerRadio, botEnemyRadio)
    closePane = EntryPane(closeButton)
    chooseGamemode = EntryDialog(fullscreenEntryPane, ScreenResolution, gamemodePane, closePane)
    chooseGamemode.setTitle("Choose your gamemode")
    
    while not chooseGamemode.isDisposed():
        if fullscreen.getValue():
            notFullscreenWidth.setEnabled(False)
            notFullscreenHeight.setEnabled(False)
            notFullscreenWidth.setValue(screenW)
            notFullscreenHeight.setValue(screenH)
        if not fullscreen.getValue():
            notFullscreenWidth.setEnabled(True)
            notFullscreenHeight.setEnabled(True)
        if closeButton.isTouched():
            close = True
            if oneDeviceRadio.getValue():
                gamemode = 0
            elif onlinePlayerRadio.getValue():
                gamemode = 1
            elif botEnemyRadio.getValue():
                gamemode = 2
            else:
                close = False
            if close and type(notFullscreenWidth.getValue()) is int and type(notFullscreenHeight.getValue()) is int:
                if (400 <= notFullscreenWidth.getValue() <= screenW) and (400 <= notFullscreenHeight.getValue() <= screenH):
                    chooseGamemode.dispose()
                    screenW = notFullscreenWidth.getValue()
                    screenH = notFullscreenHeight.getValue()
                else:
                    notFullscreenWidth.setValue(800)
                    notFullscreenHeight.setValue(800)
            else:
                notFullscreenWidth.setValue(800)
                notFullscreenHeight.setValue(800)
    
    return gamemode, screenW, screenH
