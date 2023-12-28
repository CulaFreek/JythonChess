import Values
import RequestGamemode as RG
                
if __name__ == "__main__":

    chosenGamemode, screenH, screenW = RG.gamemodeDialog()

    Values.chosenGamemode = chosenGamemode
    Values.screenH = screenH
    Values.screenW = screenW
    
    if chosenGamemode == 0:
        import OneDeviceChess as ODC
        ODC.startGame()
    if chosenGamemode == 1:
        import OnlineChess as OC
        OC.startGame()
    if chosenGamemode == 2:
        print(2)
        print(screenH, screenW)
        #  import botChess as BC
