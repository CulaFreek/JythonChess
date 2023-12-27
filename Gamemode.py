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
        print(1)
        print(screenH, screenW)
        #  import OnlineChess as OC
    if chosenGamemode == 2:
        print(2)
        print(screenH, screenW)
        #  import botChess as BC
