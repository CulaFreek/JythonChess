import gturtle as gt
import os
import sys
import socket
import time
import threading
import Gamemode
import Values

if __name__ == "__main__":
    sys.exit("Starte Gamemode.py, um das Spiel zu starten")

screenW = Values.screenW
screenH = Values.screenH

mScreenW = screenW / 800
mScreenH = screenH / 800 # Teilen durch 800, da das Schachfeld in einem 800 x 800 Feld eingerichtet ist 

fileDir = os.path.dirname(__file__) # Speichern des Verzeichnisses, in dem das Programm läuft in der Variable fileDir, damit die Figurtexturen im Ordner in diesem Verzeichniss gefunden werden können 
chessFigures = "chessfigures/" # Name des Ordners indem sich die Texturen für die Schachfiguren befinden
dirLocation = os.path.join(fileDir, chessFigures) # Anfügen des Ordnernamen an das Verzeichniss

### Schachfeld ###
                #   0           1          2          3          4       5      6       7       8        9         10            11         12     13
chessField = [ # fieldKey, fieldNumber, figure, figureTexture, leftX, yAbove, rightX, yDown, centerX, centerY, fieldTexture, figureColor, collum, row
    ("8a", 1, "black_1_rock", dirLocation + "chessblack_2.png", -400 * mScreenW, 400 * mScreenH, -300 * mScreenW, 300 * mScreenH, -350 * mScreenW, 350 * mScreenH, "white", "black", 1, 1), ("8b", 2, "black_knight", dirLocation + "chessblack_3.png", -300 * mScreenW, 400 * mScreenH, -200 * mScreenW, 300 * mScreenH, -250 * mScreenW, 350 * mScreenH, "gray", "black", 1, 2), ("8c", 3, "black_bishop", dirLocation + "chessblack_4.png", -200 * mScreenW, 400 * mScreenH, -100 * mScreenW, 300 * mScreenH, -150 * mScreenW, 350 * mScreenH, "white", "black", 1, 3), ("8d", 4, "black_queen", dirLocation + "chessblack_1.png", -100 * mScreenW, 400 * mScreenH, 0 * mScreenW, 300 * mScreenH, -50 * mScreenW, 350 * mScreenH, "gray", "black", 1, 4), ("8e", 5, "black_king", dirLocation + "chessblack_0.png", 0 * mScreenW, 400 * mScreenH, 100 * mScreenW, 300 * mScreenH, 50 * mScreenW, 350 * mScreenH, "white", "black", 1, 5), ("8f", 6, "black_bishop", dirLocation + "chessblack_4.png", 100 * mScreenW, 400 * mScreenH, 200 * mScreenW, 300 * mScreenH, 150 * mScreenW, 350 * mScreenH, "gray", "black", 1, 6), ("8g", 7, "black_knight", dirLocation + "chessblack_3.png", 200 * mScreenW, 400 * mScreenH, 300 * mScreenW, 300 * mScreenH, 250 * mScreenW, 350 * mScreenH, "white", "black", 1, 7), ("8h", 8, "black_2_rock", dirLocation + "chessblack_2.png", 300 * mScreenW, 400 * mScreenH, 400 * mScreenW, 300 * mScreenH, 350 * mScreenW, 350 * mScreenH, "gray", "black", 1, 8),
    ("7a", 9, "black_pawn", dirLocation + "chessblack_5.png", -400 * mScreenW, 300 * mScreenH, -300 * mScreenW, 200 * mScreenH, -350 * mScreenW, 250 * mScreenH, "gray", "black", 2, 1), ("7b", 10, "black_pawn", dirLocation + "chessblack_5.png", -300 * mScreenW, 300 * mScreenH, -200 * mScreenW, 200 * mScreenH, -250 * mScreenW, 250 * mScreenH, "white", "black", 2, 2), ("7c", 11, "black_pawn", dirLocation + "chessblack_5.png", -200 * mScreenW, 300 * mScreenH, -100 * mScreenW, 200 * mScreenH, -150 * mScreenW, 250 * mScreenH, "gray", "black", 2, 3), ("7d", 12, "black_pawn", dirLocation + "chessblack_5.png", -100 * mScreenW, 300 * mScreenH, 0 * mScreenW, 200 * mScreenH, -50 * mScreenW, 250 * mScreenH, "white", "black", 2, 4), ("7e", 13, "black_pawn", dirLocation + "chessblack_5.png", 0 * mScreenW, 300 * mScreenH, 100 * mScreenW, 200 * mScreenH, 50 * mScreenW, 250 * mScreenH, "gray", "black", 2, 5), ("7f", 14, "black_pawn", dirLocation + "chessblack_5.png", 100 * mScreenW, 300 * mScreenH, 200 * mScreenW, 200 * mScreenH, 150 * mScreenW, 250 * mScreenH, "white", "black", 2, 6), ("7g", 15, "black_pawn", dirLocation + "chessblack_5.png", 200 * mScreenW, 300 * mScreenH, 300 * mScreenW, 200 * mScreenH, 250 * mScreenW, 250 * mScreenH, "gray", "black", 2, 7), ("7h", 16, "black_pawn", dirLocation + "chessblack_5.png", 300 * mScreenW, 300 * mScreenH, 400 * mScreenW, 200 * mScreenH, 350 * mScreenW, 250 * mScreenH, "white", "black", 2, 8),
    ("6a", 17, "", "", -400 * mScreenW, 200 * mScreenH, -300 * mScreenW, 100 * mScreenH, -350 * mScreenW, 150 * mScreenH, "white", "", 3, 1), ("6b", 18, "", "", -300 * mScreenW, 200 * mScreenH, -200 * mScreenW, 100 * mScreenH, -250 * mScreenW, 150 * mScreenH, "gray", "", 3, 2), ("6c", 19, "", "", -200 * mScreenW, 200 * mScreenH, -100 * mScreenW, 100 * mScreenH, -150 * mScreenW, 150 * mScreenH, "white", "", 3, 3), ("6d", 20, "", "", -100 * mScreenW, 200 * mScreenH, 0 * mScreenW, 100 * mScreenH, -50 * mScreenW, 150 * mScreenH, "gray", "", 3, 4), ("6e", 21, "", "", 0 * mScreenW, 200 * mScreenH, 100 * mScreenW, 100 * mScreenH, 50 * mScreenW, 150 * mScreenH, "white", "", 3, 5), ("6f", 22, "", "", 100 * mScreenW, 200 * mScreenH, 200 * mScreenW, 100 * mScreenH, 150 * mScreenW, 150 * mScreenH, "gray", "", 3, 6), ("6g", 23, "", "", 200 * mScreenW, 200 * mScreenH, 300 * mScreenW, 100 * mScreenH, 250 * mScreenW, 150 * mScreenH, "white", "", 3, 7), ("6h", 24, "", "", 300 * mScreenW, 200 * mScreenH, 400 * mScreenW, 100 * mScreenH, 350 * mScreenW, 150 * mScreenH, "gray", "", 3, 8), 
    ("5a", 25, "", "", -400 * mScreenW, 100 * mScreenH, -300 * mScreenW, 0 * mScreenH, -350 * mScreenW, 50 * mScreenH, "gray", "", 4, 1), ("5b", 26, "", "", -300 * mScreenW, 100 * mScreenH, -200 * mScreenW, 0 * mScreenH, -250 * mScreenW, 50 * mScreenH, "white", "", 4, 2), ("5c", 27, "", "", -200 * mScreenW, 100 * mScreenH, -100 * mScreenW, 0 * mScreenH, -150 * mScreenW, 50 * mScreenH, "gray", "", 4, 3), ("5d", 28, "", "", -100 * mScreenW, 100 * mScreenH, 0 * mScreenW, 0 * mScreenH, -50 * mScreenW, 50 * mScreenH, "white", "", 4, 4), ("5e", 29, "", "", 0 * mScreenW, 100 * mScreenH, 100 * mScreenW, 0 * mScreenH, 50 * mScreenW, 50 * mScreenH, "gray", "", 4, 5), ("5f", 30, "", "", 100 * mScreenW, 100 * mScreenH, 200 * mScreenW, 0 * mScreenH, 150 * mScreenW, 50 * mScreenH, "white", "", 4, 6), ("5g", 31, "", "", 200 * mScreenW, 100 * mScreenH, 300 * mScreenW, 0 * mScreenH, 250 * mScreenW, 50 * mScreenH, "gray", "", 4, 7), ("5h", 32, "", "", 300 * mScreenW, 100 * mScreenH, 400 * mScreenW, 0 * mScreenH, 350 * mScreenW, 50 * mScreenH, "white", "", 4, 8), 
    ("4a", 33, "", "", -400 * mScreenW, 0 * mScreenH, -300 * mScreenW, -100 * mScreenH, -350 * mScreenW, -50 * mScreenH, "white", "", 5, 1), ("4b", 34, "", "", -300 * mScreenW, 0 * mScreenH, -200 * mScreenW, -100 * mScreenH, -250 * mScreenW, -50 * mScreenH, "gray", "", 5, 2), ("4c", 35, "", "", -200 * mScreenW, 0 * mScreenH, -100 * mScreenW, -100 * mScreenH, -150 * mScreenW, -50 * mScreenH, "white", "", 5, 3), ("4d", 36, "", "", -100 * mScreenW, 0 * mScreenH, 0 * mScreenW, -100 * mScreenH, -50 * mScreenW, -50 * mScreenH, "gray", "", 5, 4), ("4e", 37, "", "", 0 * mScreenW, 0 * mScreenH, 100 * mScreenW, -100 * mScreenH, 50 * mScreenW, -50 * mScreenH, "white", "", 5, 5), ("4f", 38, "", "", 100 * mScreenW, 0 * mScreenH, 200 * mScreenW, -100 * mScreenH, 150 * mScreenW, -50 * mScreenH, "gray", "", 5, 6), ("4g", 39, "", "", 200 * mScreenW, 0 * mScreenH, 300 * mScreenW, -100 * mScreenH, 250 * mScreenW, -50 * mScreenH, "white", "", 5, 7), ("4h", 40, "", "", 300 * mScreenW, 0 * mScreenH, 400 * mScreenW, -100 * mScreenH, 350 * mScreenW, -50 * mScreenH, "gray", "", 5, 8),
    ("3a", 41, "", "", -400 * mScreenW, -100 * mScreenH, -300 * mScreenW, -200 * mScreenH, -350 * mScreenW, -150 * mScreenH, "gray", "", 6, 1), ("3b", 42, "", "", -300 * mScreenW, -100 * mScreenH, -200 * mScreenW, -200 * mScreenH, -250 * mScreenW, -150 * mScreenH, "white", "", 6, 2), ("3c", 43, "", "", -200 * mScreenW, -100 * mScreenH, -100 * mScreenW, -200 * mScreenH, -150 * mScreenW, -150 * mScreenH, "gray", "", 6, 3), ("3d", 44, "", "", -100 * mScreenW, -100 * mScreenH, 0 * mScreenW, -200 * mScreenH, -50 * mScreenW, -150 * mScreenH, "white", "", 6, 4), ("3e", 45, "", "", 0 * mScreenW, -100 * mScreenH, 100 * mScreenW, -200 * mScreenH, 50 * mScreenW, -150 * mScreenH, "gray", "", 6, 5), ("3f", 46, "", "", 100 * mScreenW, -100 * mScreenH, 200 * mScreenW, -200 * mScreenH, 150 * mScreenW, -150 * mScreenH, "white", "", 6, 6), ("3g", 47, "", "", 200 * mScreenW, -100 * mScreenH, 300 * mScreenW, -200 * mScreenH, 250 * mScreenW, -150 * mScreenH, "gray", "", 6, 7), ("3h", 48, "", "", 300 * mScreenW, -100 * mScreenH, 400 * mScreenW, -200 * mScreenH, 350 * mScreenW, -150 * mScreenH, "white", "", 6, 8),
    ("2a", 49, "white_pawn", dirLocation + "chesswhite_5.png", -400 * mScreenW, -200 * mScreenH, -300 * mScreenW, -300 * mScreenH, -350 * mScreenW, -250 * mScreenH, "white", "white", 7, 1), ("2b", 50, "white_pawn", dirLocation + "chesswhite_5.png", -300 * mScreenW, -200 * mScreenH, -200 * mScreenW, -300 * mScreenH, -250 * mScreenW, -250 * mScreenH, "gray", "white", 7, 2), ("2c", 51, "white_pawn", dirLocation + "chesswhite_5.png", -200 * mScreenW, -200 * mScreenH, -100 * mScreenW, -300 * mScreenH, -150 * mScreenW, -250 * mScreenH, "white", "white", 7, 3), ("2d", 52, "white_pawn", dirLocation + "chesswhite_5.png", -100 * mScreenW, -200 * mScreenH, 0 * mScreenW, -300 * mScreenH, -50 * mScreenW, -250 * mScreenH, "gray", "white", 7, 4), ("2e", 53, "white_pawn", dirLocation + "chesswhite_5.png", 0 * mScreenW, -200 * mScreenH, 100 * mScreenW, -300 * mScreenH, 50 * mScreenW, -250 * mScreenH, "white", "white", 7, 5), ("2f", 54, "white_pawn", dirLocation + "chesswhite_5.png", 100 * mScreenW, -200 * mScreenH, 200 * mScreenW, -300 * mScreenH, 150 * mScreenW, -250 * mScreenH, "gray", "white", 7, 6), ("2g", 55, "white_pawn", dirLocation + "chesswhite_5.png", 200 * mScreenW, -200 * mScreenH, 300 * mScreenW, -300 * mScreenH, 250 * mScreenW, -250 * mScreenH, "white", "white", 7, 7), ("2h", 56, "white_pawn", dirLocation + "chesswhite_5.png", 300 * mScreenW, -200 * mScreenH, 400 * mScreenW, -300 * mScreenH, 350 * mScreenW, -250 * mScreenH, "gray", "white", 7, 8),
    ("1a", 57, "white_1_rock", dirLocation + "chesswhite_2.png", -400 * mScreenW, -300 * mScreenH, -300 * mScreenW, -400 * mScreenH, -350 * mScreenW, -350 * mScreenH, "gray", "white", 8, 1), ("1b", 58, "white_knight", dirLocation + "chesswhite_3.png", -300 * mScreenW, -300 * mScreenH, -200 * mScreenW, -400 * mScreenH, -250 * mScreenW, -350 * mScreenH, "white", "white", 8, 2), ("1c", 59, "white_bishop", dirLocation + "chesswhite_4.png", -200 * mScreenW, -300 * mScreenH, -100 * mScreenW, -400 * mScreenH, -150 * mScreenW, -350 * mScreenH, "gray", "white", 8, 3), ("1d", 60, "white_queen", dirLocation + "chesswhite_1.png", -100 * mScreenW, -300 * mScreenH, 0 * mScreenW, -400 * mScreenH, -50 * mScreenW, -350 * mScreenH, "white", "white", 8, 4), ("1e", 61, "white_king", dirLocation + "chesswhite_0.png", 0 * mScreenW, -300 * mScreenH, 100 * mScreenW, -400 * mScreenH, 50 * mScreenW, -350 * mScreenH, "gray", "white", 8, 5), ("1f", 62, "white_bishop", dirLocation + "chesswhite_4.png", 100 * mScreenW, -300 * mScreenH, 200 * mScreenW, -400 * mScreenH, 150 * mScreenW, -350 * mScreenH, "white", "white", 8, 6), ("1g", 63, "white_knight", dirLocation + "chesswhite_3.png", 200 * mScreenW, -300 * mScreenH, 300 * mScreenW, -400 * mScreenH, 250 * mScreenW, -350 * mScreenH, "gray", "white", 8, 7), ("1h", 64, "white_2_rock", dirLocation + "chesswhite_2.png", 300 * mScreenW, -300 * mScreenH, 400 * mScreenW, -400 * mScreenH, 350 * mScreenW, -350 * mScreenH, "white", "white", 8, 8)
]

kingFields = [(50 * mScreenW, 350 * mScreenH, "white", "black"), (50 * mScreenW, -350 * mScreenH, "gray", "white")] # centerX, centerY, fieldColor, figureColor

selectedField = []
rochadeFigurePlace = []
lastPossibleFields = []
possibleHitFields = []
schlagenEnPassant = [0, 0, 0]
sEPHit = []
rochadeMoved = [False, False, False, False, False, False] # w_king, w_1_rock, w_2_rock, b_king, b_1_rock, b_2_rock | Falls bereits bewegt -> entsprechender Wert == True
activePlayer = "white"
activePlayerText = "Weiss"
enemy = "black"
playerEnemy = None
playerEnemyText = None
onlineConnection = False
inputAllowed = True
clientSocket = None
moves = 0

def repaint(): # Neu zeichen des Schachfeldes nach einer Bewegung --->>> Einfachste Möglichkeit Figurtexturen wieder vom Feld zu entfernen
    gt.clean("white") # Komplettes Fenster neu färben, da sonst Grafikfehler entstehen
    
    for i in range(-400, 401, 100): # Spaltenstriche, damit das colorieren der Felder korrekt funktioniert
        gt.setPos(i * mScreenW, 400 * mScreenH)
        gt.moveTo(i * mScreenW, -400 * mScreenH)
    
    for i in range(-400, 401, 100): # Zeilenstirche, damit das colorieren der Felder korrekt funktioniert
        gt.setPos(-400 * mScreenW, i * mScreenH)
        gt.moveTo(400 * mScreenW, i * mScreenH)
    
    gt.heading(0) # Ausrichten der Blickrichtung der Turtle nach oben, damit die Figuren stehen und nicht liegen oder auf dem Kopf stehen
    for largeTupel in chessField: # Für jedes Schachfeld die Mittelpunkt Koordinaten, die Feldfarbe und die sích auf dem Feld befindliche Figur entnehmen und im Folgendem aufs Spielfeld zeichnen
        centerX = largeTupel[8]
        centerY = largeTupel[9]
        fieldTexture = largeTupel[10]
        
        gt.setPos(centerX, centerY)
        gt.setFillColor(fieldTexture)# Feld in entsprechender Farbe färben
        gt.fill()
        
        figureTexture = largeTupel[3]
        if figureTexture != "":
            gt.drawImage(figureTexture) # Textur der Schachfigur aufs Spielfeld bringen
    
    elapsedTime = gt.time.time() - gameStart
    timer = elapsedTime // 60

    gt.setTitle("Du bist " + yourColor + "  -  Aktiver Spieler : " + activePlayerText + "  |    " + str(moves) + "  :  Zuege insgesamt --- Spielzeit :  " + str(int(timer)) + " min") # Nur in Minuten, da Timer nicht fortlaufend, sondern nur bei Aktionen aktualisiert wird
    gt.repaint()

def startClient(): # Funktion zum Starten des Clients / verbinden mit dem Server
    global clientSocket
    global playerEnemy
    global playerEnemyText
    global yourColor
    global onlineConnection
    
    openGames = None
    while gt.time.time() - gameStart <= 10 and not onlineConnection: # Falls innerhalb von 10 Sekunden keine Verbindung hergestellt werden kann wird das Programm mit einem SystemExit beendet 
        try: # Falls keine Verbindung mit dem Server zustande kommt -> Fehler abfangen, Programm durch Sysexit beenden mit entsprechender Nachricht
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientSocket.connect(('localhost', 8888)) # Verbinden mit dem Server, falls möglich
            openGames = clientSocket.recv(1024) # Erhalten der offenen Spielelobby-Codes, damit dem Nutzer bekannt ist, welche Spielräume offen sind
            if openGames != None:
                onlineConnection = True
                
            if gt.time.time() - gameStart <= 10 and not onlineConnection:
                sys.exit("Es konnte keine Verbindung zum Server hergestellt werden.") # Mitteilung, dass kein Verbindungsaufbau möglich ist  
            else:      
                print("Willkommen! Bitte gib einen Game-Code ein oder erstelle einen neuen.\n" + openGames)
                gameCode = str(input("Gib einen Game-Code ein: ")) # Eingabe des Lobbycodes, des Spiels, dem man beitreten möchte
                clientSocket.send(gameCode)
                
                gameCreationSuccess = clientSocket.recv(1024) # Auf Bestätigung des Servers warten
                print(gameCreationSuccess)
        
                receiveThread = threading.Thread(target = receiveMessages, args = (clientSocket,))
                receiveThread.start() # Nachrichtenempfangs-Thread starten
                
                playerEnemy = clientSocket.recv(1024) # Gegner-Farbe empfangen 
                if playerEnemy == "white":
                    yourColor = "Schwarz"
                    playerEnemyText = "Weiss"
                else:
                    yourColor = "Weiss"
                    playerEnemyText = "Schwarz"
                print("-----Du spielst " + yourColor + "-----\n-----!Weiss beginnt!-----")
                    
        except Exception as e:
            print(e)


def receiveMessages(clientSocket): # Funktion zum Empfangen von Zügen, sowie dem Spielende 
    global inputAllowed
    try:
        while True: # Muss durchgängig laufen, da zu jedem Zeitpunkt Bewegungen empfangen werden müssen
            checkMate = False
            stalemate = False
            data = clientSocket.recv(1024) # Empfangen der Nachricht
            if not data: # Falls kein Zug gemacht wurde ist der Inhalt der Nachricht 'None'. Nur nicht 'None'-Nachrichten weiter verarbeiten, sonst Fehlermeldung 
                break
            if data == "You Won": # Nachricht, die Erhalten wird, wenn der Gegner verliert
                gt.setTitle("SPIELENDE   |   " + yourColor + " hat das Spiel gewonnen") # Titel am Spielende aktualisieren
                msgDlg(yourColor + " hat das Spiel gewonnen!", title = "Schachmatt   |   " + yourColor + " gewinnt das Spiel")
                inputAllowed = False
                break
            if data == "Draw": # Nachricht, die Erhalten wird, wenn es zu einem Unentschieden kommt
                gt.setTitle("SPIELENDE   |   Unentschieden") # Titel am Spielende aktualisieren
                msgDlg("Unentschieden!", title = "Patt   |   Niemand gewinnt das Spiel")
                inputAllowed = False
                break
            stripedData = data[1:-1].split(',') # Nachrichtenformat: (x, y) !Kein Tupel Format: Unicode! Nachricht entprechend nach x und y teilen
            sField, mField = int(stripedData[0]), int(stripedData[1])
            figureMove(sField, mField) # Erhaltene Bewegung umsetzen
            decolor() # Entfärben aller Felder sowie leeren der dazu gehörigen Listen
            playerChange()
            repaint()
            if activePlayer != playerEnemy:
                check = checkCheck() # Überprüfen, ob der König des aktuellen Spielers im Schach steht
                if check: # Aufrufen der Schachmattfunktion nur, wenn ein König im Schach steht
                    checkMate = checkCheckMate()
                if not check:    
                    stalemate = checkStalemate()
                if checkMate:
                    playerChange() # Wechseln des Gegners, da für seine Figuren die möglichen Züge ermittelt werden sollen, und seine Figuren die Figuren des aktiven Spielers schlagen könnten
                    
                    inputAllowed = False # Weiteren Input nach Spielende verhindern 
                    gt.setTitle("SPIELENDE   |   " + playerEnemyText + " hat das Spiel gewonnen") # Titel am Spielende aktualisieren
                    clientSocket.send("You Won")
                    msgDlg(playerEnemyText + " hat das Spiel gewonnen!", title = "Schachmatt   |   " + playerEnemyText + " gewinnt das Spiel")
                    break
                    
                if not checkMate and check:
                    msgDlg("Du stehst im Schach \nSchuetze deinen Koenig!", title = "SCHACH") # Ausgabe 'Schach'
                    
                if stalemate:
                    inputAllowed = False # Weiteren Input nach Spielende verhindern 
                    gt.setTitle("SPIELENDE   |   Unentschieden") # Titel am Spielende aktualisieren
                    clientSocket.send("Draw")
                    msgDlg("Unentschieden!", title = "Patt   |   Niemand gewinnt das Spiel")
                    break

    except Exception as e:
        print("Fehler beim Erhalten der Nachrichten: {}".format(e))


gameStart = gt.time.time() # Zeit des Spielstarts speichern
startClient()        
                        
gt.setPlaygroundSize(int(800 * mScreenW), int(800 * mScreenH)) # Feste Fenstergröße, in die das Schachfeld perfekt hinein passt
gt.makeTurtle()
gt.hideTurtle() # Zeichengeschwindigkeit auf instant speeed setzen und Turtle verstecken
gt.setPenColor("black")
gt.setPenWidth(3)
gt.enableRepaint(False)
    
repaint() # Erstes Zeichnen des Spielfeldes
 
# Programmende! Ab hier reagiert das Programm nur noch auf MausCallBacks           
            
def possiblePawnMoves(): # Funktion die alle möglichen Bewegungen für den ausgewählten Bauern zurückgibt
    global sEPHit
    
    repaintX, repaintY, repaintTexture, rFigure, rFieldNumber, rCollum, rRow = selectedField[0] # Entpacken des ausgewählten Feldes
    possibleMoves = []
    possibleHitFields = []
    
    indexes = [-16, -9, -8, -7, 7, 8, 9, 16] # Alle Indexe, um die sich ein Bauer bewegen kann | Negativ: Weiß Positiv: Schwarz
    for index in indexes: # Durchlaufen aller Indexe
        sEPColor = False # Falls True wird das Feld hinter dem schlagbaren Bauern rot gefärbt
        if (rFigure.startswith("black") and index > 0) or (rFigure.startswith("white") and index < 0): # Überspringen der Indexe, um die sich ein schwarzer bzw. weißer Bauer nicht bewegen kann
            if rFieldNumber + index - 1 < 64 and rFieldNumber + index - 1 > -1: # Überprüfen des Indexes, sodass keine Index außerhalb der Listenlänge abgefragt wird und es einen Fehler gibt
                field = chessField[rFieldNumber + index - 1]
                if (rRow == 1 and field[13] == 8) or (rRow == 8 and field[13] == 1): # Abfrage, ob der Bauer am Spielfeldrand heraus laufen würde
                    continue
                if field[11] == "" or field[11] == enemy: # Falls das zu überprüfende Feld leer ist oder ein Gegner auf diesem steht
                    if not (schlagenEnPassant[0] == moves and field[1] == schlagenEnPassant[1]): # Implimentierung der Regel 'Schlagen en passant' hier falsch falls diese eine Anwendung finden würde
                        if (abs(index) == 7 or abs(index) == 9) and field[11] != enemy:
                            continue
                    elif abs(index) == 7 or abs(index) == 9:
                        sEPField = chessField[schlagenEnPassant[2] - 1] # Feld auf dem der 'Schlagen en passant' Bauer steht einlesen
                        sEPColor = True
                        sEPHit = [(sEPField[8], sEPField[9], sEPField[10], sEPField[1], field[8], field[9], field[10])] # Speichern der Felder, damit diese korrekt gefärbt und falls der Bauer den anderen en passant schlägt dieser entfernt wird
                    if abs(index) == 8 and field[11] != "": # Bauern können nur nach vorne laufen, wenn das Feld vor ihnen Frei ist
                        continue
                    if abs(index) == 16 and not ((rCollum == 2 and rFigure == "black_pawn") or (rCollum == 7 and rFigure == "white_pawn")): # Falls der abzufragende Index 16 ist und es sich nicht um einen Bauern handelt, der noch auf seinem Startfeld steht wird mit dem nächsten Schleifendurchlauf fortgefahren
                        continue
                    if abs(index) == 16: # Prüft ob beide Felder (das über welches der Bauer läuft und das auf welchem er landet) frei sind
                        rField = chessField[rFieldNumber + (index // 2) - 1]
                        if rField[11] != "" or field[11] != "":
                            continue
    
                    possibleMoves.append((field[8], field[9], field[10], field[1]))
                    
                    if field[11] == enemy or sEPColor:
                        possibleHitFields.append((field[8], field[9], field[10], field[1])) # Liste mit Feldern die Rot gefärbt werden sollen -> Eine Figur steht auf diesen

    return possibleMoves, possibleHitFields # Zurückgeben aller ermittelten möglichen Bewegungen


def possibleKnightMoves(): # Funktion, die alle möglichen Bewegungen für ein ausgewähltes Pferd zurück gibt
    
    repaintX, repaintY, repaintTexture, rFigure, rFieldNumber, rCollum, rRow = selectedField[0] # Entpacken des ausgewählten Feldes
    possibleMoves = []
    possibleHitFields = []
    
    indexes = [-17, -15, -10, -6, 6, 10, 15, 17] # Alle möglichen Pferdbewegungen, falls die entsprechenden Felder frei oder von Gegnern besetzt sind
    for index in indexes: # Durchlaufen jedes indexes und überprüfen, ob das entsprechende Feld frei oder von einem Gegner besetzt ist
        if rFieldNumber + index - 1 < 64 and rFieldNumber + index - 1 > -1: # Verhindern eines Index out of Range Errors, indem überprüft wird, ob der Azufragende Index innerhalb der Range liegt
            field = chessField[rFieldNumber + index - 1]
            if ((rRow == 8 or rRow == 7) and field[13] < 5) or ((rRow == 1 or rRow == 2) and field[13] > 4): # Verhindern, dass Pferde über die Seitenränder des Schachfeldes springen können 
                continue
            if field[11] == "" or field[11] == enemy:
                possibleMoves.append((field[8], field[9], field[10], field[1]))
                if field[11] == enemy:
                    possibleHitFields.append((field[8], field[9], field[10], field[1])) # Liste mit Feldern die Rot gefärbt werden sollen -> Eine Figur steht auf diesen

    return possibleMoves, possibleHitFields # Zurückgeben aller möglichen Pferdbewegungen


def possibleRockMoves(): # Funktion zum ermitteln aller möglichen Turmzüge

    repaintX, repaintY, repaintTexture, rFigure, rFieldNumber, rCollum, rRow = selectedField[0] # Entpacken des ausgewählten Feldes
    possibleMoves = []
    possibleHitFields = []
        
    tupleList = [(rCollum, 8, 0, -1), (rCollum, 8, 9, 1), (rRow, 1, 0, -1), (rRow, 1, 9, 1)] #[0]: Spalte oder Zeile [1]: Felder, die im index vor / zurück gegangen werden müssen, um das nächste Feld in der Reihe oder Spalte zu ermittlen [2]: Ende, falls die Zeile oder Spalte vor Ende überprüft wird bricht die Schleife nach dieser ab [3]: Zum negieren der Laufrichtung und des Indexes
    for t in tupleList:
        line, number, end, step = t # Entpacken der tuple aus tupleList          
        m = 0 # wird mit dem Index multipliziert pro Durchlauf, damit immer das nächste Feld in die entsprechende Richtung abgefragt wird
        for i in range(line + step, end, step):
            m += 1
            index = number * m * step # Ermitteln des Indexes, der abgefragt werden soll
            field = chessField[rFieldNumber + index - 1]
            if field[11] == "" or field[11] == enemy:
                possibleMoves.append((field[8], field[9], field[10], field[1]))
            if field[11] != "": # Schleifenabbruch bei Gegner oder bei eigner Figur | Bei Gegner wird dieser zuvor noch ermittelt und in die möglichen Züge aufgenommen
                possibleHitFields.append((field[8], field[9], field[10], field[1])) # Liste mit Feldern die Rot gefärbt werden sollen -> Eine Figur steht auf diesen
                break
    
    return possibleMoves, possibleHitFields # Zurückgeben aller möglichen Bewegungen für den ausgewählten Turm


def possiblesBishopMoves(): # Funktion zum Ermitteln aller möglichen Läuferbewegungen 

    repaintX, repaintY, repaintTexture, rFigure, rFieldNumber, rCollum, rRow = selectedField[0] # Entpacken des ausgewählten Feldes
    possibleMoves = []
    possibleHitFields = []
    
    tupleList = [(-9, 0, -1, 1), (-7, 0, -1, 2), (7, 9, 1, 3), (9, 9, 1, 4)] # [0]: Feldindex, auf das sich bewegt werden soll, [1]: Reihenende, [2]: Schritt, [3]: Runde (Nummer des Tuples) 
    for t in tupleList:
        line = 0 + rCollum
        number, end, step, runde = t # Entpacken des aktuellen Tuples aus tupleList
        m = 0 # wird mit dem Index multipliziert pro Durchlauf, damit immer das nächste Feld in die entsprechende Richtung abgefragt wird
        for i in range(line + step, end, step):
            m += 1
            index = number * m # Ermitteln des Indexes, der abgefragt werden soll
            if rFieldNumber + index - 1 < 64 and rFieldNumber + index - 1 > -1: # Falls der Index außerhalb des Schachfeldes liegen würde, wird hier abgebrochen, damit ein Error verhindert wird
                field = chessField[rFieldNumber + index - 1]
                if (field[13] == 1  and runde % 2 == 0.0) or (field[13] == 8 and runde % 2 != 0.0): # Falls das ermittelte Feld den entsprechenden Wert hat und der Läufer sich entgegen der Richtung bewegt, also über den Rand gelaufen ist, bricht die Schleife ab, und die Bewegung über den Rand wird nicht mehr erfasst
                    break 
                if (field[11] == "" or field[11] == enemy):
                    possibleMoves.append((field[8], field[9], field[10], field[1]))
                if field[11] != "":
                    possibleHitFields.append((field[8], field[9], field[10], field[1])) # Liste mit Feldern die Rot gefärbt werden sollen -> Eine Figur steht auf diesen
                    break
    
    return possibleMoves, possibleHitFields # Zurückgeben aller ermittelten möglichen Läuferbewegungen 
        
        
# Bedient sich an der Läufer- und Turmfunktion, da sich die Dame wie eine Kombination aus beiden bewegt
def possibleQueenMoves(): # Funktion zum ermitteln aller möglichen Bewegungen für die Dame
    rock, hitFieldsRock = possibleRockMoves()
    bishop, hitFieldsBishop = possiblesBishopMoves()
    
    possibleMoves = rock + bishop # Zusammen führen der möglichen Felder aus beiden Klassen, da sich nicht Turm oder Läufer, sondern Turm und Läufer ist
    possibleHitFields = hitFieldsRock + hitFieldsBishop
    
    return possibleMoves, possibleHitFields # Zurückgeben aller möglichen Zugfelder

            
def possibleKingMoves(): # Funktion zum ermitteln aller möglichen Bewegungen für den König
    global rochadeFigurePlace
    
    repaintX, repaintY, repaintTexture, rFigure, rFieldNumber, rCollum, rRow = selectedField[0] # Entpacken des ausgewählten Feldes
    possibleMoves = []
        
    indexes = [-9, -8, -7, -1, 1, 7, 8, 9] # Alle möglichen Indexe, um die sich der König bewegen kann (rochieren hierbei ausgeschlossen folgt weiter unten in der Funktion)
    for index in indexes:
        if rFieldNumber + index - 1 < 64 and rFieldNumber + index - 1 > -1: # Falls der Index außerhalb des Schachfeldes liegen würde, wird hier abgebrochen, damit ein Error verhindert wird
            field = chessField[rFieldNumber + index - 1]
            if (field[13] == 1  and rRow == 8) or (field[13] == 8 and rRow == 1): # Falls der König vor der Bewegung auf der anderen Seite des Schachfeldes war, wird hier in den nächsten Durchlauf gesprungen und der Wert nicht mehr zu den möglichen Zügen hinzugefügt
                continue
            if field[11] == "" or field[11] == enemy:
                possibleMoves.append((field[8], field[9], field[10], field[1]))
                
            if field[11] == enemy:
                possibleHitFields.append((field[8], field[9], field[10], field[1])) # Liste mit Feldern die Rot gefärbt werden sollen -> Eine Figur steht auf diesen
            
    kingColor = rFigure.rstrip("king").rstrip("_") # Festschreiben der Farbe des Königs in einer Variablen
    oddNumbersr = [-2, -1, 1, -4] # [0]: Bewegung des Königs bei einer Rochade [1]: Bewegung des Turms bei einer Rochade [2]: ID des Turms [3]: Index, bei dem die Überprüfung nach leeren Feldern aufhört  
    evenNumbers = [2, 1, 2, 3]   # [0]: Bewegung des Königs bei einer Rochade [1]: Bewegung des Turms bei einer Rochade [2]: ID des Turms [3]: Index, bei dem die Überprüfung nach leeren Feldern aufhört
    odd = [-1, -2, -3, -4] # Indexe große Rochade
    even = [1, 2, 3] # Indexe kleine Rochade
    
    for i in [(0, "white"), (3, "black")]: # [0]: Index in rochadeMoved zum Überprüfen, ob sich der König bereits bewegt hat [1]: Farbe des zu überprüfenden Königs
        if (not rochadeMoved[i[0]]) and rFigure.startswith(i[1]): # Falls sich der Köing noch nicht bewegt hat und die Farbe des Königs mit der Farbe des ausgewählten Königs übereinstimmt
            r = 0
            for j in [1, 2, 4, 5]: # Indexe in rochadeMoved zum Überprüfen, ob sich die Türme, mit denen rochiert werden soll bereits bewegt haben
                r += 1
                if r % 2 == 0.0:
                    evenOddIndex = [] + evenNumbers
                    evenOrOdd = [] + even
                else:
                    evenOddIndex = [] + oddNumbersr
                    evenOrOdd = [] + odd
                    
                if (i[0] == 0 and (not rochadeMoved[j]) and j < 3) or (i[0] == 3 and (not rochadeMoved[j]) and j > 3): # Falls sich der zu überprüfende Turm sich noch nicht bewegt hat 
                        for index in evenOrOdd:
                            if rFieldNumber + index - 1 < 64 and rFieldNumber + index - 1 > -1: # Falls der Index außerhalb des Schachfeldes liegen würde, wird hier abgebrochen, damit ein Error verhindert wird
                                field = chessField[rFieldNumber + index - 1]
                                if index == evenOddIndex[3] and field[2] == kingColor + "_" + str(evenOddIndex[2]) + "_rock": # Falls der letzte Index für die Rochade erreicht wurde und auf dem letzten Feld der Turm steht, der zu beginn des Spiels auf dem entsprechenden Feld stand
                                    kingField = chessField[rFieldNumber + evenOddIndex[0] - 1] # Feld auf das der König bei der entsprechenden Rochade zieht
                                    rockField = chessField[rFieldNumber + evenOddIndex[1] - 1] # Feld auf das der Turm bei der entsprechenden Rochade zieht
                                    rochadeFigurePlace.append((field[1], kingField[1], kingColor + "_king", dirLocation + "chess" + kingColor + "_0.png", kingColor, (kingField[8], kingField[9], kingField[10]), rockField[1], kingColor + "_" + str(evenOddIndex[2]) + "_rock", dirLocation + "chess" + kingColor +  "_2.png", kingColor, (rockField[8], rockField[9], rockField[10])))                                    
                                    possibleMoves.append((field[8], field[9], field[10], field[1]))
                                if field[11] != "":
                                    break 

    return possibleMoves, possibleHitFields # Zurückgeben aller möglichen Bewegungen
                                        
                                                                                                    
def figureMove(sourceIndex, moveToIndex, automatic = False, illegalMoveTest = False): # Funktion, die Figuren bewegt / die Schachfeldliste an den bestimmten Stellen überschreibt
    global schlagenEnPassant
    global sEPHit
    global chessField
    global moves
    global rochadeMoved
    global rochadeFigurePlace
    
    rochade = False
    
    lastChessField = [] + chessField # Für den Durchlauf eine Kopie des Feldes erstellen, um bei einem illegalen Zug alle Figuren leicht zurücksetzen zu können 
    lastRochadeMoved = [] + rochadeMoved # Für den Durchlauf eine Kopie der Liste erstellen, um bei einem illegalen Zug die Liste mit den bewegten Figuren zurücksetzen zu können
    
    sourceField = chessField[sourceIndex] # s = source / Ausgangsfeld | Das Feld von dem aus sich die Figur bewegt
    moveToField = chessField[moveToIndex] # m = moveto / Endfeld | Das Feld auf das die Figur bewegt werden soll
    
    sFieldKey, sFieldNumber, sFigure, sFigureTexture, sLeftX, sYAbove, sRightX, sYDown, sCenterX, sCenterY, sFieldTexture, sFigureColor, sCollum, sRow = sourceField # Entpacken des source_fields
    mFieldKey, mFieldNumber, mFigure, mFigureTexture, mLeftX, mYAbove, mRightX, mYDown, mCenterX, mCenterY, mFieldTexture, mFigureColor, mCollum, mRow = moveToField # Entpacken des move_to_fields
    
    if not automatic and not illegalMoveTest: # Die folgenden 3 Methoden dürfen nur bei einem Zug und nicht bei einer Zugüberprüfung des Computers aufgerufen werden
        
        if len(sEPHit) != 0 and sFigure.endswith("pawn"): # Falls im letzen Zug sich ein Bauer um 2 Felder nach vorne bewegt hat und somit von einem gegnerischen Bauern, der nun neben ihm steht geschlagen werden könnte
            fX, fY, figureTexture, fFieldNumber, fTargetFieldX, fTargetFieldY, fFigureTexture = sEPHit[0] # Entpacken des 'schlagen en passant' hit 
            if fTargetFieldX == mCenterX and fTargetFieldY == mCenterY: # Falls das 'schlagen en passant' Feld mit den Koordinaten des Feldes, auf das sich die Figur gerade bewegt übereinstimmen 
                hittetPawn = chessField[fFieldNumber - 1]
                hPFieldKey, hPFieldNumber, hPFigure, hPFigureTexture, hPLleftX, hPYAbove, hPRightX, hPYDown, hPCenterX, hPCenterY, hPFieldTexture, hPFigureColor, hPCollum, hPRow = hittetPawn # Entpacken des Feldes mit dem geschlagenen Bauern, da dieser sich nicht auf dem move_to Feld befindet, jedoch trotzdem entfernt werden muss
                chessField[fFieldNumber - 1] = (hPFieldKey, hPFieldNumber, "", "", hPLleftX, hPYAbove, hPRightX, hPYDown, hPCenterX, hPCenterY, hPFieldTexture, "", hPCollum, hPRow) # Verpacken des entsprechenden Feldes / überschreiben
            sEPHit = []
        
        if sFigure.endswith("pawn"): # Abfrage, ob sich ein Bauer in diesem Zug um 16 Felder nach vorne bewegt, um diesen dann in die 'Schlagen en passant' Möglichkeit einzuschreiben 
            if sFieldNumber - 16 == mFieldNumber:
                schlagenEnPassant = [moves + 1, sFieldNumber - 8, mFieldNumber]
            elif sFieldNumber + 16 == mFieldNumber:
                schlagenEnPassant = [moves + 1, sFieldNumber + 8, mFieldNumber]
            
        
            if (mCollum == 1 and sFigure.startswith("white")) or (mCollum == 8 and sFigure.startswith("black")): # Falls ein Bauer sich auf die gegnerische letzte Linie begibt, tauscht er seinen Bauern gegen einen Turm, Pferd, Läufer oder eine Dame ein 
                sure = False
                while not sure:
                    eFigure = inputInt("Bauern ersetzen durch '1' Turm, '2' Pferd, '3' Laeufer, '4' Dame")# Leider hier UI-technisch sehr unschön, ging aber leider nicht anders, da TigerJython auf Maus Callbacks anscheinend Fenster erstellen, diese aber nicht mehr mit Inhalt füllen kann
                    if eFigure == 1:
                        output = "Turm"
                        eFigure = "_rock"
                        eFigureTexture = "_2.png"
                    elif eFigure == 2:
                        output = "Pferd"
                        eFigure = "_knight"
                        eFigureTexture = "_3.png"
                    elif eFigure == 3:
                        output = "Laeufer"
                        eFigure = "_bishop"
                        eFigureTexture = "_4.png"
                    elif eFigure == 4:
                        output = "Dame"
                        eFigure = "_queen"
                        eFigureTexture = "_1.png"
                    else:
                        continue # Hier ein else mit contínue, um den restlichen Schleifendurchlauf, also die 'sure' Zuweisung mit der Frage zu überspringen, da eine Zahl eingegeben wurde, der keine Figur zugeordent ist
                    sure = askYesNo("Moechtest du deinen Bauern wirklich durch eine*n " + output + " ersetzen?")
                
                sFigure = sFigureColor + eFigure
                sFigureTexture = dirLocation + "chess" + sFigureColor + eFigureTexture                               
                                                            
                                                            
        if sFigure.endswith("king"): # Dekativiren der Rochademöglichkeit für die entsprechende Figur, falls sich diese bewegt
            if sFigure.startswith("white"):
                rochadeMoved[0] = True
            if sFigure.startswith("black"):
                rochadeMoved[3] = True
        if sFigure.endswith("rock"):
            if sFigure.startswith("white"):
                if sFigure == "white_1_rock":
                    rochadeMoved[1] = True
                if sFigure == "white_2_rock":
                    rochadeMoved[2] = True
            if sFigure.startswith("black"):
                if sFigure == "black_1_rock":
                    rochadeMoved[4] = True
                if sFigure == "black_2_rock":
                    rochadeMoved[5] = True 
    
    mFigure = "" + sFigure
    mFigureTexture = "" + sFigureTexture
    mFigureColor = "" + sFigureColor
    
    sFigure = ""
    sFigureTexture = ""
    sFigureColor = ""
    
    if len(rochadeFigurePlace) != 0: # Falls eine Rochade durchgeführt werden könnte
        for t in rochadeFigurePlace:
            clickedField, kFieldNumber, k, kTexture, kColor, kT, rockFieldNumber, rock, rockTexture, rockColor, rockT = t
            if clickedField - 1 == moveToIndex: # Prüft für jede Rochade, die in diesem Zug hätte durchgeführt werden können, ob sie durchgeführt wurde
                
                kingField = chessField[kFieldNumber - 1] # weder source noch moveto Feld, da sich König und Turm bei der Rochade auf andere Felder bewegen, weshalb hier diese Felder entpackt werden müssen
                rockField = chessField[rockFieldNumber - 1] # weder source noch moveto Feld, da sich König und Turm bei der Rochade auf andere Felder bewegen, weshalb hier diese Felder entpackt werden müssen
                
                eKFieldKey, eKFieldNumber, eKFigure, eKFigureTexture, eKLeftX, eKYAbove, eKRightX, eKYDown, eKCenterX, eKCenterY, eKFieldTexture, eKFigureColor, eKCollum, eKRow = kingField
                eRockFieldKey, eRockFieldNumber, eRockFigure, eRockFigureTexture, eRockLeftX, eRockYAbove, eRockRightX, eRockYDown, eRockCenterX, eRockCenterY, eRockFieldTexture, eRockFigureColor, eRockCollum, eRockRow = rockField    
                
                # Einpacken der Überschriebenden Felder
                chessField[kFieldNumber - 1] = (eKFieldKey, eKFieldNumber, k, kTexture, eKLeftX, eKYAbove, eKRightX, eKYDown, eKCenterX, eKCenterY, eKFieldTexture, kColor, eKCollum, eKRow)
                chessField[rockFieldNumber - 1] = (eRockFieldKey, eRockFieldNumber, rock, rockTexture, eRockLeftX, eRockYAbove, eRockRightX, eRockYDown, eRockCenterX, eRockCenterY, eRockFieldTexture, rockColor, eRockCollum, eRockRow)    
                
                rochade = True
            
                rochadeFigurePlace = []    
                # Moveto leeren, da sich Turm und König ja bereits auf andere Felder bewegt haben 
                mFigure = ""
                mFigureTexture = ""
                mFigureColor = "" 
    
    chessField[sourceIndex] = (sFieldKey, sFieldNumber, sFigure, sFigureTexture, sLeftX, sYAbove, sRightX, sYDown, sCenterX, sCenterY, sFieldTexture, sFigureColor, sCollum, sRow)
    chessField[moveToIndex] = (mFieldKey, mFieldNumber, mFigure, mFigureTexture, mLeftX, mYAbove, mRightX, mYDown, mCenterX, mCenterY, mFieldTexture, mFigureColor, mCollum, mRow)
    
    kingGetter() # Ermitteln der neuen Königsfelder
            
    if illegalMoveTest:
        check = checkCheck() # Überprüfung auf einen illegalen Zug
        kingGetter() 
        chessField = [] + lastChessField # Feld mit der erstellten Kopie überschreiben
        rochadeMoved = [] + lastRochadeMoved # Liste mit den bewegten Rochadefiguren auf Stand vor dem illegalen Zug zurücksetzen
        return check

        
    if not automatic and not illegalMoveTest: # Bei automatischem Programmdurchlauf würden im folgendem weitere automatische Programmdurchläufe entstehen
        moves += 1  
        return sourceIndex
    
    if automatic:
        return sourceField, sourceIndex, moveToField, moveToIndex # Beim Automatischen durchlaufen die Ursprungsfelder zurückgeben, damit diese nach der automatischen Figurbewegung sich nicht ändern

def decolor(notMoved = False): # Funktion zum Entfärben der gedfärbten Felder
    global lastPossibleFields
    global rochadeFigurePlace
    global possibleHitFields
    global selectedField

    lastPossibleFields = [] # Leeren der Listen und danach repainten wichtig, um Feld neu zu "malen"
    rochadeFigurePlace = []
    possibleHitFields = []
    selectedField = []    
    
    if notMoved:
        repaint() # Repainten, um alle Färbungen zu entfernen


def checkCheck(): # Funktion zum Überprüfen ob der König im Schach steht
    global selectedField
    
    Check = False
    runde = 0
    for largeTuple in chessField: # Für jedes Feld prüfen, ob eine gegnerische Figur auf diesem steht
        selectedField = [(largeTuple[8], largeTuple[9], largeTuple[10], largeTuple[2], largeTuple[1], largeTuple[12], largeTuple[13]), runde] # Neue Werte des Feldes zuweisen, wichtig da sonst die Überprüfung der Möglichen bewegungen der Figuren nicht funktioniert
        if largeTuple[11] == enemy:
            playerChange() # Wechseln des Gegners wichtig, da für gegnerische Figuren ermittelt werden soll, ob diese den eingen König schlagen könnten 
            lastPossibleFields, possibleHitFields = checkFigureType(largeTuple[2]) # Funktionsaufruf mit der Figur, die auf dem aktuell überprüften Feld steht
            playerChange() # Wichtig, da die Schlagmöglichkeit der gegnerischen Figuren gegen den EINGENEN König getestet werden soll
            for fieldTuple in lastPossibleFields: # Überprüfen für jedes mögliche Feld, das zuvor ermittelt wurde, ob die Figur den gegnerischen König schlagen könnte
                for king in kingFields:
                    if king[3] == activePlayer and (fieldTuple[0] == king[0] and fieldTuple[1] == king[1]):
                        Check = True # Schach-Situation durch eine Figur erkannt
        runde += 1
    return Check # Zurückgeben von 'False' oder 'True', jenachdem, ob ein König im Schach steht oder nicht

         
def checkCheckMate(): # Funktion zum Überprüfen, ob ein Spieler Schachmatt ist | wird nur aufgerufen, falls ein König im Schach steht
    global selectedField
    
    check = True
    runde = 0
    for tTuple in chessField:
        selectedField = [(tTuple[8], tTuple[9], tTuple[10], tTuple[2], tTuple[1], tTuple[12], tTuple[13]), runde] # Neue Werte des Feldes zuweisen, wichtig da sonst die Überprüfung der Möglichen bewegungen der Figuren nicht funktioniert
        if tTuple[11] == activePlayer:
            lastPossibleFields, possibleHitFields = checkFigureType(tTuple[2])
            for possibleField in lastPossibleFields:
                lRunde = 0
                for largeTuple in chessField:
                    if possibleField[0] == largeTuple[8] and possibleField[1] == largeTuple[9]:
                        lSelectedField = [(largeTuple[8], largeTuple[9], largeTuple[10], largeTuple[2], largeTuple[1], largeTuple[12], largeTuple[13]), runde] # Neue Werte des Feldes zuweisen, wichtig da sonst die Überprüfung der Möglichen bewegungen der Figuren nicht funktioniert
                        sourceField, sourceIndex, moveToField, moveToIndex = figureMove(lSelectedField[1], lRunde, True)
                        check = checkCheck() # Prüfen, ob König noch im Schach steht, wenn nicht wird die Funktion abgebrochen
                        chessField[sourceIndex] = sourceField # Zurücksetzen der Figuren auf ihre Ursprungsfelder
                        chessField[moveToIndex] = moveToField
                        
                        kingGetter() # Ermitteln, auf welchen Feldern die Könige stehen, da diese möglicher Weise bewegt wurden
                        
                    if not check:
                        return check # Bricht Funktion ab, da es eine Möglichkeit gibt aus dem "Schach" herauszokommen
                    lRunde += 1  
        runde += 1                   
    return check # Zurückgeben von 'False' oder 'True', jenachdem, ob ein König im Schachmatt ist oder nicht      

                          
def checkStalemate(): # Funktion zum Überprüfen auf ein Unentschieden
    stalemate = checkCheckMate() # Prüfen, ob sich eine Figur bewegen kann, ohne dass der König nach der Bewegung im Schach steht
    
    if not stalemate: # Falls dies möglich ist, wird geguckt, ob es nur noch 2 Könige gibt, wodurch ebenfalls ein Unentschieden entsteht
        for field in chessField:
            if not (field[2].endswith("king") or field[2] == ""): # Falls es ein Feld gibt, auf dem etwas anderes als nichts oder ein König steht wird die Schleife abgebrochen
                break # Hier sehr nützlich, da nur durch dieses Break das Else-Statement nicht ausgelöst wird
        else: # Fall das Break nicht einmal aufgerufen wurde, gibt es ein Unentschieden
            stalemate = True
                
    return stalemate # Zurückgeben von False oder True, jenachdem, ob das Spiel unentschieden ist oder nicht


def playerChange(): # Funktion zum wechseln der Spieler
    global activePlayer
    global activePlayerText
    global enemy
    
    if activePlayer == "white":
        activePlayer = "black"
        activePlayerText = "Schwarz"
        enemy = "white"

    else:
        activePlayer = "white"
        activePlayerText = "Weiss"
        enemy = "black"


def kingGetter(): # Funktion zum Ermitteln der Positionen der Könige
    global kingFields
    
    for t in chessField: # Neu ermitteln des Königfeldes, falls dieses durch das Programm verändert wurde
        if t[2].endswith("king"):
            if t[2].startswith("black"):
                kingFields[0] = t[8], t[9], t[10], "black"
            elif t[2].startswith("white"):
                kingFields[1] = t[8], t[9], t[10], "white" 
                                                                                    
        
def checkFigureType(figure): # Funktion zum überprüfen, für welche Figur die nächst möglichen Felder ausgegeben werden soll
    
    if figure.endswith("pawn"):
        lastPossibleFields, possibleHitFields = possiblePawnMoves()   
    if figure.endswith("knight"):
        lastPossibleFields, possibleHitFields = possibleKnightMoves()    
    if figure.endswith("rock"):
        lastPossibleFields, possibleHitFields = possibleRockMoves()  
    if figure.endswith("bishop"):
        lastPossibleFields, possibleHitFields = possiblesBishopMoves()   
    if figure.endswith("queen"):
        lastPossibleFields, possibleHitFields = possibleQueenMoves()      
    if figure.endswith("king"):
        lastPossibleFields, possibleHitFields = possibleKingMoves()    
    
    return lastPossibleFields, possibleHitFields # Zurückgeben der möglichen ermittelten Felder           


@gt.onMouseClicked    
def figureSelect(x, y): # Funktion die auf Aufruf des obigen Mauscallbacks aufgrufen und ausgeführt wird | Der Mauscallback übergibt die angeklickten Koordinaten, mit welchen im Folgenden die anglickte Position überprüft wird
    global sEPHit
    global selectedField
    global lastPossibleFields
    global inputAllowed
    global possibleHitFields
    global rochadeFigurePlace
    global chessField
    
    index = 0
    if inputAllowed and playerEnemy != activePlayer: # Solange True, bis ein König fällt
        for largeTuple in chessField: # Durchgehen jedes Feldes bis ein Feld mit den angeklickten Koordianten übereinstimmt, auf diesem werden dann die weiteren Schritte ausgeführt
            moved = False
            fieldKey, fieldNumber, figure, figureTexture, leftX, yAbove, rightX, yDown, centerX, centerY, fieldTexture, figureColor, collum, row = largeTuple # Entpacken des Schachfeld Tupels
            if (x >= leftX and y <= yAbove) and (x <= rightX and y >= yDown): # Prüft ob das oben entpackte Schachfeld zu den angeklickten Koordinaten passt
                kingGetter() # Wichtig, da es sonst zu illegalen Zugmöglichkeiten kommen kann, da die Könige noch auf anderen Feldern regestriert sind
                if len(lastPossibleFields) != 0: # Falls bereits eine Figur ausgewählt wurde und Bewegungsmöglichkeiten für die Figur grün gefärbt wurden wir als erstes geprüft, ob das angeklickte Feld eines derer ist, auf die sich die Figur bewegen kann
                    for possibleField in lastPossibleFields: 
                        if centerX == possibleField[0] and centerY == possibleField[1]: # Falls die Center mit den Centern des aktuellen Feldes übereinstimmen 
                            moved = True
                            clientSocket.send((selectedField[1], index)) # Senden der Bewegung an den Server, damit beide Clients ihre Spielfelder updaten
                            selectedField = []
                            break
                if moved:
                    break # Keine Andere Möglichkeit gefunden | Schleife muss im if Fall sofort abgebrochen werden, da es sonst zu verherenden Fehlern kommen kann
                if figure != "" and figureColor == activePlayer: # Falls das angeklickte Feld nicht leer und die Figurenfarbe mit dem aktiven Spieler übereinstimmt
                    decolor(True)
                    selectedField.append((centerX, centerY, fieldTexture, figure, fieldNumber, collum, row))# Nach leeren und entfärben wird hier die neu ausgewählte Figur aufgenommen
                    selectedField.append(index) # Speichern des Indexes des ausgewählten Feldes | Wichtig für die move Funktion
                    gt.setPos(centerX - (25 * mScreenW) , centerY)
                    gt.setFillColor("lightblue") # Makieren der ausgewählten Figur durch färben des Feldes unter ihr
                    gt.fill()
                    
                    lastPossibleFields, possibleHitFields = checkFigureType(figure) # Funktionsaufrufe je nach ausgewählter Figur
                    newPossibleMoves = []
                    for lTuple in lastPossibleFields: # Für jedes possible Field wird geguckt, ob der Zug legal wäre, wenn nicht wird das Feld nicht zur neuen Liste hinzugefügt, die die Alte dann ersetzt
                        selectedCopy = [] + selectedField # Copy von selectedField, da dieses sich ändert und sonst nichts mehr funktioniert
                        figureHitCopy = [] + possibleHitFields
                        rochadeCopy = [] + rochadeFigurePlace
                        
                        check = figureMove(selectedField[1], lTuple[3] - 1, False, True) # Hier wird die legalität des möglichen Zuges überprüft
                        
                        selectedField = [] + selectedCopy # selectedField mit der erzeugten Kopie überschreiben
                        possibleHitFields = [] + figureHitCopy
                        rochadeFigurePlace = [] + rochadeCopy
                        
                        if not check: # Falls der mögliche Zug nicht illegal ist, wird er zu den neuen möglichen Zügen hinzugefügt
                            newPossibleMoves.append(lTuple)
                    lastPossibleFields = [] + newPossibleMoves # Überschreiben der Liste mit dedn möglichen Feldern, mit den möglichen legalen Feldern
                    
                    newHitFields = []
                    for f in possibleHitFields: # Überprüfen, ob eine Schlagmöglichkeit soeben als illegal erkannt wurde, falls dies der Fall ist MUSS dieses Feld auch aus figure_hit_field entfernt werden
                        for l in lastPossibleFields:
                            if f == l: # Falls das Hit field noch in den möglichen ist, wird es der neuen Liste hinzugefügt
                                newHitFields.append(f)
                    possibleHitFields = [] + newHitFields # Überschreiben der alten möglichen Schläge mit den möglichen legalen Schlägen
                    
                    newRochadeFields = []
                    for f in rochadeFigurePlace:
                            for l in lastPossibleFields:
                                if f[0] == l[3]: # Wenn die Feldnummern übereinstimmen
                                    newRochadeFields.append(f)
                    rochadeFigurePlace = [] + newRochadeFields
                                
                          
                    for f in lastPossibleFields: # Färben der möglichen Züge 
                        fX, fY, fieldTexture, fNumber = f
                        gt.setPos(fX - (25 * mScreenW), fY) # -25, da es sonst zu Färbfehlern kommt
                        gt.setFillColor("lime")
                        gt.fill()
                    for f in rochadeFigurePlace: # Färben der Felder für König und Turm bei einer Rochade
                        for t in f:
                            if type(t) is tuple:
                                tX, tY, fieldTexture = t
                                gt.setPos(tX - (25 * mScreenW), tY) # -25, da es sonst zu Färbfehlern kommt
                                gt.setFillColor("purple")
                                gt.fill()
                    for f in possibleHitFields:
                        fX, fY, fieldTexture, fNumber = f
                        gt.setPos(fX - (25 * mScreenW), fY) # -25, da es sonst zu Färbfehlern kommt
                        gt.setFillColor("red")
                        gt.fill()
                        
            index += 1 # Nach einem Schleifendurchlauf wird der Index um 1 erhöht 
          
