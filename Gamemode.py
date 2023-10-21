from gturtle import *
    
def start():
    import RequestGamemode as RG

    choosenGamemode, x, y = RG.gamemodeDialog()
        
    if choosenGamemode == 0:
        import OneDeviceChess as ODC
        
if __name__ == "__main__":
    start()