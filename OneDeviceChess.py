import pygame
import os
import sys
import time
import Values

if __name__ == "__main__":
    sys.exit("Starte Gamemode.py, um das Spiel zu starten")

screenW = Values.screenW
screenH = Values.screenH

mScreenW = screenW / 800
mScreenH = screenH / 800  # Teilen durch 800, da das Schachfeld in einem 800 x 800 Feld eingerichtet ist

fileDir = os.getcwd()  # Speichern des Verzeichnisses, in dem das Programm läuft in der Variable fileDir, damit die Figur texturen im Ordner in diesem Verzeichnis gefunden werden können
chessFigures = "chessfigures/"  # Name des Ordners, indem sich die Texturen für die Schachfiguren befinden
dirLocation = os.path.join(fileDir, chessFigures)  # Anfügen des Ordnernamen an das Verzeichnis

white = (250, 250, 250)
gray = (198, 198, 198)


# Schachfeld
                #   0           1          2          3          4       5       6        7           8            9         10    11
chessField = [  # fieldKey, fieldNumber, figure, figureTexture, leftX, yAbove, centerX, centerY, fieldTexture, figureColor, column, row
    ("8a", 1, "black_1_rook", dirLocation + "chessblack_2.svg", 0 * mScreenW, 0 * mScreenH, 50 * mScreenW, 50 * mScreenH, white, "black", 1, 1), ("8b", 2, "black_knight", dirLocation + "chessblack_3.svg", 100 * mScreenW, 0 * mScreenH, 150 * mScreenW, 50 * mScreenH, gray, "black", 1, 2), ("8c", 3, "black_bishop", dirLocation + "chessblack_4.svg", 200 * mScreenW, 0 * mScreenH, 250 * mScreenW, 50 * mScreenH, white, "black", 1, 3), ("8d", 4, "black_queen", dirLocation + "chessblack_1.svg", 300 * mScreenW, 0 * mScreenH, 350 * mScreenW, 50 * mScreenH, gray, "black", 1, 4), ("8e", 5, "black_king", dirLocation + "chessblack_0.svg", 400 * mScreenW, 0 * mScreenH, 450 * mScreenW, 50 * mScreenH, white, "black", 1, 5), ("8f", 6, "black_bishop", dirLocation + "chessblack_4.svg", 500 * mScreenW, 0 * mScreenH, 550 * mScreenW, 50 * mScreenH, gray, "black", 1, 6), ("8g", 7, "black_knight", dirLocation + "chessblack_3.svg", 600 * mScreenW, 0 * mScreenH, 650 * mScreenW, 50 * mScreenH, white, "black", 1, 7), ("8h", 8, "black_2_rook", dirLocation + "chessblack_2.svg", 700 * mScreenW, 0 * mScreenH, 750 * mScreenW, 50 * mScreenH, gray, "black", 1, 8),
    ("7a", 9, "black_pawn", dirLocation + "chessblack_5.svg", 0 * mScreenW, 100 * mScreenH, 50 * mScreenW, 150 * mScreenH, gray, "black", 2, 1), ("7b", 10, "black_pawn", dirLocation + "chessblack_5.svg", 100 * mScreenW, 100 * mScreenH, 150 * mScreenW, 150 * mScreenH, white, "black", 2, 2), ("7c", 11, "black_pawn", dirLocation + "chessblack_5.svg", 200 * mScreenW, 100 * mScreenH, 250 * mScreenW, 150 * mScreenH, gray, "black", 2, 3), ("7d", 12, "black_pawn", dirLocation + "chessblack_5.svg", 300 * mScreenW, 100 * mScreenH, 350 * mScreenW, 150 * mScreenH, white, "black", 2, 4), ("7e", 13, "black_pawn", dirLocation + "chessblack_5.svg", 400 * mScreenW, 100 * mScreenH, 450 * mScreenW, 150 * mScreenH, gray, "black", 2, 5), ("7f", 14, "black_pawn", dirLocation + "chessblack_5.svg", 500 * mScreenW, 100 * mScreenH, 550 * mScreenW, 150 * mScreenH, white, "black", 2, 6), ("7g", 15, "black_pawn", dirLocation + "chessblack_5.svg", 600 * mScreenW, 100 * mScreenH, 650 * mScreenW, 150 * mScreenH, gray, "black", 2, 7), ("7h", 16, "black_pawn", dirLocation + "chessblack_5.svg", 700 * mScreenW, 100 * mScreenH, 750 * mScreenW, 150 * mScreenH, white, "black", 2, 8),
    ("6a", 17, "", "", 0 * mScreenW, 200 * mScreenH, 50 * mScreenW, 250 * mScreenH, white, "", 3, 1), ("6b", 18, "", "", 100 * mScreenW, 200 * mScreenH, 150 * mScreenW, 250 * mScreenH, gray, "", 3, 2), ("6c", 19, "", "", 200 * mScreenW, 200 * mScreenH, 250 * mScreenW, 250 * mScreenH, white, "", 3, 3), ("6d", 20, "", "", 300 * mScreenW, 200 * mScreenH, 350 * mScreenW, 250 * mScreenH, gray, "", 3, 4), ("6e", 21, "", "", 400 * mScreenW, 200 * mScreenH, 450 * mScreenW, 250 * mScreenH, white, "", 3, 5), ("6f", 22, "", "", 500 * mScreenW, 200 * mScreenH, 550 * mScreenW, 250 * mScreenH, gray, "", 3, 6), ("6g", 23, "", "", 600 * mScreenW, 200 * mScreenH, 650 * mScreenW, 250 * mScreenH, white, "", 3, 7), ("6h", 24, "", "", 700 * mScreenW, 200 * mScreenH, 750 * mScreenW, 250 * mScreenH, gray, "", 3, 8),
    ("5a", 25, "", "", 0 * mScreenW, 300 * mScreenH, 50 * mScreenW, 350 * mScreenH, gray, "", 4, 1), ("5b", 26, "", "", 100 * mScreenW, 300 * mScreenH, 150 * mScreenW, 350 * mScreenH, white, "", 4, 2), ("5c", 27, "", "", 200 * mScreenW, 300 * mScreenH, 250 * mScreenW, 350 * mScreenH, gray, "", 4, 3), ("5d", 28, "", "", 300 * mScreenW, 300 * mScreenH, 350 * mScreenW, 350 * mScreenH, white, "", 4, 4), ("5e", 29, "", "", 400 * mScreenW, 300 * mScreenH, 450 * mScreenW, 350 * mScreenH, gray, "", 4, 5), ("5f", 30, "", "", 500 * mScreenW, 300 * mScreenH, 550 * mScreenW, 350 * mScreenH, white, "", 4, 6), ("5g", 31, "", "", 600 * mScreenW, 300 * mScreenH, 650 * mScreenW, 350 * mScreenH, gray, "", 4, 7), ("5h", 32, "", "", 700 * mScreenW, 300 * mScreenH, 750 * mScreenW, 350 * mScreenH, white, "", 4, 8),
    ("4a", 33, "", "", 0 * mScreenW, 400 * mScreenH, 50 * mScreenW, 450 * mScreenH, white, "", 5, 1), ("4b", 34, "", "", 100 * mScreenW, 400 * mScreenH, 150 * mScreenW, 450 * mScreenH, gray, "", 5, 2), ("4c", 35, "", "", 200 * mScreenW, 400 * mScreenH, 250 * mScreenW, 450 * mScreenH, white, "", 5, 3), ("4d", 36, "", "", 300 * mScreenW, 400 * mScreenH, 350 * mScreenW, 450 * mScreenH, gray, "", 5, 4), ("4e", 37, "", "", 400 * mScreenW, 400 * mScreenH, 450 * mScreenW, 450 * mScreenH, white, "", 5, 5), ("4f", 38, "", "", 500 * mScreenW, 400 * mScreenH, 550 * mScreenW, 450 * mScreenH, gray, "", 5, 6), ("4g", 39, "", "", 600 * mScreenW, 400 * mScreenH, 650 * mScreenW, 450 * mScreenH, white, "", 5, 7), ("4h", 40, "", "", 700 * mScreenW, 400 * mScreenH, 750 * mScreenW, 450 * mScreenH, gray, "", 5, 8),
    ("3a", 41, "", "", 0 * mScreenW, 500 * mScreenH, 50 * mScreenW, 550 * mScreenH, gray, "", 6, 1), ("3b", 42, "", "", 100 * mScreenW, 500 * mScreenH, 150 * mScreenW, 550 * mScreenH, white, "", 6, 2), ("3c", 43, "", "", 200 * mScreenW, 500 * mScreenH, 250 * mScreenW, 550 * mScreenH, gray, "", 6, 3), ("3d", 44, "", "", 300 * mScreenW, 500 * mScreenH, 350 * mScreenW, 550 * mScreenH, white, "", 6, 4), ("3e", 45, "", "", 400 * mScreenW, 500 * mScreenH, 450 * mScreenW, 550 * mScreenH, gray, "", 6, 5), ("3f", 46, "", "", 500 * mScreenW, 500 * mScreenH, 550 * mScreenW, 550 * mScreenH, white, "", 6, 6), ("3g", 47, "", "", 600 * mScreenW, 500 * mScreenH, 650 * mScreenW, 550 * mScreenH, gray, "", 6, 7), ("3h", 48, "", "", 700 * mScreenW, 500 * mScreenH, 750 * mScreenW, 550 * mScreenH, white, "", 6, 8),
    ("2a", 49, "white_pawn", dirLocation + "chesswhite_5.svg", 0 * mScreenW, 600 * mScreenH, 50 * mScreenW, 650 * mScreenH, white, "white", 7, 1), ("2b", 50, "white_pawn", dirLocation + "chesswhite_5.svg", 100 * mScreenW, 600 * mScreenH, 150 * mScreenW, 650 * mScreenH, gray, "white", 7, 2), ("2c", 51, "white_pawn", dirLocation + "chesswhite_5.svg", 200 * mScreenW, 600 * mScreenH, 250 * mScreenW, 650 * mScreenH, white, "white", 7, 3), ("2d", 52, "white_pawn", dirLocation + "chesswhite_5.svg", 300 * mScreenW, 600 * mScreenH, 350 * mScreenW, 650 * mScreenH, gray, "white", 7, 4), ("2e", 53, "white_pawn", dirLocation + "chesswhite_5.svg", 400 * mScreenW, 600 * mScreenH, 450 * mScreenW, 650 * mScreenH, white, "white", 7, 5), ("2f", 54, "white_pawn", dirLocation + "chesswhite_5.svg", 500 * mScreenW, 600 * mScreenH, 550 * mScreenW, 650 * mScreenH, gray, "white", 7, 6), ("2g", 55, "white_pawn", dirLocation + "chesswhite_5.svg", 600 * mScreenW, 600 * mScreenH, 650 * mScreenW, 650 * mScreenH, white, "white", 7, 7), ("2h", 56, "white_pawn", dirLocation + "chesswhite_5.svg", 700 * mScreenW, 600 * mScreenH, 750 * mScreenW, 650 * mScreenH, gray, "white", 7, 8),
    ("1a", 57, "white_1_rook", dirLocation + "chesswhite_2.svg", 0 * mScreenW, 700 * mScreenH, 50 * mScreenW, 750 * mScreenH, gray, "white", 8, 1), ("1b", 58, "white_knight", dirLocation + "chesswhite_3.svg", 100 * mScreenW, 700 * mScreenH, 150 * mScreenW, 750 * mScreenH, white, "white", 8, 2), ("1c", 59, "white_bishop", dirLocation + "chesswhite_4.svg", 200 * mScreenW, 700 * mScreenH, 250 * mScreenW, 750 * mScreenH, gray, "white", 8, 3), ("1d", 60, "white_queen", dirLocation + "chesswhite_1.svg", 300 * mScreenW, 700 * mScreenH, 350 * mScreenW, 750 * mScreenH, white, "white", 8, 4), ("1e", 61, "white_king", dirLocation + "chesswhite_0.svg", 400 * mScreenW, 700 * mScreenH, 450 * mScreenW, 750 * mScreenH, gray, "white", 8, 5), ("1f", 62, "white_bishop", dirLocation + "chesswhite_4.svg", 500 * mScreenW, 700 * mScreenH, 550 * mScreenW, 750 * mScreenH, white, "white", 8, 6), ("1g", 63, "white_knight", dirLocation + "chesswhite_3.svg", 600 * mScreenW, 700 * mScreenH, 650 * mScreenW, 750 * mScreenH, gray, "white", 8, 7), ("1h", 64, "white_2_rook", dirLocation + "chesswhite_2.svg", 700 * mScreenW, 700 * mScreenH, 750 * mScreenW, 750 * mScreenH, white, "white", 8, 8)
]

kingFields = [(50 * mScreenW, 350 * mScreenH, white, "black"), (50 * mScreenW, -350 * mScreenH, gray, "white")]  # centerX, centerY, fieldColor, figureColor

selectedField = []
rochadeFigurePlace = []
lastPossibleFields = []
possibleHitFields = []
schlagenEnPassant = [0, 0, 0]  # [move, sourceField, MoveToField] (move: ZUg in dem der Bauer geschlagen werden könnte)
sEPHit = []
rochadeAllowed = True
rochadeMoved = [False, False, False, False, False, False]  # w_king, w_1_rook, w_2_rook, b_king, b_1_rook, b_2_rook | Falls bereits bewegt -> entsprechender Wert == True
activePlayer = "white"
activePlayerText = "Weiss"
enemy = "black"
inputAllowed = True
moves = 0


def repaint():  # Neu zeichen des Schachfeldes nach einer Bewegung --->>> Einfachste Möglichkeit Figur texturen wieder vom Feld zu entfernen
    pygameWindow.fill((250, 250, 250))  # Komplettes Fenster neu färben, da sonst Grafikfehler entstehen

    for i in range(0, 801, 100):  # Spaltenstriche, damit das kolorieren der Felder korrekt funktioniert
        for j in range(0, 801, 100):  # Zeilenstriche, damit das kolorieren der Felder korrekt funktioniert
            if (i + j) % 200 == 0:
                color = (255, 255, 255)
            else:
                color = (198, 198, 198)
            pygame.draw.rect(pygameWindow, color, (i * mScreenW, j * mScreenH, 100 * mScreenW, 100 * mScreenH))

    figureRepaint()

    elapsedTime = time.time() - gameStart
    timer = elapsedTime // 60

    pygame.display.set_caption("Aktiver Spieler : " + activePlayerText + "  |    " + str(moves) + "  :  Züge insgesamt --- Spielzeit :  " + str(int(timer)) + " min")  # Nur in Minuten, da Timer nicht fortlaufend, sondern nur bei Aktionen aktualisiert wird
    pygame.display.update()


def figureRepaint():
    for largeTupel in chessField:  # Für jedes Schachfeld die Mittelpunktkoordinaten, die Feldfarbe und die sích auf dem Feld befindliche Figur entnehmen und im Folgendem aufs Spielfeld zeichnen
        centerX = largeTupel[6]
        centerY = largeTupel[7]
        figureTexture = largeTupel[3]

        if figureTexture != "":

            image = pygame.image.load(figureTexture)
            image_rect = image.get_rect()

            a = (centerX - image_rect.width // 2)
            b = (centerY - image_rect.height // 2)

            pygameWindow.blit(image, (a, b))
    pygame.display.update()


def possiblePawnMoves():  # Funktion die alle möglichen Bewegungen für den ausgewählten Bauern zurückgibt
    global sEPHit
    
    repaintX, repaintY, repaintTexture, rFigure, rFieldNumber, rColumn, rRow = selectedField[0]  # Entpacken des ausgewählten Feldes
    possibleMoves = []
    possibleHitFieldsPawn = []
    
    indexes = [-16, -9, -8, -7, 7, 8, 9, 16]  # Alle Indexe, um die sich ein Bauer bewegen kann | Negativ: Weiß Positiv: Schwarz
    for index in indexes:  # Durchlaufen aller Indexe
        sEPColor = False  # Falls True wird das Feld hinter dem Bauern rot gefärbt
        if (rFigure.startswith("black") and index > 0) or (rFigure.startswith("white") and index < 0):  # Überspringen der Indexe, um die sich ein schwarzer bzw. weißer Bauer nicht bewegen kann
            if 64 > rFieldNumber + index - 1 > -1:  # Überprüfen des Indexes, sodass keine Indexe außerhalb der Listenlänge abgefragt wird und es einen Fehler gibt
                field = chessField[rFieldNumber + index - 1]
                if (rRow == 1 and field[11] == 8) or (rRow == 8 and field[11] == 1):  # Abfrage, ob der Bauer am Spielfeldrand herauslaufen würde
                    continue
                if field[9] == "" or field[9] == enemy:  # Falls das zu überprüfende Feld leer ist oder ein Gegner auf diesem steht
                    if not (schlagenEnPassant[0] == moves and field[1] == schlagenEnPassant[1]):  # Implementierung der Regel 'Schlagen en passant' hier falsch, falls diese eine Anwendung finden würde
                        if (abs(index) == 7 or abs(index) == 9) and field[9] != enemy:
                            continue
                    elif abs(index) == 7 or abs(index) == 9:
                        sEPField = chessField[schlagenEnPassant[2] - 1]  # Feld auf dem der 'Schlagen en passant' Bauer steht einlesen
                        sEPColor = True
                        sEPHit = [(sEPField[6], sEPField[7], sEPField[8], sEPField[1], field[6], field[7], field[8])]  # Speichern der Felder, damit diese korrekt gefärbt und falls der Bauer den anderen en passant schlägt dieser entfernt wird
                    if abs(index) == 8 and field[9] != "":  # Bauern können nur nach vorne laufen, wenn das Feld vor ihnen Frei ist
                        continue
                    if abs(index) == 16 and not ((rColumn == 2 and rFigure == "black_pawn") or (rColumn == 7 and rFigure == "white_pawn")):  # Falls der abzufragende Index 16 ist und es sich nicht um einen Bauern handelt, der noch auf seinem Startfeld steht, wird mit dem nächsten Schleifendurchlauf fortgefahren
                        continue
                    if abs(index) == 16:  # Prüft, ob beide Felder (das über welches der Bauer läuft und das auf welchem er landet) frei sind
                        rField = chessField[rFieldNumber + (index // 2) - 1]
                        if rField[9] != "" or field[9] != "":
                            continue
    
                    possibleMoves.append((field[6], field[7], field[8], field[1]))
                    
                    if field[9] == enemy or sEPColor:
                        possibleHitFieldsPawn.append((field[6], field[7], field[8], field[1]))  # Liste mit Feldern, die Rot gefärbt werden sollen: Eine Figur steht auf diesen

    return possibleMoves, possibleHitFieldsPawn  # Zurückgeben aller ermittelten möglichen Bewegungen


def possibleKnightMoves():  # Funktion, die alle möglichen Bewegungen für ein ausgewähltes Pferd zurückgibt
    
    repaintX, repaintY, repaintTexture, rFigure, rFieldNumber, rColumn, rRow = selectedField[0]  # Entpacken des ausgewählten Feldes
    possibleMoves = []
    possibleHitFieldsKnight = []
    
    indexes = [-17, -15, -10, -6, 6, 10, 15, 17]  # Alle möglichen Pferd bewegungen, falls die entsprechenden Felder frei oder von Gegnern besetzt sind
    for index in indexes:  # Durchlaufen jedes indexes und überprüfen, ob das entsprechende Feld frei oder von einem Gegner besetzt ist
        if 64 > rFieldNumber + index - 1 > -1:  # Verhindern eines Index out of Range Errors, indem überprüft wird, ob der Anzufragende Index innerhalb der Range liegt
            field = chessField[rFieldNumber + index - 1]
            if ((rRow == 8 or rRow == 7) and field[11] < 5) or ((rRow == 1 or rRow == 2) and field[11] > 4):  # Verhindern, dass Pferde über die Seitenränder des Schachfeldes springen können
                continue
            if field[9] == "" or field[9] == enemy:
                possibleMoves.append((field[6], field[7], field[8], field[1]))
                if field[9] == enemy:
                    possibleHitFieldsKnight.append((field[6], field[7], field[8], field[1]))  # Liste mit Feldern, die Rot gefärbt werden sollen: Eine Figur steht auf diesen

    return possibleMoves, possibleHitFieldsKnight  # Zurückgeben aller möglichen Pferd bewegungen


def possibleRookMoves():  # Funktion zum Ermitteln aller möglichen Turmzüge

    repaintX, repaintY, repaintTexture, rFigure, rFieldNumber, rColumn, rRow = selectedField[0]  # Entpacken des ausgewählten Feldes
    possibleMoves = []
    possibleHitFieldsRook = []
        
    tupleList = [(rColumn, 8, 0, -1), (rColumn, 8, 9, 1), (rRow, 1, 0, -1), (rRow, 1, 9, 1)]  # [0]: Spalte oder Zeile [1]: Felder, die im index vor / zurückgegangen werden müssen, um das nächste Feld in der Reihe oder Spalte zu ermitteln [2]: Ende, falls die Zeile oder Spalte vor Ende überprüft wird bricht die Schleife nach dieser ab [3]: zum Negieren der Laufrichtung und des Indexes
    for t in tupleList:
        line, number, end, step = t  # Entpacken der tuple aus tupleList
        m = 0  # wird mit dem Index multipliziert pro Durchlauf, damit immer das nächste Feld in die entsprechende Richtung abgefragt wird
        for i in range(line + step, end, step):
            m += 1
            index = number * m * step  # Ermitteln des Indexes, der abgefragt werden soll
            field = chessField[rFieldNumber + index - 1]
            if field[9] == "" or field[9] == enemy:
                possibleMoves.append((field[6], field[7], field[8], field[1]))
            if field[9] != "":  # Schleifenabbruch bei Gegner oder bei eigner Figur | Bei Gegner wird dieser zuvor noch ermittelt und in die möglichen Züge aufgenommen
                possibleHitFieldsRook.append((field[6], field[7], field[8], field[1]))  # Liste mit Feldern, die Rot gefärbt werden sollen: Eine Figur steht auf diesen
                break
    
    return possibleMoves, possibleHitFieldsRook  # Zurückgeben aller möglichen Bewegungen für den ausgewählten Turm


def possiblesBishopMoves():  # Funktion zum Ermitteln aller möglichen Läufer bewegungen

    repaintX, repaintY, repaintTexture, rFigure, rFieldNumber, rColumn, rRow = selectedField[0]  # Entpacken des ausgewählten Feldes
    possibleMoves = []
    possibleHitFieldsBishop = []
    
    tupleList = [(-9, 0, -1, 1), (-7, 0, -1, 2), (7, 9, 1, 3), (9, 9, 1, 4)]  # [0]: Feldindex, auf das sich bewegt werden soll, [1]: Reihenende, [2]: Schritt, [3]: Runde (Nummer des Tuples)
    for t in tupleList:
        line = 0 + rColumn
        number, end, step, runde = t  # Entpacken des aktuellen Tuples aus tupleList
        m = 0  # wird mit dem Index multipliziert pro Durchlauf, damit immer das nächste Feld in die entsprechende Richtung abgefragt wird
        for i in range(line + step, end, step):
            m += 1
            index = number * m  # Ermitteln des Indexes, der abgefragt werden soll
            if 64 > rFieldNumber + index - 1 > -1:  # Falls der Index außerhalb des Schachfeldes liegen würde, wird hier abgebrochen, damit ein Error verhindert wird
                field = chessField[rFieldNumber + index - 1]
                if (field[11] == 1 and runde % 2 == 0.0) or (field[11] == 8 and runde % 2 != 0.0):  # Falls das ermittelte Feld den entsprechenden Wert hat und der Läufer sich entgegen der Richtung bewegt, also über den Rand gelaufen ist, bricht die Schleife ab, und die Bewegung über den Rand wird nicht mehr erfasst
                    break 
                if field[9] == "" or field[9] == enemy:
                    possibleMoves.append((field[6], field[7], field[8], field[1]))
                if field[9] != "":
                    possibleHitFieldsBishop.append((field[6], field[7], field[8], field[1]))  # Liste mit Feldern, die Rot gefärbt werden sollen: Eine Figur steht auf diesen
                    break
    
    return possibleMoves, possibleHitFieldsBishop  # Zurückgeben aller ermittelten möglichen Läufer bewegungen
        
        
# Bedient sich an der Läufer- und Turmfunktion, da sich die Dame wie eine Kombination aus beiden bewegt
def possibleQueenMoves():  # Funktion zum Ermitteln aller möglichen Bewegungen für die Dame
    rook, hitFieldsRook = possibleRookMoves()
    bishop, hitFieldsBishop = possiblesBishopMoves()
    
    possibleMoves = rook + bishop  # Zusammen führen der möglichen Felder aus beiden Klassen, da sich nicht Turm oder Läufer, sondern Turm und Läufer ist
    possibleHitFieldsQueen = hitFieldsRook + hitFieldsBishop
    
    return possibleMoves, possibleHitFieldsQueen  # Zurückgeben aller möglichen Zugfelder

            
def possibleKingMoves():  # Funktion zum Ermitteln aller möglichen Bewegungen für den König
    global rochadeFigurePlace
    
    repaintX, repaintY, repaintTexture, rFigure, rFieldNumber, rColumn, rRow = selectedField[0]  # Entpacken des ausgewählten Feldes
    possibleMoves = []
        
    indexes = [-9, -8, -7, -1, 1, 7, 8, 9]  # Alle möglichen Indexe, um die sich der König bewegen kann (rochieren hierbei ausgeschlossen folgt weiter unten in der Funktion)
    for index in indexes:
        if 64 > rFieldNumber + index - 1 > -1:  # Falls der Index außerhalb des Schachfeldes liegen würde, wird hier abgebrochen, damit ein Error verhindert wird
            field = chessField[rFieldNumber + index - 1]
            if (field[11] == 1 and rRow == 8) or (field[11] == 8 and rRow == 1):  # Falls der König vor der Bewegung auf der anderen Seite des Schachfeldes war, wird hier in den nächsten Durchlauf gesprungen und der Wert nicht mehr zu den möglichen Zügen hinzugefügt
                continue
            if field[9] == "" or field[9] == enemy:
                possibleMoves.append((field[6], field[7], field[8], field[1]))
                
            if field[9] == enemy:
                possibleHitFields.append((field[6], field[7], field[8], field[1]))  # Liste mit Feldern, die Rot gefärbt werden sollen: Eine Figur steht auf diesen
            
    kingColor = rFigure.rstrip("king").rstrip("_")  # Festschreiben der Farbe des Königs in einer Variablen
    oddNumbers = [-2, -1, 1, -4]  # [0]: Bewegung des Königs bei einer Rochade [1]: Bewegung des Turms bei einer Rochade [2]: ID des Turms [3]: Index, bei dem die Überprüfung nach leeren Feldern aufhört
    evenNumbers = [2, 1, 2, 3]   # [0]: Bewegung des Königs bei einer Rochade [1]: Bewegung des Turms bei einer Rochade [2]: ID des Turms [3]: Index, bei dem die Überprüfung nach leeren Feldern aufhört
    odd = [-1, -2, -3, -4]  # Indexe große Rochade
    even = [1, 2, 3]  # Indexe kleine Rochade

    if rochadeAllowed:
        for i in [(0, "white"), (3, "black")]:  # [0]: Index in rochadeMoved zum Überprüfen, ob sich der König bereits bewegt hat [1]: Farbe des zu überprüfenden Königs
            if (not rochadeMoved[i[0]]) and rFigure.startswith(i[1]):  # Falls sich der König noch nicht bewegt hat und die Farbe des Königs mit der Farbe des ausgewählten Königs übereinstimmt
                r = 0
                for j in [1, 2, 4, 5]:  # Indexe in rochadeMoved zum Überprüfen, ob sich die Türme, mit denen rochiert werden soll bereits bewegt haben
                    r += 1
                    if r % 2 == 0.0:
                        evenOddIndex = [] + evenNumbers
                        evenOrOdd = [] + even
                    else:
                        evenOddIndex = [] + oddNumbers
                        evenOrOdd = [] + odd

                    if (i[0] == 0 and (not rochadeMoved[j]) and j < 3) or (i[0] == 3 and (not rochadeMoved[j]) and j > 3):  # Falls sich der zu überprüfende Turm sich noch nicht bewegt hat
                        for index in evenOrOdd:
                            if 64 > rFieldNumber + index - 1 > -1:  # Falls der Index außerhalb des Schachfeldes liegen würde, wird hier abgebrochen, damit ein Error verhindert wird
                                field = chessField[rFieldNumber + index - 1]
                                if index == evenOddIndex[3] and field[2] == kingColor + "_" + str(evenOddIndex[2]) + "_rook":  # Falls der letzte Index für die Rochade erreicht wurde und auf dem letzten Feld der Turm steht, der zu Beginn des Spiels auf dem entsprechenden Feld stand
                                    kingField = chessField[rFieldNumber + evenOddIndex[0] - 1]  # Feld auf das der König bei der entsprechenden Rochade zieht
                                    rookField = chessField[rFieldNumber + evenOddIndex[1] - 1]  # Feld auf das der Turm bei der entsprechenden Rochade zieht
                                    rochadeFigurePlace.append((field[1], kingField[1], kingColor + "_king", dirLocation + "chess" + kingColor + "_0.svg", kingColor, (kingField[6], kingField[7], kingField[8]), rookField[1], kingColor + "_" + str(evenOddIndex[2]) + "_rook", dirLocation + "chess" + kingColor + "_2.svg", kingColor, (rookField[6], rookField[7], rookField[8])))
                                    possibleMoves.append((field[6], field[7], field[8], field[1]))
                                if field[9] != "":
                                    break

    return possibleMoves, possibleHitFields  # Zurückgeben aller möglichen Bewegungen
                                        
                                                                                                    
def figureMove(sourceIndex, moveToIndex, automatic=False, illegalMoveTest=False):  # Funktion, die Figuren bewegt / die Schachfeldliste an den bestimmten Stellen überschreibt
    global schlagenEnPassant
    global sEPHit
    global chessField
    global moves
    global rochadeMoved
    global rochadeFigurePlace
    
    lastChessField = [] + chessField  # Für den Durchlauf eine Kopie des Feldes erstellen, um bei einem illegalen Zug alle Figuren leicht zurücksetzen zu können
    lastRochadeMoved = [] + rochadeMoved  # Für den Durchlauf eine Kopie der Liste erstellen, um bei einem illegalen Zug die Liste mit den bewegten Figuren zurücksetzen zu können
    
    sourceField = chessField[sourceIndex]  # s = source / Ausgangsfeld | Das Feld von dem aus sich die Figur bewegt
    moveToField = chessField[moveToIndex]  # m = moveto / Endfeld | Das Feld auf das die Figur bewegt werden soll
    
    sFieldKey, sFieldNumber, sFigure, sFigureTexture, sLeftX, sYAbove, sCenterX, sCenterY, sFieldTexture, sFigureColor, sColumn, sRow = sourceField  # Entpacken des source_fields
    mFieldKey, mFieldNumber, mFigure, mFigureTexture, mLeftX, mYAbove, mCenterX, mCenterY, mFieldTexture, mFigureColor, mColumn, mRow = moveToField  # Entpacken des move_to_fields
    
    if not automatic and not illegalMoveTest:  # Die folgenden 3 Methoden dürfen nur bei einem Zug und nicht bei einer Zugüberprüfung des Computers aufgerufen werden
        
        if len(sEPHit) != 0 and sFigure.endswith("pawn"):  # Falls im letzten Zug sich ein Bauer um 2 Felder nach vorne bewegt hat und somit von einem gegnerischen Bauern, der nun neben ihm steht geschlagen werden könnte
            fX, fY, figureTexture, fFieldNumber, fTargetFieldX, fTargetFieldY, fFigureTexture = sEPHit[0]  # Entpacken des 'schlagen en passant' hit
            if fTargetFieldX == mCenterX and fTargetFieldY == mCenterY:  # Falls das 'schlagen en passant' Feld mit den Koordinaten des Feldes, auf das sich die Figur gerade bewegt übereinstimmen
                hittetPawn = chessField[fFieldNumber - 1]
                hPFieldKey, hPFieldNumber, hPFigure, hPFigureTexture, hPLleftX, hPYAbove, hPCenterX, hPCenterY, hPFieldTexture, hPFigureColor, hPColumn, hPRow = hittetPawn  # Entpacken des Feldes mit dem geschlagenen Bauern, da dieser sich nicht auf dem move_to Feld befindet, jedoch trotzdem entfernt werden muss
                chessField[fFieldNumber - 1] = (hPFieldKey, hPFieldNumber, "", "", hPLleftX, hPYAbove, hPCenterX, hPCenterY, hPFieldTexture, "", hPColumn, hPRow)  # Verpacken des entsprechenden Feldes / überschreiben
            sEPHit = []
        
        if sFigure.endswith("pawn"):  # Abfrage, ob sich ein Bauer in diesem Zug um 16 Felder nach vorne bewegt, um diesen dann in die 'Schlagen en passant' Möglichkeit einzuschreiben
            if sFieldNumber - 16 == mFieldNumber:
                schlagenEnPassant = [moves + 1, sFieldNumber - 8, mFieldNumber]
            elif sFieldNumber + 16 == mFieldNumber:
                schlagenEnPassant = [moves + 1, sFieldNumber + 8, mFieldNumber]
        
            if (mColumn == 1 and sFigure.startswith("white")) or (mColumn == 8 and sFigure.startswith("black")):  # Falls ein Bauer sich auf die gegnerische letzte Linie begibt, tauscht er seinen Bauern gegen einen Turm, Pferd, Läufer oder eine Dame ein
                sure = False
                sFigure = ""
                while not sure or sFigure == "":
                    eFigure = int(input("\nBauern ersetzen durch '1' Turm, '2' Pferd, '3' Läufer, '4' Dame: "))  # Leider hier UI-technisch sehr unschön, ging aber leider nicht anders, da TigerJython auf Maus Callbacks anscheinend Fenster erstellen, diese aber nicht mehr mit Inhalt füllen kann
                    if eFigure == 1:
                        output = "Turm"
                        eFigure = "_rook"
                        eFigureTexture = "_2.svg"
                    elif eFigure == 2:
                        output = "Pferd"
                        eFigure = "_knight"
                        eFigureTexture = "_3.svg"
                    elif eFigure == 3:
                        output = "Läufer"
                        eFigure = "_bishop"
                        eFigureTexture = "_4.svg"
                    elif eFigure == 4:
                        output = "Dame"
                        eFigure = "_queen"
                        eFigureTexture = "_1.svg"
                    else:
                        continue  # Hier ein else mit contínue, um den restlichen Schleifendurchlauf, also die 'sure' Zuweisung mit der Frage zu überspringen, da eine Zahl eingegeben wurde, der keine Figur zugeordnet ist

                    sFigure = sFigureColor + eFigure
                    sFigureTexture = dirLocation + "chess" + sFigureColor + eFigureTexture

                    sure = bool(input("\nMöchtest du deinen Bauern wirklich durch eine*n " + output + " ersetzen? \n'True' oder 'False': "))

        if sFigure.endswith("king"):  # Deaktivieren der Rochade-Möglichkeit für die entsprechende Figur, falls sich diese bewegt
            if sFigure.startswith("white"):
                rochadeMoved[0] = True
            if sFigure.startswith("black"):
                rochadeMoved[3] = True
        if sFigure.endswith("rook"):
            if sFigure.startswith("white"):
                if sFigure == "white_1_rook":
                    rochadeMoved[1] = True
                if sFigure == "white_2_rook":
                    rochadeMoved[2] = True
            if sFigure.startswith("black"):
                if sFigure == "black_1_rook":
                    rochadeMoved[4] = True
                if sFigure == "black_2_rook":
                    rochadeMoved[5] = True 
    
    mFigure = "" + sFigure
    mFigureTexture = "" + sFigureTexture
    mFigureColor = "" + sFigureColor
    
    sFigure = ""
    sFigureTexture = ""
    sFigureColor = ""
    
    if len(rochadeFigurePlace) != 0:  # Falls eine Rochade durchgeführt werden könnte
        for t in rochadeFigurePlace:
            clickedField, kFieldNumber, k, kTexture, kColor, kT, rookFieldNumber, rook, rookTexture, rookColor, rookT = t
            if clickedField - 1 == moveToIndex:  # Prüft für jede Rochade, die in diesem Zug hätte durchgeführt werden können, ob sie durchgeführt wurde
                
                kingField = chessField[kFieldNumber - 1]  # weder source noch moveto Feld, da sich König und Turm bei der Rochade auf andere Felder bewegen, weshalb hier diese Felder entpackt werden müssen
                rookField = chessField[rookFieldNumber - 1]  # weder source noch moveto Feld, da sich König und Turm bei der Rochade auf andere Felder bewegen, weshalb hier diese Felder entpackt werden müssen
                
                eKFieldKey, eKFieldNumber, eKFigure, eKFigureTexture, eKLeftX, eKYAbove, eKCenterX, eKCenterY, eKFieldTexture, eKFigureColor, eKColumn, eKRow = kingField
                eRookFieldKey, eRookFieldNumber, eRookFigure, eRookFigureTexture, eRookLeftX, eRookYAbove, eRookCenterX, eRookCenterY, eRookFieldTexture, eRookFigureColor, eRookColumn, eRookRow = rookField
                
                # Einpacken der überschriebenen Felder
                chessField[kFieldNumber - 1] = (eKFieldKey, eKFieldNumber, k, kTexture, eKLeftX, eKYAbove, eKCenterX, eKCenterY, eKFieldTexture, kColor, eKColumn, eKRow)
                chessField[rookFieldNumber - 1] = (eRookFieldKey, eRookFieldNumber, rook, rookTexture, eRookLeftX, eRookYAbove, eRookCenterX, eRookCenterY, eRookFieldTexture, rookColor, eRookColumn, eRookRow)
            
                rochadeFigurePlace = []    
                # Moveto leeren, da sich Turm und König ja bereits auf andere Felder bewegt haben 
                mFigure = ""
                mFigureTexture = ""
                mFigureColor = "" 
    
    chessField[sourceIndex] = (sFieldKey, sFieldNumber, sFigure, sFigureTexture, sLeftX, sYAbove, sCenterX, sCenterY, sFieldTexture, sFigureColor, sColumn, sRow)
    chessField[moveToIndex] = (mFieldKey, mFieldNumber, mFigure, mFigureTexture, mLeftX, mYAbove, mCenterX, mCenterY, mFieldTexture, mFigureColor, mColumn, mRow)
    
    kingGetter()  # Ermitteln der neuen Königsfelder
            
    if illegalMoveTest:
        check = checkCheck()  # Überprüfung auf einen illegalen Zug
        kingGetter() 
        chessField = [] + lastChessField  # Feld mit der erstellten Kopie überschreiben
        rochadeMoved = [] + lastRochadeMoved  # Liste mit den bewegten Rochade-Figuren auf Stand vor dem illegalen Zug zurücksetzen
        return check

    if not automatic and not illegalMoveTest:  # Bei automatischem Programmdurchlauf würden im folgendem weitere automatische Programmdurchläufe entstehen
        
        playerChange()  # Spielerwechsel mit Spieler text, enemy und Zug counter
        moves += 1  
        
        repaint()  # Repainten des Schachfeldes, da sich die Figuren Grafisch bisher noch nicht bewegt haben
    
    if automatic:
        return lastChessField, lastRochadeMoved  # Beim Automatischen durchlaufen die Ursprungsfelder zurückgeben, damit diese nach der automatischen Figur bewegung sich nicht ändern


def decolor():  # Funktion zum Entfärben der gefärbten Felder
    global lastPossibleFields
    global rochadeFigurePlace
    global possibleHitFields
    global selectedField

    lastPossibleFields = []  # Leeren der Listen und danach repainten wichtig, um Feld neu zu "malen"
    rochadeFigurePlace = []
    possibleHitFields = []
    selectedField = []    
    
    repaint()  # Repainten, um alle Färbungen zu entfernen


def checkCheck():  # Funktion zum Überprüfen, ob der König im Schach steht
    global selectedField
    
    Check = False
    runde = 0
    for largeTuple in chessField:  # Für jedes Feld prüfen, ob eine gegnerische Figur auf diesem steht
        selectedField = [(largeTuple[6], largeTuple[7], largeTuple[8], largeTuple[2], largeTuple[1], largeTuple[10], largeTuple[11]), runde]  # Neue Werte des Feldes zuweisen, wichtig da sonst die Überprüfung der Möglichen bewegungen der Figuren nicht funktioniert
        if largeTuple[9] == enemy:
            playerChange()  # Wechseln des Gegners wichtig, da für gegnerische Figuren ermittelt werden soll, ob diese den eigenen König schlagen könnten
            lastPossibleFieldsCheck, possibleHitFieldsCheck = checkFigureType(largeTuple[2])  # Funktionsaufruf mit der Figur, die auf dem aktuell überprüften Feld steht
            playerChange()  # Wichtig, da die Schlagmöglichkeit der gegnerischen Figuren gegen den EIGENEN König getestet werden soll
            for fieldTuple in lastPossibleFieldsCheck:  # Überprüfen für jedes mögliche Feld, das zuvor ermittelt wurde, ob die Figur den gegnerischen König schlagen könnte
                for king in kingFields:
                    if king[3] == activePlayer and (fieldTuple[0] == king[0] and fieldTuple[1] == king[1]):
                        Check = True  # Schach-Situation durch eine Figur erkannt
        runde += 1
    return Check  # Zurückgeben von 'False' oder 'True', je nachdem, ob ein König im Schach steht oder nicht

         
def checkCheckMate():  # Funktion zum Überprüfen, ob ein Spieler Schachmatt ist. (Wird nur aufgerufen, falls ein König im Schach steht)
    global selectedField
    global chessField
    global rochadeMoved
    
    check = True
    runde = 0
    for tTuple in chessField:
        selectedField = [(tTuple[6], tTuple[7], tTuple[8], tTuple[2], tTuple[1], tTuple[10], tTuple[11]), runde]  # Neue Werte des Feldes zuweisen, wichtig da sonst die Überprüfung der Möglichen bewegungen der Figuren nicht funktioniert
        if tTuple[9] == activePlayer:
            lastPossibleFieldsCheckMate, possibleHitFieldsCheckMate = checkFigureType(tTuple[2])
            for possibleField in lastPossibleFieldsCheckMate:
                lRunde = 0
                for largeTuple in chessField:
                    if possibleField[0] == largeTuple[6] and possibleField[1] == largeTuple[7]:
                        lSelectedField = [(largeTuple[6], largeTuple[7], largeTuple[8], largeTuple[2], largeTuple[1], largeTuple[10], largeTuple[11]), runde]  # Neue Werte des Feldes zuweisen, wichtig da sonst die Überprüfung der Möglichen bewegungen der Figuren nicht funktioniert
                        lastChessField, lastRochadeMoved = figureMove(lSelectedField[1], lRunde, True)
                        check = checkCheck()  # Prüfen, ob König noch im Schach steht. Wenn nicht, wird die Funktion abgebrochen
                        chessField = [] + lastChessField  # Zurücksetzen der Figuren auf ihre Ursprungsfelder
                        rochadeMoved = [] + lastRochadeMoved
                        
                        kingGetter()  # Ermitteln, auf welchen Feldern die Könige stehen, da diese möglicherweise bewegt wurden
                        
                    if not check:
                        return check  # Bricht Funktion ab, da es eine Möglichkeit gibt aus dem "Schach" herauszukommen
                    lRunde += 1  
        runde += 1                   
    return check  # Zurückgeben von 'False' oder 'True', je nachdem, ob ein König im Schachmatt ist oder nicht

                          
def checkStalemate():  # Funktion zum Überprüfen auf ein Unentschieden
    stalemate = checkCheckMate()  # Prüfen, ob sich eine Figur bewegen kann, ohne dass der König nach der Bewegung im Schach steht
    
    if not stalemate:  # Falls dies möglich ist, wird geguckt, ob es nur noch 2 Könige gibt, wodurch ebenfalls ein Unentschieden entsteht
        for field in chessField:
            if not (field[2].endswith("king") or field[2] == ""):  # Falls es ein Feld gibt, auf dem etwas anderes als nichts oder ein König steht, wird die Schleife abgebrochen
                break  # Hier sehr nützlich, da nur durch dieses Break das Else-Statement nicht ausgelöst wird
        else:  # Fall das Break nicht einmal aufgerufen wurde, gibt es ein Unentschieden
            stalemate = True
                
    return stalemate  # Zurückgeben von False oder True, je nachdem, ob das Spiel unentschieden ist oder nicht


def playerChange():  # Funktion zum Wechseln der Spieler
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


def kingGetter():  # Funktion zum Ermitteln der Positionen der Könige
    global kingFields
    
    for t in chessField:  # Neu ermitteln des König feldes, falls dieses durch das Programm verändert wurde
        if t[2].endswith("king"):
            if t[2].startswith("black"):
                kingFields[0] = t[6], t[7], t[8], "black"
            elif t[2].startswith("white"):
                kingFields[1] = t[6], t[7], t[8], "white"
                                                                                    
        
def checkFigureType(figure):  # Funktion zum Überprüfen, für welche Figur die nächstmöglichen Felder ausgegeben werden soll
    lastPossibleFields1 = None
    possibleHitFields1 = None

    if figure.endswith("pawn"):
        lastPossibleFields1, possibleHitFields1 = possiblePawnMoves()
    if figure.endswith("knight"):
        lastPossibleFields1, possibleHitFields1 = possibleKnightMoves()
    if figure.endswith("rook"):
        lastPossibleFields1, possibleHitFields1 = possibleRookMoves()
    if figure.endswith("bishop"):
        lastPossibleFields1, possibleHitFields1 = possiblesBishopMoves()
    if figure.endswith("queen"):
        lastPossibleFields1, possibleHitFields1 = possibleQueenMoves()
    if figure.endswith("king"):
        lastPossibleFields1, possibleHitFields1 = possibleKingMoves()
    
    return lastPossibleFields1, possibleHitFields1  # Zurückgeben der möglichen ermittelten Felder


def figureSelect(posX, posY):  # Funktion die auf Aufruf des obigen Maus-callbacks aufgerufen und ausgeführt wird | Das Maus-callback übergibt die angeklickten Koordinaten, mit welchen im Folgenden die angeklickte Position überprüft wird
    global sEPHit
    global rochadeAllowed
    global selectedField
    global lastPossibleFields
    global inputAllowed
    global possibleHitFields
    global rochadeFigurePlace
    
    checkMate = False
    stalemate = False
    index = 0
    if inputAllowed:  # Solange True, bis ein König fällt
        for largeTuple in chessField:  # Durchgehen jedes Feldes bis ein Feld mit den angeklickten Koordinaten übereinstimmt, auf diesem werden dann die weiteren Schritte ausgeführt
            moved = False
            fieldKey, fieldNumber, figure, figureTexture, leftX, yAbove, centerX, centerY, fieldTexture, figureColor, column, row = largeTuple  # Entpacken des Schachfeld Tupels
            if (posX >= leftX and posY >= yAbove) and (posX <= (leftX + 100 * mScreenW) and posY <= (yAbove + 100 * mScreenH)):  # Prüft ob das oben entpackte Schachfeld zu den angeklickten Koordinaten passt
                kingGetter()  # Wichtig, da es sonst zu illegalen Zugmöglichkeiten kommen kann, da die Könige noch auf anderen Feldern registriert sind
                if len(lastPossibleFields) != 0:  # Falls bereits eine Figur ausgewählt wurde und Bewegungsmöglichkeiten für die Figur grün gefärbt wurden wir als erstes geprüft, ob das angeklickte Feld eines derer ist, auf die sich die Figur bewegen kann
                    for possibleField in lastPossibleFields: 
                        if centerX == possibleField[0] and centerY == possibleField[1]:  # Falls die Center mit den Centern des aktuellen Feldes übereinstimmen
                            moved = True
                            figureMove(selectedField[1], index)  # Übergibt an die Move-Funktion das ausgewählte Feld, sowie das Feld, auf welches sich die Figur bewegen soll
                            decolor()  # Entfärben aller Felder sowie leeren der dazugehörigen Listen
                        
                            check = checkCheck()  # Überprüfen, ob der König des aktuellen Spielers im Schach steht
                            if check:  # Aufrufen der Schachmatt-funktion nur, wenn ein König im Schach steht
                                rochadeAllowed = False
                                checkMate = checkCheckMate()
                            if not check:
                                rochadeAllowed = True
                                stalemate = checkStalemate()
                            
                            if checkMate:
                                playerChange()  # Wechseln des Gegners, da für seine Figuren die möglichen Züge ermittelt werden sollen, und seine Figuren die Figuren des aktiven Spielers schlagen könnten
                                
                                inputAllowed = False  # Weiteren Input nach Spielende verhindern
                                pygame.display.set_caption("SPIELENDE   |   " + activePlayerText + " hat das Spiel gewonnen")  # Titel am Spielende aktualisieren
                                print("\n" + activePlayerText + " hat das Spiel gewonnen!")  # , title="Schachmatt   |   " + activePlayerText + " gewinnt das Spiel")
                                
                            if not checkMate and check:
                                print("\n" + activePlayerText + ", du stehst im Schach \nSchütze deinen Koenig!")  # , title="SCHACH")  # Ausgabe 'Schach'
                                
                            if stalemate:
                                inputAllowed = False  # Weiteren Input nach Spielende verhindern
                                pygame.display.set_caption("SPIELENDE   |   Unentschieden")  # Titel am Spielende aktualisieren
                                print("\nUnentschieden!")  # , title="Patt   |   Niemand gewinnt das Spiel")
                                
                            selectedField = []
                            break
                if moved:
                    break  # Keine andere Möglichkeit gefunden | Schleife muss im if Fall sofort abgebrochen werden, da es sonst zu verheerenden Fehlern kommen kann
                if figure != "" and figureColor == activePlayer:  # Falls das angeklickte Feld nicht leer und die Figurenfarbe mit dem aktiven Spieler übereinstimmt
                    decolor()
                    selectedField.append((centerX, centerY, fieldTexture, figure, fieldNumber, column, row))  # Nach leeren und entfärben wird hier die neu ausgewählte Figur aufgenommen
                    selectedField.append(index)  # Speichern des Indexes des ausgewählten Feldes | Wichtig für die move Funktion
                    pygame.draw.rect(pygameWindow, (173, 216, 230), (centerX - 50 * mScreenW, centerY - 50 * mScreenH, 100 * mScreenW, 100 * mScreenH))
                    figureRepaint()

                    lastPossibleFields, possibleHitFields = checkFigureType(figure)  # Funktionsaufrufe je nach ausgewählter Figur
                    newPossibleMoves = []
                    for largeT in lastPossibleFields:  # Für jedes possible Field wird geguckt, ob der Zug legal wäre, wenn nicht, wird das Feld nicht zur neuen Liste hinzugefügt, die die Alte dann ersetzt
                        selectedCopy = [] + selectedField  # Copy von selectedField, da dieses sich ändert und sonst nichts mehr funktioniert
                        figureHitCopy = [] + possibleHitFields
                        rochadeCopy = [] + rochadeFigurePlace
                        
                        check = figureMove(selectedField[1], largeT[3] - 1, False, True)  # Hier wird die legalität des möglichen Zuges überprüft
                        
                        selectedField = [] + selectedCopy  # selectedField mit der erzeugten Kopie überschreiben
                        possibleHitFields = [] + figureHitCopy
                        rochadeFigurePlace = [] + rochadeCopy
                        
                        if not check:  # Falls der mögliche Zug nicht illegal ist, wird er zu den neuen möglichen Zügen hinzugefügt
                            newPossibleMoves.append(largeT)
                    lastPossibleFields = [] + newPossibleMoves  # Überschreiben der Liste mit den möglichen Feldern, mit den möglichen legalen Feldern
                    
                    newHitFields = []
                    for f in possibleHitFields:  # Überprüfen, ob eine Schlagmöglichkeit soeben als illegal erkannt wurde, falls dies der Fall ist MUSS dieses Feld aus figure_hit_field entfernt sein
                        for i in lastPossibleFields:
                            if f == i:  # Falls das Hit-field noch in den möglichen ist, wird es der neuen Liste hinzugefügt
                                newHitFields.append(f)
                    possibleHitFields = [] + newHitFields  # Überschreiben der alten möglichen Schläge mit den möglichen legalen Schlägen
                    
                    newRochadeFields = []
                    for f in rochadeFigurePlace:
                        for i in lastPossibleFields:
                            if f[0] == i[3]:  # Wenn die Feldnummern übereinstimmen
                                newRochadeFields.append(f)
                    rochadeFigurePlace = [] + newRochadeFields

                    for f in lastPossibleFields:  # Färben der möglichen Züge
                        fX, fY, fieldTexture, fNumber = f
                        pygame.draw.rect(pygameWindow, (63, 255, 0), (fX - 50 * mScreenW, fY - 50 * mScreenH, 100 * mScreenW, 100 * mScreenH))

                    for f in rochadeFigurePlace:  # Färben der Felder für König und Turm bei einer Rochade
                        for t in f:
                            if type(t) is tuple:
                                tX, tY, fieldTexture = t
                                pygame.draw.rect(pygameWindow, (192, 0, 255), (tX - 50 * mScreenW, tY - 50 * mScreenH, 100 * mScreenW, 100 * mScreenH))

                    for f in possibleHitFields:
                        fX, fY, fieldTexture, fNumber = f
                        pygame.draw.rect(pygameWindow, (250, 0, 0), (fX - 50 * mScreenW, fY - 50 * mScreenH, 100 * mScreenW, 100 * mScreenH))

                    figureRepaint()

            index += 1  # Nach einem Schleifendurchlauf wird der Index um 1 erhöht


def startGame(bot):
    import botChess as BC
    global pygameWindow
    global gameStart
    global inputAllowed

    pygame.init()

    pygameWindow = pygame.display.set_mode((800 * mScreenW, 800 * mScreenH))  # Feste Fenstergröße, in die das Schachfeld perfekt hinein passt
    gameStart = time.time()  # Zeit des Spielstarts speichern
    repaint()  # Erstes Zeichnen des Spielfeldes
    if bot:
        while inputAllowed:
            if activePlayer == "white":
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        figureSelect(x, y)
                    if event.type == pygame.QUIT:
                        inputAllowed = False
            else:
                BC.getMove()

    else:
        while inputAllowed:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    figureSelect(x, y)
                if event.type == pygame.QUIT:
                    inputAllowed = False

    pygame.quit()
