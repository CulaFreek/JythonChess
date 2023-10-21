from gturtle import *
import Values
                
if __name__ == "__main__":
    
    import RequestGamemode as RG

    choosenGamemode, screenW, screenH = RG.gamemodeDialog()

    Values.choosenGamemode = choosenGamemode
    Values.screenW = screenW
    Values.screenH = screenH
    
    if choosenGamemode == 0:
        import OneDeviceChess as ODC