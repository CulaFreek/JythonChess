import Values
import OneDeviceChess as ODC
                
if __name__ == "__main__":

    import RequestGamemode as RG

    chosenGamemode, screenH, screenW = RG.gamemodeDialog()

    Values.chosenGamemode = chosenGamemode
    Values.screenH = screenH
    Values.screenW = screenW
    
    if chosenGamemode == 0:
        ODC.startGame()
    if chosenGamemode == 1:
        print(1)
        print(screenH, screenW)
        #  import OnlineChess as OC
    if chosenGamemode == 2:
        print(2)
        print(screenH, screenW)
        #  import botChess as BC
