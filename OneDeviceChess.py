# Christian Tolger
# 15.9.2023
# v1.2
# Full Comment Version

import gturtle as gt
import os
import Gamemode
import Values

screenX = Values.screenW
screenY = Values.screenH

mX = screenX / 800
mY = screenY / 800 # Teilen durch 800, da das Schachfeld in einem 800 x 800 Feld eingerichtet ist

file_dir = os.path.dirname(__file__) # Speichern des Verzeichnisses, in dem das Programm läuft in der Variable file_dir, damit die Figurtexturen im Ordner in diesem Verzeichniss gefunden werden können 
chess_figures = "chessfigures/" # Name des Ordners indem sich die Texturen für die Schachfiguren befinden
chess_figure_file = os.path.join(file_dir, chess_figures) # Anfügen des Ordnernamen an das Verzeichniss

### Schachfeld ###
                #     0            1          2           3           4        5       6        7        8         9          10             11         12     13
chess_field = [ # field_key, field_number, figure, figure_texture, left_x, y_above, right_x, y_down, center_x, center_y, field_texture, figure_color, collum, row
    ("8a", 1, "black_1_rock", chess_figure_file + "chessblack_2.png", -400 * mX, 400 * mY, -300 * mX, 300 * mY, -350 * mX, 350 * mY, "white", "black", 1, 1), ("8b", 2, "black_knight", chess_figure_file + "chessblack_3.png", -300 * mX, 400 * mY, -200 * mX, 300 * mY, -250 * mX, 350 * mY, "gray", "black", 1, 2), ("8c", 3, "black_bishop", chess_figure_file + "chessblack_4.png", -200 * mX, 400 * mY, -100 * mX, 300 * mY, -150 * mX, 350 * mY, "white", "black", 1, 3), ("8d", 4, "black_queen", chess_figure_file + "chessblack_1.png", -100 * mX, 400 * mY, 0 * mX, 300 * mY, -50 * mX, 350 * mY, "gray", "black", 1, 4), ("8e", 5, "black_king", chess_figure_file + "chessblack_0.png", 0 * mX, 400 * mY, 100 * mX, 300 * mY, 50 * mX, 350 * mY, "white", "black", 1, 5), ("8f", 6, "black_bishop", chess_figure_file + "chessblack_4.png", 100 * mX, 400 * mY, 200 * mX, 300 * mY, 150 * mX, 350 * mY, "gray", "black", 1, 6), ("8g", 7, "black_knight", chess_figure_file + "chessblack_3.png", 200 * mX, 400 * mY, 300 * mX, 300 * mY, 250 * mX, 350 * mY, "white", "black", 1, 7), ("8h", 8, "black_2_rock", chess_figure_file + "chessblack_2.png", 300 * mX, 400 * mY, 400 * mX, 300 * mY, 350 * mX, 350 * mY, "gray", "black", 1, 8),
    ("7a", 9, "black_pawn", chess_figure_file + "chessblack_5.png", -400 * mX, 300 * mY, -300 * mX, 200 * mY, -350 * mX, 250 * mY, "gray", "black", 2, 1), ("7b", 10, "black_pawn", chess_figure_file + "chessblack_5.png", -300 * mX, 300 * mY, -200 * mX, 200 * mY, -250 * mX, 250 * mY, "white", "black", 2, 2), ("7c", 11, "black_pawn", chess_figure_file + "chessblack_5.png", -200 * mX, 300 * mY, -100 * mX, 200 * mY, -150 * mX, 250 * mY, "gray", "black", 2, 3), ("7d", 12, "black_pawn", chess_figure_file + "chessblack_5.png", -100 * mX, 300 * mY, 0 * mX, 200 * mY, -50 * mX, 250 * mY, "white", "black", 2, 4), ("7e", 13, "black_pawn", chess_figure_file + "chessblack_5.png", 0 * mX, 300 * mY, 100 * mX, 200 * mY, 50 * mX, 250 * mY, "gray", "black", 2, 5), ("7f", 14, "black_pawn", chess_figure_file + "chessblack_5.png", 100 * mX, 300 * mY, 200 * mX, 200 * mY, 150 * mX, 250 * mY, "white", "black", 2, 6), ("7g", 15, "black_pawn", chess_figure_file + "chessblack_5.png", 200 * mX, 300 * mY, 300 * mX, 200 * mY, 250 * mX, 250 * mY, "gray", "black", 2, 7), ("7h", 16, "black_pawn", chess_figure_file + "chessblack_5.png", 300 * mX, 300 * mY, 400 * mX, 200 * mY, 350 * mX, 250 * mY, "white", "black", 2, 8),
    ("6a", 17, "", "", -400 * mX, 200 * mY, -300 * mX, 100 * mY, -350 * mX, 150 * mY, "white", "", 3, 1), ("6b", 18, "", "", -300 * mX, 200 * mY, -200 * mX, 100 * mY, -250 * mX, 150 * mY, "gray", "", 3, 2), ("6c", 19, "", "", -200 * mX, 200 * mY, -100 * mX, 100 * mY, -150 * mX, 150 * mY, "white", "", 3, 3), ("6d", 20, "", "", -100 * mX, 200 * mY, 0 * mX, 100 * mY, -50 * mX, 150 * mY, "gray", "", 3, 4), ("6e", 21, "", "", 0 * mX, 200 * mY, 100 * mX, 100 * mY, 50 * mX, 150 * mY, "white", "", 3, 5), ("6f", 22, "", "", 100 * mX, 200 * mY, 200 * mX, 100 * mY, 150 * mX, 150 * mY, "gray", "", 3, 6), ("6g", 23, "", "", 200 * mX, 200 * mY, 300 * mX, 100 * mY, 250 * mX, 150 * mY, "white", "", 3, 7), ("6h", 24, "", "", 300 * mX, 200 * mY, 400 * mX, 100 * mY, 350 * mX, 150 * mY, "gray", "", 3, 8), 
    ("5a", 25, "", "", -400 * mX, 100 * mY, -300 * mX, 0 * mY, -350 * mX, 50 * mY, "gray", "", 4, 1), ("5b", 26, "", "", -300 * mX, 100 * mY, -200 * mX, 0 * mY, -250 * mX, 50 * mY, "white", "", 4, 2), ("5c", 27, "", "", -200 * mX, 100 * mY, -100 * mX, 0 * mY, -150 * mX, 50 * mY, "gray", "", 4, 3), ("5d", 28, "", "", -100 * mX, 100 * mY, 0 * mX, 0 * mY, -50 * mX, 50 * mY, "white", "", 4, 4), ("5e", 29, "", "", 0 * mX, 100 * mY, 100 * mX, 0 * mY, 50 * mX, 50 * mY, "gray", "", 4, 5), ("5f", 30, "", "", 100 * mX, 100 * mY, 200 * mX, 0 * mY, 150 * mX, 50 * mY, "white", "", 4, 6), ("5g", 31, "", "", 200 * mX, 100 * mY, 300 * mX, 0 * mY, 250 * mX, 50 * mY, "gray", "", 4, 7), ("5h", 32, "", "", 300 * mX, 100 * mY, 400 * mX, 0 * mY, 350 * mX, 50 * mY, "white", "", 4, 8), 
    ("4a", 33, "", "", -400 * mX, 0 * mY, -300 * mX, -100 * mY, -350 * mX, -50 * mY, "white", "", 5, 1), ("4b", 34, "", "", -300 * mX, 0 * mY, -200 * mX, -100 * mY, -250 * mX, -50 * mY, "gray", "", 5, 2), ("4c", 35, "", "", -200 * mX, 0 * mY, -100 * mX, -100 * mY, -150 * mX, -50 * mY, "white", "", 5, 3), ("4d", 36, "", "", -100 * mX, 0 * mY, 0 * mX, -100 * mY, -50 * mX, -50 * mY, "gray", "", 5, 4), ("4e", 37, "", "", 0 * mX, 0 * mY, 100 * mX, -100 * mY, 50 * mX, -50 * mY, "white", "", 5, 5), ("4f", 38, "", "", 100 * mX, 0 * mY, 200 * mX, -100 * mY, 150 * mX, -50 * mY, "gray", "", 5, 6), ("4g", 39, "", "", 200 * mX, 0 * mY, 300 * mX, -100 * mY, 250 * mX, -50 * mY, "white", "", 5, 7), ("4h", 40, "", "", 300 * mX, 0 * mY, 400 * mX, -100 * mY, 350 * mX, -50 * mY, "gray", "", 5, 8),
    ("3a", 41, "", "", -400 * mX, -100 * mY, -300 * mX, -200 * mY, -350 * mX, -150 * mY, "gray", "", 6, 1), ("3b", 42, "", "", -300 * mX, -100 * mY, -200 * mX, -200 * mY, -250 * mX, -150 * mY, "white", "", 6, 2), ("3c", 43, "", "", -200 * mX, -100 * mY, -100 * mX, -200 * mY, -150 * mX, -150 * mY, "gray", "", 6, 3), ("3d", 44, "", "", -100 * mX, -100 * mY, 0 * mX, -200 * mY, -50 * mX, -150 * mY, "white", "", 6, 4), ("3e", 45, "", "", 0 * mX, -100 * mY, 100 * mX, -200 * mY, 50 * mX, -150 * mY, "gray", "", 6, 5), ("3f", 46, "", "", 100 * mX, -100 * mY, 200 * mX, -200 * mY, 150 * mX, -150 * mY, "white", "", 6, 6), ("3g", 47, "", "", 200 * mX, -100 * mY, 300 * mX, -200 * mY, 250 * mX, -150 * mY, "gray", "", 6, 7), ("3h", 48, "", "", 300 * mX, -100 * mY, 400 * mX, -200 * mY, 350 * mX, -150 * mY, "white", "", 6, 8),
    ("2a", 49, "white_pawn", chess_figure_file + "chesswhite_5.png", -400 * mX, -200 * mY, -300 * mX, -300 * mY, -350 * mX, -250 * mY, "white", "white", 7, 1), ("2b", 50, "white_pawn", chess_figure_file + "chesswhite_5.png", -300 * mX, -200 * mY, -200 * mX, -300 * mY, -250 * mX, -250 * mY, "gray", "white", 7, 2), ("2c", 51, "white_pawn", chess_figure_file + "chesswhite_5.png", -200 * mX, -200 * mY, -100 * mX, -300 * mY, -150 * mX, -250 * mY, "white", "white", 7, 3), ("2d", 52, "white_pawn", chess_figure_file + "chesswhite_5.png", -100 * mX, -200 * mY, 0 * mX, -300 * mY, -50 * mX, -250 * mY, "gray", "white", 7, 4), ("2e", 53, "white_pawn", chess_figure_file + "chesswhite_5.png", 0 * mX, -200 * mY, 100 * mX, -300 * mY, 50 * mX, -250 * mY, "white", "white", 7, 5), ("2f", 54, "white_pawn", chess_figure_file + "chesswhite_5.png", 100 * mX, -200 * mY, 200 * mX, -300 * mY, 150 * mX, -250 * mY, "gray", "white", 7, 6), ("2g", 55, "white_pawn", chess_figure_file + "chesswhite_5.png", 200 * mX, -200 * mY, 300 * mX, -300 * mY, 250 * mX, -250 * mY, "white", "white", 7, 7), ("2h", 56, "white_pawn", chess_figure_file + "chesswhite_5.png", 300 * mX, -200 * mY, 400 * mX, -300 * mY, 350 * mX, -250 * mY, "gray", "white", 7, 8),
    ("1a", 57, "white_1_rock", chess_figure_file + "chesswhite_2.png", -400 * mX, -300 * mY, -300 * mX, -400 * mY, -350 * mX, -350 * mY, "gray", "white", 8, 1), ("1b", 58, "white_knight", chess_figure_file + "chesswhite_3.png", -300 * mX, -300 * mY, -200 * mX, -400 * mY, -250 * mX, -350 * mY, "white", "white", 8, 2), ("1c", 59, "white_bishop", chess_figure_file + "chesswhite_4.png", -200 * mX, -300 * mY, -100 * mX, -400 * mY, -150 * mX, -350 * mY, "gray", "white", 8, 3), ("1d", 60, "white_queen", chess_figure_file + "chesswhite_1.png", -100 * mX, -300 * mY, 0 * mX, -400 * mY, -50 * mX, -350 * mY, "white", "white", 8, 4), ("1e", 61, "white_king", chess_figure_file + "chesswhite_0.png", 0 * mX, -300 * mY, 100 * mX, -400 * mY, 50 * mX, -350 * mY, "gray", "white", 8, 5), ("1f", 62, "white_bishop", chess_figure_file + "chesswhite_4.png", 100 * mX, -300 * mY, 200 * mX, -400 * mY, 150 * mX, -350 * mY, "white", "white", 8, 6), ("1g", 63, "white_knight", chess_figure_file + "chesswhite_3.png", 200 * mX, -300 * mY, 300 * mX, -400 * mY, 250 * mX, -350 * mY, "gray", "white", 8, 7), ("1h", 64, "white_2_rock", chess_figure_file + "chesswhite_2.png", 300 * mX, -300 * mY, 400 * mX, -400 * mY, 350 * mX, -350 * mY, "white", "white", 8, 8)
]

king_fields = [(50 * mX, 350 * mY, "white", "black"), (50 * mX, -350 * mY, "gray", "white")] # center_x, center_y, field_color, figure_color

selected_field = []
rochade_figure_place = []
last_possible_fields = []
figure_hit_fields = []
schlagen_en_passant = [0, 0, 0]
s_e_p_hit = []
rochade_moves = [False, False, False, False, False, False] # w_king, w_1_rock, w_2_rock, b_king, b_1_rock, b_2_rock | Falls bereits bewegt -> entsprechender Wert == True
active_player = "white"
aktiver_spieler_text = "Weiss"
enemy = "black"
input_allowed = True
moves = 0

def repaint(): # Neu zeichen des Schachfeldes nach einer Bewegung --->>> Einfachste Möglichkeit Figurtexturen wieder vom Feld zu entfernen
    gt.clean("white") # Komplettes Fenster neu färben, da sonst Grafikfehler entstehen
    
    for i in range(-400, 401, 100): # Spaltenstriche, damit das colorieren der Felder korrekt funktioniert
        gt.setPos(i * mX, 400 * mY)
        gt.moveTo(i * mX, -400 * mY)
    
    for i in range(-400, 401, 100): # Zeilenstirche, damit das colorieren der Felder korrekt funktioniert
        gt.setPos(-400 * mX, i * mY)
        gt.moveTo(400 * mX, i * mY)
    
    gt.heading(0) # Ausrichten der Blickrichtung der Turtle nach oben, damit die Figuren stehen und nicht liegen oder auf dem Kopf stehen
    for large_tupel in chess_field: # Für jedes Schachfeld die Mittelpunkt Koordinaten, die Feldfarbe und die sích auf dem Feld befindliche Figur entnehmen und im Folgendem aufs Spielfeld zeichnen
        center_x = large_tupel[8]
        center_y = large_tupel[9]
        field_texture = large_tupel[10]
        
        gt.setPos(center_x, center_y)
        gt.setFillColor(field_texture)# Feld in entsprechender Farbe färben
        gt.fill()
        
        figure_texture = large_tupel[3]
        gt.drawImage(figure_texture) # Textur der Schachfigur aufs Spielfeld bringen
    
    elapsed_time = gt.time.time() - game_start
    timer = elapsed_time // 60

    gt.setTitle("Aktiver Spieler : " + aktiver_spieler_text + "  |    " + str(moves) + "  :  Zuege insgesamt --- Spielzeit :  " + str(int(timer)) + " min") # Nur in Minuten, da Timer nicht fortlaufend, sondern nur bei Aktionen aktualisiert wird

    
gt.setPlaygroundSize(int(800 * mX), int(800 * mY)) # Feste Fenstergröße, in die das Schachfeld perfekt hinein passt
gt.makeTurtle()
gt.hideTurtle() # Zeichengeschwindigkeit auf instant speeed setzen und Turtle verstecken
gt.setPenColor("black")
gt.setPenWidth(3)
    
game_start = gt.time.time() # Zeit des Spielstarts speichern
repaint() # Erstes Zeichnen des Spielfeldes
 
# Programmende! Ab hier reagiert das Programm nur noch auf MausCallBacks           
            
def possible_pawn_moves(): # Funktion die alle möglichen Bewegungen für den ausgewählten Bauern zurückgibt
    global s_e_p_hit
    
    repaint_x, repaint_y, repaint_texture, r_figure, r_field_number, r_collum, r_row = selected_field[0] # Entpacken des ausgewählten Feldes
    possible_moves = []
    figure_hit_fields = []
    
    indexes = [-16, -9, -8, -7, 7, 8, 9, 16] # Alle Indexe, um die sich ein Bauer bewegen kann | Negativ: Weiß Positiv: Schwarz
    for index in indexes: # Durchlaufen aller Indexe
        s_e_p_color = False # Falls True wird das Feld hinter dem schlagbaren Bauern rot gefärbt
        if (r_figure.startswith("black") and index > 0) or (r_figure.startswith("white") and index < 0): # Überspringen der Indexe, um die sich ein schwarzer bzw. weißer Bauer nicht bewegen kann
            if r_field_number + index - 1 < 64 and r_field_number + index - 1 > -1: # Überprüfen des Indexes, sodass keine Index außerhalb der Listenlänge abgefragt wird und es einen Fehler gibt
                field = chess_field[r_field_number + index - 1]
                if (r_row == 1 and field[13] == 8) or (r_row == 8 and field[13] == 1): # Abfrage, ob der Bauer am Spielfeldrand heraus laufen würde
                    continue
                if field[11] == "" or field[11] == enemy: # Falls das zu überprüfende Feld leer ist oder ein Gegner auf diesem steht
                    if not (schlagen_en_passant[0] == moves and field[1] == schlagen_en_passant[1]): # Implimentierung der Regel 'Schlagen en passant' hier falsch falls diese eine Anwendung finden würde
                        if (abs(index) == 7 or abs(index) == 9) and field[11] != enemy:
                            continue
                    elif abs(index) == 7 or abs(index) == 9:
                        s_e_p_field = chess_field[schlagen_en_passant[2] - 1] # Feld auf dem der 'Schlagen en passant' Bauer steht einlesen
                        s_e_p_color = True
                        s_e_p_hit = [(s_e_p_field[8], s_e_p_field[9], s_e_p_field[10], s_e_p_field[1], field[8], field[9], field[10])] # Speichern der Felder, damit diese korrekt gefärbt und falls der Bauer den anderen en passant schlägt dieser entfernt wird
                    if abs(index) == 8 and field[11] != "": # Bauern können nur nach vorne laufen, wenn das Feld vor ihnen Frei ist
                        continue
                    if abs(index) == 16 and not ((r_collum == 2 and r_figure == "black_pawn") or (r_collum == 7 and r_figure == "white_pawn")): # Falls der abzufragende Index 16 ist und es sich nicht um einen Bauern handelt, der noch auf seinem Startfeld steht wird mit dem nächsten Schleifendurchlauf fortgefahren
                        continue
                    if abs(index) == 16: # Prüft ob beide Felder (das über welches der Bauer läuft und das auf welchem er landet) frei sind
                        r_field = chess_field[r_field_number + (index // 2) - 1]
                        if r_field[11] != "" or field[11] != "":
                            continue
    
                    possible_moves.append((field[8], field[9], field[10], field[1]))
                    
                    if field[11] == enemy or s_e_p_color:
                        figure_hit_fields.append((field[8], field[9], field[10], field[1])) # Liste mit Feldern die Rot gefärbt werden sollen -> Eine Figur steht auf diesen

    return possible_moves, figure_hit_fields # Zurückgeben aller ermittelten möglichen Bewegungen


def possible_knight_moves(): # Funktion, die alle möglichen Bewegungen für ein ausgewähltes Pferd zurück gibt
    
    repaint_x, repaint_y, repaint_texture, r_figure, r_field_number, r_collum, r_row = selected_field[0] # Entpacken des ausgewählten Feldes
    possible_moves = []
    figure_hit_fields = []
    
    indexes = [-17, -15, -10, -6, 6, 10, 15, 17] # Alle möglichen Pferdbewegungen, falls die entsprechenden Felder frei oder von Gegnern besetzt sind
    for index in indexes: # Durchlaufen jedes indexes und überprüfen, ob das entsprechende Feld frei oder von einem Gegner besetzt ist
        if r_field_number + index - 1 < 64 and r_field_number + index - 1 > -1: # Verhindern eines Index out of Range Errors, indem überprüft wird, ob der Azufragende Index innerhalb der Range liegt
            field = chess_field[r_field_number + index - 1]
            if ((r_row == 8 or r_row == 7) and field[13] < 5) or ((r_row == 1 or r_row == 2) and field[13] > 4): # Verhindern, dass Pferde über die Seitenränder des Schachfeldes springen können 
                continue
            if field[11] == "" or field[11] == enemy:
                possible_moves.append((field[8], field[9], field[10], field[1]))
                if field[11] == enemy:
                    figure_hit_fields.append((field[8], field[9], field[10], field[1])) # Liste mit Feldern die Rot gefärbt werden sollen -> Eine Figur steht auf diesen

    return possible_moves, figure_hit_fields # Zurückgeben aller möglichen Pferdbewegungen


def possible_rock_moves(): # Funktion zum ermitteln aller möglichen Turmzüge

    repaint_x, repaint_y, repaint_texture, r_figure, r_field_number, r_collum, r_row = selected_field[0] # Entpacken des ausgewählten Feldes
    possible_moves = []
    figure_hit_fields = []
        
    t_list = [(r_collum, 8, 0, -1), (r_collum, 8, 9, 1), (r_row, 1, 0, -1), (r_row, 1, 9, 1)] #[0]: Spalte oder Zeile [1]: Felder, die im index vor / zurück gegangen werden müssen, um das nächste Feld in der Reihe oder Spalte zu ermittlen [2]: Ende, falls die Zeile oder Spalte vor Ende überprüft wird bricht die Schleife nach dieser ab [3]: Zum negieren der Laufrichtung und des Indexes
    for t in t_list:
        line, number, end, step = t # Entpacken der tuple aus t_list          
        m = 0 # wird mit dem Index multipliziert pro Durchlauf, damit immer das nächste Feld in die entsprechende Richtung abgefragt wird
        for i in range(line + step, end, step):
            m += 1
            index = number * m * step # Ermitteln des Indexes, der abgefragt werden soll
            field = chess_field[r_field_number + index - 1]
            if field[11] == "" or field[11] == enemy:
                possible_moves.append((field[8], field[9], field[10], field[1]))
            if field[11] != "": # Schleifenabbruch bei Gegner oder bei eigner Figur | Bei Gegner wird dieser zuvor noch ermittelt und in die möglichen Züge aufgenommen
                figure_hit_fields.append((field[8], field[9], field[10], field[1])) # Liste mit Feldern die Rot gefärbt werden sollen -> Eine Figur steht auf diesen
                break
    
    return possible_moves, figure_hit_fields # Zurückgeben aller möglichen Bewegungen für den ausgewählten Turm


def possibles_bishop_moves(): # Funktion zum Ermitteln aller möglichen Läuferbewegungen 

    repaint_x, repaint_y, repaint_texture, r_figure, r_field_number, r_collum, r_row = selected_field[0] # Entpacken des ausgewählten Feldes
    possible_moves = []
    figure_hit_fields = []
    
    t_list = [(-9, 0, -1, 1), (-7, 0, -1, 2), (7, 9, 1, 3), (9, 9, 1, 4)] # [0]: Feldindex, auf das sich bewegt werden soll, [1]: Reihenende, [2]: Schritt, [3]: Runde (Nummer des Tuples) 
    for t in t_list:
        line = 0 + r_collum
        number, end, step, runde = t # Entpacken des aktuellen Tuples aus t_list
        m = 0 # wird mit dem Index multipliziert pro Durchlauf, damit immer das nächste Feld in die entsprechende Richtung abgefragt wird
        for i in range(line + step, end, step):
            m += 1
            index = number * m # Ermitteln des Indexes, der abgefragt werden soll
            if r_field_number + index - 1 < 64 and r_field_number + index - 1 > -1: # Falls der Index außerhalb des Schachfeldes liegen würde, wird hier abgebrochen, damit ein Error verhindert wird
                field = chess_field[r_field_number + index - 1]
                if (field[13] == 1  and runde % 2 == 0.0) or (field[13] == 8 and runde % 2 != 0.0): # Falls das ermittelte Feld den entsprechenden Wert hat und der Läufer sich entgegen der Richtung bewegt, also über den Rand gelaufen ist, bricht die Schleife ab, und die Bewegung über den Rand wird nicht mehr erfasst
                    break 
                if (field[11] == "" or field[11] == enemy):
                    possible_moves.append((field[8], field[9], field[10], field[1]))
                if field[11] != "":
                    figure_hit_fields.append((field[8], field[9], field[10], field[1])) # Liste mit Feldern die Rot gefärbt werden sollen -> Eine Figur steht auf diesen
                    break
    
    return possible_moves, figure_hit_fields # Zurückgeben aller ermittelten möglichen Läuferbewegungen 
        
        
# Bedient sich an der Läufer- und Turmfunktion, da sich die Dame wie eine Kombination aus beiden bewegt
def possible_queen_moves(): # Funktion zum ermitteln aller möglichen Bewegungen für die Dame
    rock, f_rock = possible_rock_moves()
    bishop, f_bishop = possibles_bishop_moves()
    
    possible_moves = rock + bishop # Zusammen führen der möglichen Felder aus beiden Klassen, da sich nicht Turm oder Läufer, sondern Turm und Läufer ist
    figure_hit_fields = f_rock + f_bishop
    
    return possible_moves, figure_hit_fields # Zurückgeben aller möglichen Zugfelder

            
def possible_king_moves(): # Funktion zum ermitteln aller möglichen Bewegungen für den König
    global rochade_figure_place
    
    repaint_x, repaint_y, repaint_texture, r_figure, r_field_number, r_collum, r_row = selected_field[0] # Entpacken des ausgewählten Feldes
    possible_moves = []
        
    indexes = [-9, -8, -7, -1, 1, 7, 8, 9] # Alle möglichen Indexe, um die sich der König bewegen kann (rochieren hierbei ausgeschlossen folgt weiter unten in der Funktion)
    for index in indexes:
        if r_field_number + index - 1 < 64 and r_field_number + index - 1 > -1: # Falls der Index außerhalb des Schachfeldes liegen würde, wird hier abgebrochen, damit ein Error verhindert wird
            field = chess_field[r_field_number + index - 1]
            if (field[13] == 1  and r_row == 8) or (field[13] == 8 and r_row == 1): # Falls der König vor der Bewegung auf der anderen Seite des Schachfeldes war, wird hier in den nächsten Durchlauf gesprungen und der Wert nicht mehr zu den möglichen Zügen hinzugefügt
                continue
            if field[11] == "" or field[11] == enemy:
                possible_moves.append((field[8], field[9], field[10], field[1]))
                
            if field[11] == enemy:
                figure_hit_fields.append((field[8], field[9], field[10], field[1])) # Liste mit Feldern die Rot gefärbt werden sollen -> Eine Figur steht auf diesen
            
    roch_f_color = r_figure.rstrip("king").rstrip("_") # Festschreiben der Farbe des Königs in einer Variablen
    odd_numbers = [-2, -1, 1, -4] # [0]: Bewegung des Königs bei einer Rochade [1]: Bewegung des Turms bei einer Rochade [2]: ID des Turms [3]: Index, bei dem die Überprüfung nach leeren Feldern aufhört  
    even_numbers = [2, 1, 2, 3]   # [0]: Bewegung des Königs bei einer Rochade [1]: Bewegung des Turms bei einer Rochade [2]: ID des Turms [3]: Index, bei dem die Überprüfung nach leeren Feldern aufhört
    odd = [-1, -2, -3, -4] # Indexe große Rochade
    even = [1, 2, 3] # Indexe kleine Rochade
    
    for i in [(0, "white"), (3, "black")]: # [0]: Index in rochade_moves zum Überprüfen, ob sich der König bereits bewegt hat [1]: Farbe des zu überprüfenden Königs
        if (not rochade_moves[i[0]]) and r_figure.startswith(i[1]): # Falls sich der Köing noch nicht bewegt hat und die Farbe des Königs mit der Farbe des ausgewählten Königs übereinstimmt
            r = 0
            for j in [1, 2, 4, 5]: # Indexe in rochade_moves zum Überprüfen, ob sich die Türme, mit denen rochiert werden soll bereits bewegt haben
                r += 1
                if r % 2 == 0.0:
                    e_o_index = [] + even_numbers
                    even_or_odd = [] + even
                else:
                    e_o_index = [] + odd_numbers
                    even_or_odd = [] + odd
                    
                if (i[0] == 0 and (not rochade_moves[j]) and j < 3) or (i[0] == 3 and (not rochade_moves[j]) and j > 3): # Falls sich der zu überprüfende Turm sich noch nicht bewegt hat 
                        for index in even_or_odd:
                            if r_field_number + index - 1 < 64 and r_field_number + index - 1 > -1: # Falls der Index außerhalb des Schachfeldes liegen würde, wird hier abgebrochen, damit ein Error verhindert wird
                                field = chess_field[r_field_number + index - 1]
                                if index == e_o_index[3] and field[2] == roch_f_color + "_" + str(e_o_index[2]) + "_rock": # Falls der letzte Index für die Rochade erreicht wurde und auf dem letzten Feld der Turm steht, der zu beginn des Spiels auf dem entsprechenden Feld stand
                                    king_field = chess_field[r_field_number + e_o_index[0] - 1] # Feld auf das der König bei der entsprechenden Rochade zieht
                                    rock_field = chess_field[r_field_number + e_o_index[1] - 1] # Feld auf das der Turm bei der entsprechenden Rochade zieht
                                    rochade_figure_place.append((field[1], king_field[1], roch_f_color + "_king", chess_figure_file + "chess" + roch_f_color + "_0.png", roch_f_color, (king_field[8], king_field[9], king_field[10]), rock_field[1], roch_f_color + "_" + str(e_o_index[2]) + "_rock", chess_figure_file + "chess" + roch_f_color +  "_2.png", roch_f_color, (rock_field[8], rock_field[9], rock_field[10])))                                    
                                    possible_moves.append((field[8], field[9], field[10], field[1]))
                                if field[11] != "":
                                    break 

    return possible_moves, figure_hit_fields # Zurückgeben aller möglichen Bewegungen
                                        
                                                                                                    
def figure_move(s_index, m_index, automatic = False, illegal_move_test = False): # Funktion, die Figuren bewegt / die Schachfeldliste an den bestimmten Stellen überschreibt
    global schlagen_en_passant
    global s_e_p_hit
    global chess_field
    global moves
    global rochade_moves
    global rochade_figure_place
    
    rochade = False
    
    last_chess_field = [] + chess_field # Für den Durchlauf eine Kopie des Feldes erstellen, um bei einem illegalen Zug alle Figuren leicht zurücksetzen zu können 
    last_rochade_moves = [] + rochade_moves # Für den Durchlauf eine Kopie der Liste erstellen, um bei einem illegalen Zug die Liste mit den bewegten Figuren zurücksetzen zu können
    
    source_field = chess_field[s_index] # s = source / Ausgangsfeld | Das Feld von dem aus sich die Figur bewegt
    move_to_field = chess_field[m_index] # m = moveto / Endfeld | Das Feld auf das die Figur bewegt werden soll
    
    s_field_key, s_field_number, s_figure, s_figure_texture, s_left_x, s_y_above, s_right_x, s_y_down, s_center_x, s_center_y, s_field_texture, s_figure_color, s_collum, s_row = source_field # Entpacken des source_fields
    m_field_key, m_field_number, m_figure, m_figure_texture, m_left_x, m_y_above, m_right_x, m_y_down, m_center_x, m_center_y, m_field_texture, m_figure_color, m_collum, m_row = move_to_field # Entpacken des move_to_fields
    
    if not automatic and not illegal_move_test: # Die folgenden 3 Methoden dürfen nur bei einem Zug und nicht bei einer Zugüberprüfung des Computers aufgerufen werden
        
        if len(s_e_p_hit) != 0 and s_figure.endswith("pawn"): # Falls im letzen Zug sich ein Bauer um 2 Felder nach vorne bewegt hat und somit von einem gegnerischen Bauern, der nun neben ihm steht geschlagen werden könnte
            f_x, f_y, figure_texture, f_f_number, f_target_field_x, f_target_field_y, f_figure_texture = s_e_p_hit[0] # Entpacken des 'schlagen en passant' hit 
            if f_target_field_x == m_center_x and f_target_field_y == m_center_y: # Falls das 'schlagen en passant' Feld mit den Koordinaten des Feldes, auf das sich die Figur gerade bewegt übereinstimmen 
                hittet_pawn = chess_field[f_f_number - 1]
                h_p_field_key, h_p_field_number, h_p_figure, h_p_figure_texture, h_p_left_x, h_p_y_above, h_p_right_x, h_p_y_down, h_p_center_x, h_p_center_y, h_p_field_texture, h_p_figure_color, h_p_collum, h_p_row = hittet_pawn # Entpacken des Feldes mit dem geschlagenen Bauern, da dieser sich nicht auf dem move_to Feld befindet, jedoch trotzdem entfernt werden muss
                chess_field[f_f_number - 1] = (h_p_field_key, h_p_field_number, "", "", h_p_left_x, h_p_y_above, h_p_right_x, h_p_y_down, h_p_center_x, h_p_center_y, h_p_field_texture, "", h_p_collum, h_p_row) # Verpacken des entsprechenden Feldes / überschreiben
            s_e_p_hit = []
        
        if s_figure.endswith("pawn"): # Abfrage, ob sich ein Bauer in diesem Zug um 16 Felder nach vorne bewegt, um diesen dann in die 'Schlagen en passant' Möglichkeit einzuschreiben 
            if s_field_number - 16 == m_field_number:
                schlagen_en_passant = [moves + 1, s_field_number - 8, m_field_number]
            elif s_field_number + 16 == m_field_number:
                schlagen_en_passant = [moves + 1, s_field_number + 8, m_field_number]
            
        
            if (m_collum == 1 and s_figure.startswith("white")) or (m_collum == 8 and s_figure.startswith("black")): # Falls ein Bauer sich auf die gegnerische letzte Linie begibt, tauscht er seinen Bauern gegen einen Turm, Pferd, Läufer oder eine Dame ein 
                sure = False
                while not sure:
                    e_figure = inputInt("Bauern ersetzen durch '1' Turm, '2' Pferd, '3' Laeufer, '4' Dame")# Leider hier UI-technisch sehr unschön, ging aber leider nicht anders, da TigerJython auf Maus Callbacks anscheinend Fenster erstellen, diese aber nicht mehr mit Inhalt füllen kann
                    if e_figure == 1:
                        output = "Turm"
                        e_figure = "_rock"
                        e_figure_texture = "_2.png"
                    elif e_figure == 2:
                        output = "Pferd"
                        e_figure = "_knight"
                        e_figure_texture = "_3.png"
                    elif e_figure == 3:
                        output = "Laeufer"
                        e_figure = "_bishop"
                        e_figure_texture = "_4.png"
                    elif e_figure == 4:
                        output = "Dame"
                        e_figure = "_queen"
                        e_figure_texture = "_1.png"
                    else:
                        continue # Hier ein else mit contínue, um den restlichen Schleifendurchlauf, also die 'sure' Zuweisung mit der Frage zu überspringen, da eine Zahl eingegeben wurde, der keine Figur zugeordent ist
                    sure = askYesNo("Moechtest du deinen Bauern wirklich durch eine*n " + output + " ersetzen?")
                
                s_figure = s_figure_color + e_figure
                s_figure_texture = chess_figure_file + "chess" + s_figure_color + e_figure_texture                               
                                                            
                                                            
        if s_figure.endswith("king"): # Dekativiren der Rochademöglichkeit für die entsprechende Figur, falls sich diese bewegt
            if s_figure.startswith("white"):
                rochade_moves[0] = True
            if s_figure.startswith("black"):
                rochade_moves[3] = True
        if s_figure.endswith("rock"):
            if s_figure.startswith("white"):
                if s_figure == "white_1_rock":
                    rochade_moves[1] = True
                if s_figure == "white_2_rock":
                    rochade_moves[2] = True
            if s_figure.startswith("black"):
                if s_figure == "black_1_rock":
                    rochade_moves[4] = True
                if s_figure == "black_2_rock":
                    rochade_moves[5] = True 
    
    m_figure = "" + s_figure
    m_figure_texture = "" + s_figure_texture
    m_figure_color = "" + s_figure_color
    
    s_figure = ""
    s_figure_texture = ""
    s_figure_color = ""
    
    if len(rochade_figure_place) != 0: # Falls eine Rochade durchgeführt werden könnte
        for t in rochade_figure_place:
            clicked_field, k_field_number, k, k_texture, k_color, k_t, rock_field_number, rock, rock_texture, rock_color, rock_t = t
            if clicked_field - 1 == m_index: # Prüft für jede Rochade, die in diesem Zug hätte durchgeführt werden können, ob sie durchgeführt wurde
                
                king_field = chess_field[k_field_number - 1] # weder source noch moveto Feld, da sich König und Turm bei der Rochade auf andere Felder bewegen, weshalb hier diese Felder entpackt werden müssen
                rock_field = chess_field[rock_field_number - 1] # weder source noch moveto Feld, da sich König und Turm bei der Rochade auf andere Felder bewegen, weshalb hier diese Felder entpackt werden müssen
                
                e_k_field_key, e_k_field_number, e_k_figure, e_k_figure_texture, e_k_left_x, e_k_y_above, e_k_right_x, e_k_y_down, e_k_center_x, e_k_center_y, e_k_field_texture, e_k_figure_color, e_k_collum, e_k_row = king_field
                e_rock_field_key, e_rock_field_number, e_rock_figure, e_rock_figure_texture, e_rock_left_x, e_rock_y_above, e_rock_right_x, e_rock_y_down, e_rock_center_x, e_rock_center_y, e_rock_field_texture, e_rock_figure_color, e_rock_collum, e_rock_row = rock_field    
                
                # Einpacken der Überschriebenden Felder
                chess_field[k_field_number - 1] = (e_k_field_key, e_k_field_number, k, k_texture, e_k_left_x, e_k_y_above, e_k_right_x, e_k_y_down, e_k_center_x, e_k_center_y, e_k_field_texture, k_color, e_k_collum, e_k_row)
                chess_field[rock_field_number - 1] = (e_rock_field_key, e_rock_field_number, rock, rock_texture, e_rock_left_x, e_rock_y_above, e_rock_right_x, e_rock_y_down, e_rock_center_x, e_rock_center_y, e_rock_field_texture, rock_color, e_rock_collum, e_rock_row)    
                
                rochade = True
            
                rochade_figure_place = []    
                # Moveto leeren, da sich Turm und König ja bereits auf andere Felder bewegt haben 
                m_figure = ""
                m_figure_texture = ""
                m_figure_color = "" 
    
    chess_field[s_index] = (s_field_key, s_field_number, s_figure, s_figure_texture, s_left_x, s_y_above, s_right_x, s_y_down, s_center_x, s_center_y, s_field_texture, s_figure_color, s_collum, s_row)
    chess_field[m_index] = (m_field_key, m_field_number, m_figure, m_figure_texture, m_left_x, m_y_above, m_right_x, m_y_down, m_center_x, m_center_y, m_field_texture, m_figure_color, m_collum, m_row)
    
    king_getter() # Ermitteln der neuen Königsfelder
            
    if illegal_move_test:
        check = check_check() # Überprüfung auf einen illegalen Zug
        king_getter() 
        chess_field = [] + last_chess_field # Feld mit der erstellten Kopie überschreiben
        rochade_moves = [] + last_rochade_moves # Liste mit den bewegten Rochadefiguren auf Stand vor dem illegalen Zug zurücksetzen
        return check

        
    if not automatic and not illegal_move_test: # Bei automatischem Programmdurchlauf würden im folgendem weitere automatische Programmdurchläufe entstehen
        
        player_change()# Spielerwechsel mit Spielertext, enemy und Zugcounter
        moves += 1  
        
        repaint() # Repainten des Schachfeldes, da sich die Figuren Grafisch bisher noch nicht bewegt haben
        return s_index
    
    if automatic:
        return source_field, s_index, move_to_field, m_index # Beim Automatischen durchlaufen die Ursprungsfelder zurückgeben, damit diese nach der automatischen Figurbewegung sich nicht ändern

def decolor(): # Funktion zum Entfärben der gedfärbten Felder
    global last_possible_fields
    global rochade_figure_place
    global figure_hit_fields
    global selected_field

    last_possible_fields = [] # Leeren der Listen und danach repainten wichtig, um Feld neu zu "malen"
    rochade_figure_place = []
    figure_hit_fields = []
    selected_field = []    
    
    repaint() # Repainten, um alle Färbungen zu entfernen


def check_check(): # Funktion zum Überprüfen ob der König im Schach steht
    global selected_field
    
    Check = False
    runde = 0
    for l_tuple in chess_field: # Für jedes Feld prüfen, ob eine gegnerische Figur auf diesem steht
        selected_field = [(l_tuple[8], l_tuple[9], l_tuple[10], l_tuple[2], l_tuple[1], l_tuple[12], l_tuple[13]), runde] # Neue Werte des Feldes zuweisen, wichtig da sonst die Überprüfung der Möglichen bewegungen der Figuren nicht funktioniert
        if l_tuple[11] == enemy:
            player_change() # Wechseln des Gegners wichtig, da für gegnerische Figuren ermittelt werden soll, ob diese den eingen König schlagen könnten 
            last_possible_fields, figure_hit_fields = check_figure_type(l_tuple[2]) # Funktionsaufruf mit der Figur, die auf dem aktuell überprüften Feld steht
            player_change() # Wichtig, da die Schlagmöglichkeit der gegnerischen Figuren gegen den EINGENEN König getestet werden soll
            for field_tuple in last_possible_fields: # Überprüfen für jedes mögliche Feld, das zuvor ermittelt wurde, ob die Figur den gegnerischen König schlagen könnte
                for king in king_fields:
                    if king[3] == active_player and (field_tuple[0] == king[0] and field_tuple[1] == king[1]):
                        Check = True # Schach-Situation durch eine Figur erkannt
        runde += 1
    return Check # Zurückgeben von 'False' oder 'True', jenachdem, ob ein König im Schach steht oder nicht

         
def check_check_mate(): # Funktion zum Überprüfen, ob ein Spieler Schachmatt ist | wird nur aufgerufen, falls ein König im Schach steht
    global selected_field
    
    check = True
    runde = 0
    for t_tuple in chess_field:
        selected_field = [(t_tuple[8], t_tuple[9], t_tuple[10], t_tuple[2], t_tuple[1], t_tuple[12], t_tuple[13]), runde] # Neue Werte des Feldes zuweisen, wichtig da sonst die Überprüfung der Möglichen bewegungen der Figuren nicht funktioniert
        if t_tuple[11] == active_player:
            last_possible_fields, figure_hit_fields = check_figure_type(t_tuple[2])
            for p_field in last_possible_fields:
                l_runde = 0
                for l_tuple in chess_field:
                    if p_field[0] == l_tuple[8] and p_field[1] == l_tuple[9]:
                        l_selected_field = [(l_tuple[8], l_tuple[9], l_tuple[10], l_tuple[2], l_tuple[1], l_tuple[12], l_tuple[13]), runde] # Neue Werte des Feldes zuweisen, wichtig da sonst die Überprüfung der Möglichen bewegungen der Figuren nicht funktioniert
                        source_field, s_index, move_to_field, m_index = figure_move(l_selected_field[1], l_runde, True)
                        check = check_check() # Prüfen, ob König noch im Schach steht, wenn nicht wird die Funktion abgebrochen
                        chess_field[s_index] = source_field # Zurücksetzen der Figuren auf ihre Ursprungsfelder
                        chess_field[m_index] = move_to_field
                        
                        king_getter() # Ermitteln, auf welchen Feldern die Könige stehen, da diese möglicher Weise bewegt wurden
                        
                    if not check:
                        return check # Bricht Funktion ab, da es eine Möglichkeit gibt aus dem "Schach" herauszokommen
                    l_runde += 1  
        runde += 1                   
    return check # Zurückgeben von 'False' oder 'True', jenachdem, ob ein König im Schachmatt ist oder nicht      

                          
def check_stalemate(): # Funktion zum Überprüfen auf ein Unentschieden
    stalemate = check_check_mate() # Prüfen, ob sich eine Figur bewegen kann, ohne dass der König nach der Bewegung im Schach steht
    
    if not stalemate: # Falls dies möglich ist, wird geguckt, ob es nur noch 2 Könige gibt, wodurch ebenfalls ein Unentschieden entsteht
        for field in chess_field:
            if not (field[2].endswith("king") or field[2] == ""): # Falls es ein Feld gibt, auf dem etwas anderes als nichts oder ein König steht wird die Schleife abgebrochen
                break # Hier sehr nützlich, da nur durch dieses Break das Else-Statement nicht ausgelöst wird
        else: # Fall das Break nicht einmal aufgerufen wurde, gibt es ein Unentschieden
            stalemate = True
                
    return stalemate # Zurückgeben von False oder True, jenachdem, ob das Spiel unentschieden ist oder nicht


def player_change(): # Funktion zum wechseln der Spieler
    global active_player
    global aktiver_spieler_text
    global enemy
    
    if active_player == "white":
        active_player = "black"
        aktiver_spieler_text = "Schwarz"
        enemy = "white"
    else:
        active_player = "white"
        aktiver_spieler_text = "Weiss"
        enemy = "black"


def king_getter(): # Funktion zum Ermitteln der Positionen der Könige
    global king_fields
    
    for c_tuple in chess_field: # Neu ermitteln des Königfeldes, falls dieses durch das Programm verändert wurde
        if c_tuple[2].endswith("king"):
            if c_tuple[2].startswith("black"):
                king_fields[0] = c_tuple[8], c_tuple[9], c_tuple[10], "black"
            elif c_tuple[2].startswith("white"):
                king_fields[1] = c_tuple[8], c_tuple[9], c_tuple[10], "white" 
                                                                                    
        
def check_figure_type(figure): # Funktion zum überprüfen, für welche Figur die nächst möglichen Felder ausgegeben werden soll
    
    if figure.endswith("pawn"):
        last_possible_fields, figure_hit_fields = possible_pawn_moves()   
    if figure.endswith("knight"):
        last_possible_fields, figure_hit_fields = possible_knight_moves()    
    if figure.endswith("rock"):
        last_possible_fields, figure_hit_fields = possible_rock_moves()  
    if figure.endswith("bishop"):
        last_possible_fields, figure_hit_fields = possibles_bishop_moves()   
    if figure.endswith("queen"):
        last_possible_fields, figure_hit_fields = possible_queen_moves()      
    if figure.endswith("king"):
        last_possible_fields, figure_hit_fields = possible_king_moves()    
    
    return last_possible_fields, figure_hit_fields # Zurückgeben der möglichen ermittelten Felder           


@gt.onMouseClicked    
def figure_select(x, y): # Funktion die auf Aufruf des obigen Mauscallbacks aufgrufen und ausgeführt wird | Der Mauscallback übergibt die angeklickten Koordinaten, mit welchen im Folgenden die anglickte Position überprüft wird
    global s_e_p_hit
    global selected_field
    global last_possible_fields
    global input_allowed
    global figure_hit_fields
    global rochade_figure_place
    
    check_mate = False
    stalemate = False
    index = 0
    if input_allowed: # Solange True, bis ein König fällt
        for large_tuple in chess_field: # Durchgehen jedes Feldes bis ein Feld mit den angeklickten Koordianten übereinstimmt, auf diesem werden dann die weiteren Schritte ausgeführt
            moved = False
            field_key, field_number, figure, figure_texture, left_x, y_above, right_x, y_down, center_x, center_y, field_texture, figure_color, collum, row = large_tuple # Entpacken des Schachfeld Tupels
            if (x >= left_x and y <= y_above) and (x <= right_x and y >= y_down): # Prüft ob das oben entpackte Schachfeld zu den angeklickten Koordinaten passt
                king_getter() # Wichtig, da es sonst zu illegalen Zugmöglichkeiten kommen kann, da die Könige noch auf anderen Feldern regestriert sind
                if len(last_possible_fields) != 0: # Falls bereits eine Figur ausgewählt wurde und Bewegungsmöglichkeiten für die Figur grün gefärbt wurden wir als erstes geprüft, ob das angeklickte Feld eines derer ist, auf die sich die Figur bewegen kann
                    for p_field in last_possible_fields: 
                        if center_x == p_field[0] and center_y == p_field[1]: # Falls die Center mit den Centern des aktuellen Feldes übereinstimmen 
                            moved = True
                            move_to_index = figure_move(selected_field[1], index) # Übergibt an die Move Funktion das augewählte Figurenfeld, sowie das Feld, auf welches sich die Figur bewegen soll
                            decolor() # Entfärben aller Felder sowie leeren der dazu gehörigen Listen 
                        
                            check = check_check() # Überprüfen, ob der König des aktuellen Spielers im Schach steht
                            if check: # Aufrufen der Schachmattfunktion nur, wenn ein König im Schach steht
                                check_mate = check_check_mate()
                            if not check:    
                                stalemate = check_stalemate()
                            
                            if check_mate:
                                player_change() # Wechseln des Gegners, da für seine Figuren die möglichen Züge ermittelt werden sollen, und seine Figuren die Figuren des aktiven Spielers schlagen könnten
                                
                                input_allowed = False # Weiteren Input nach Spielende verhindern 
                                setTitle("SPIELENDE   |   " + aktiver_spieler_text + " hat das Spiel gewonnen") # Titel am Spielende aktualisieren
                                msgDlg(aktiver_spieler_text + " hat das Spiel gewonnen!", title = "Schachmatt   |   " + aktiver_spieler_text + " gewinnt das Spiel")
                                
                            if not check_mate and check:
                                msgDlg(aktiver_spieler_text + ", du stehst im Schach \nSchuetze deinen Koenig!", title = "SCHACH") # Ausgabe 'Schach'
                                
                            if stalemate:
                                input_allowed = False # Weiteren Input nach Spielende verhindern 
                                setTitle("SPIELENDE   |   Unentschieden") # Titel am Spielende aktualisieren
                                msgDlg("Unentschieden!", title = "Patt   |   Niemand gewinnt das Spiel")
                                
                            selected_field = []
                            break
                if moved:
                    break # Keine Andere Möglichkeit gefunden | Schleife muss im if Fall sofort abgebrochen werden, da es sonst zu verherenden Fehlern kommen kann
                if figure != "" and figure_color == active_player: # Falls das angeklickte Feld nicht leer und die Figurenfarbe mit dem aktiven Spieler übereinstimmt
                    decolor()
                    selected_field.append((center_x, center_y, field_texture, figure, field_number, collum, row))# Nach leeren und entfärben wird hier die neu ausgewählte Figur aufgenommen
                    selected_field.append(index) # Speichern des Indexes des ausgewählten Feldes | Wichtig für die move Funktion
                    gt.setPos(center_x - (25 * mX) , center_y)
                    gt.setFillColor("lightblue") # Makieren der ausgewählten Figur durch färben des Feldes unter ihr
                    gt.fill()
                    
                    last_possible_fields, figure_hit_fields = check_figure_type(figure) # Funktionsaufrufe je nach ausgewählter Figur
                    new_possible_moves = []
                    for l_tuple in last_possible_fields: # Für jedes possible Field wird geguckt, ob der Zug legal wäre, wenn nicht wird das Feld nicht zur neuen Liste hinzugefügt, die die Alte dann ersetzt
                        selected_copy = [] + selected_field # Copy von selected_field, da dieses sich ändert und sonst nichts mehr funktioniert
                        figure_hit_copy = [] + figure_hit_fields
                        rochade_copy = [] + rochade_figure_place
                        
                        check = figure_move(selected_field[1], l_tuple[3] - 1, False, True) # Hier wird die legalität des möglichen Zuges überprüft
                        
                        selected_field = [] + selected_copy # selected_field mit der erzeugten Kopie überschreiben
                        figure_hit_fields = [] + figure_hit_copy
                        rochade_figure_place = [] + rochade_copy
                        
                        if not check: # Falls der mögliche Zug nicht illegal ist, wird er zu den neuen möglichen Zügen hinzugefügt
                            new_possible_moves.append(l_tuple)
                    last_possible_fields = [] + new_possible_moves # Überschreiben der Liste mit dedn möglichen Feldern, mit den möglichen legalen Feldern
                    
                    new_hit_fields = []
                    for f in figure_hit_fields: # Überprüfen, ob eine Schlagmöglichkeit soeben als illegal erkannt wurde, falls dies der Fall ist MUSS dieses Feld auch aus figure_hit_field entfernt werden
                        for l in last_possible_fields:
                            if f == l: # Falls das Hit field noch in den möglichen ist, wird es der neuen Liste hinzugefügt
                                new_hit_fields.append(f)
                    figure_hit_fields = [] + new_hit_fields # Überschreiben der alten möglichen Schläge mit den möglichen legalen Schlägen
                    
                    new_rochade_fields = []
                    for f in rochade_figure_place:
                            for l in last_possible_fields:
                                if f[0] == l[3]: # Wenn die Feldnummern übereinstimmen
                                    new_rochade_fields.append(f)
                    rochade_figure_place = [] + new_rochade_fields
                                
                          
                    for f in last_possible_fields: # Färben der möglichen Züge 
                        f_x, f_y, field_texture, f_number = f
                        gt.setPos(f_x - (25 * mX), f_y) # -25, da es sonst zu Färbfehlern kommt
                        gt.setFillColor("lime")
                        gt.fill()
                    for f in rochade_figure_place: # Färben der Felder für König und Turm bei einer Rochade
                        for t in f:
                            if type(t) is tuple:
                                t_x, t_y, field_texture = t
                                gt.setPos(t_x - (25 * mX), t_y) # -25, da es sonst zu Färbfehlern kommt
                                gt.setFillColor("purple")
                                gt.fill()
                    for f in figure_hit_fields:
                        f_x, f_y, field_texture, f_number = f
                        gt.setPos(f_x - (25 * mX), f_y) # -25, da es sonst zu Färbfehlern kommt
                        gt.setFillColor("red")
                        gt.fill()
                        
            index += 1 # Nach einem Schleifendurchlauf wird der Index um 1 erhöht 
          
