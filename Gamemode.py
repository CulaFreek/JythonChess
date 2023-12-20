from gturtle import *
import Values
                
if __name__ == "__main__":
    
    import RequestGamemode as RG

    chosenGamemode, screenW, screenH = RG.gamemodeDialog()

    Values.chosenGamemode = chosenGamemode
    Values.screenW = screenW
    Values.screenH = screenH
    
    if chosenGamemode == 0:
        import OneDeviceChess as ODC
    if chosenGamemode == 1:
        import OnlineChess as OC
    if chosenGamemode == 2:
        import botChess as BC
