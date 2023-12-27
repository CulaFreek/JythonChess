# piece-square tables für alle figuren die angeben wie gut sie auf den jeweiligen feldern positioniert sind
pawnTable = {
    1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0,
    9: 5, 10: 10, 11: 10, 12: -20, 13: -20, 14: 10, 15: 10, 16: 5,
    17: 5, 18: -5, 19: -10, 20: 0, 21: 0, 22: -10, 23: -5, 24: 5,
    25: 0, 26: 0, 27: 0, 28: 20, 29: 20, 30: 0, 31: 0, 32: 0,
    33: 5, 34: 5, 35: 10, 36: 25, 37: 25, 38: 10, 39: 5, 40: 5,
    41: 10, 42: 10, 43: 20, 44: 30, 45: 30, 46: 20, 47: 10, 48: 10,
    49: 50, 50: 50, 51: 50, 52: 50, 53: 50, 54: 50, 55: 50, 56: 50,
    57: 0, 58: 0, 59: 0, 60: 0, 61: 0, 62: 0, 63: 0, 64: 0
}
knightTable = {
    1: -50, 2: -40, 3: -30, 4: -30, 5: -30, 6: -30, 7: -40, 8: -50,
    9: -40, 10: -20, 11: 0, 12: 5, 13: 5, 14: 0, 15: -20, 16: -40,
    17: -30, 18: 5, 19: 10, 20: 15, 21: 15, 22: 10, 23: 5, 24: -30,
    25: -30, 26: 0, 27: 15, 28: 20, 29: 20, 30: 15, 31: 0, 32: -30,
    33: -30, 34: 5, 35: 15, 36: 20, 37: 20, 38: 15, 39: 5, 40: -30,
    41: -30, 42: 0, 43: 10, 44: 15, 45: 15, 46: 10, 47: 0, 48: -30,
    49: -40, 50: -20, 51: 0, 52: 0, 53: 0, 54: 0, 55: -20, 56: -40,
    57: -50, 58: -40, 59: -30, 60: -30, 61: -30, 62: -30, 63: -40, 64: -50
}
bishopTable = {
    1: -20, 2: -10, 3: -10, 4: -10, 5: -10, 6: -10, 7: -10, 8: -20,
    9: -10, 10: 5, 11: 0, 12: 0, 13: 0, 14: 0, 15: 5, 16: -10,
    17: -10, 18: 10, 19: 10, 20: 10, 21: 10, 22: 10, 23: 10, 24: -10,
    25: -10, 26: 0, 27: 10, 28: 10, 29: 10, 30: 10, 31: 0, 32: -10,
    33: -10, 34: 5, 35: 5, 36: 10, 37: 10, 38: 5, 39: 5, 40: -10,
    41: -10, 42: 10, 43: 10, 44: 10, 45: 10, 46: 10, 47: 10, 48: -10,
    49: -10, 50: 5, 51: 0, 52: 0, 53: 0, 54: 0, 55: 5, 56: -10,
    57: -20, 58: -10, 59: -10, 60: -10, 61: -10, 62: -10, 63: -10, 64: -20,
}
rookTable = {
    64: 0, 63: 0, 62: 0, 61: 0, 60: 0, 59: 0, 58: 0, 57: 0,
    56: 5, 55: 10, 54: 10, 53: 10, 52: 10, 51: 10, 50: 10, 49: 5,
    48: -5, 47: 0, 46: 0, 45: 0, 44: 0, 43: 0, 42: 0, 41: -5,
    40: -5, 39: 0, 38: 0, 37: 0, 36: 0, 35: 0, 34: 0, 33: -5,
    32: -5, 31: 0, 30: 0, 29: 0, 28: 0, 27: 0, 26: 0, 25: -5,
    24: -5, 23: 0, 22: 0, 21: 0, 20: 0, 19: 0, 18: 0, 17: -5,
    16: -5, 15: 0, 14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: -5,
    8: 0, 7: 0, 6: 0, 5: 5, 4: 5, 3: 0, 2: 0, 1: 0
}
queenTable = {
    1: -20, 2: -10, 3: -10, 4: -5, 5: -5, 6: -10, 7: -10, 8: -20,
    9: -10, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: -10,
    17: -10, 18: 0, 19: 5, 20: 5, 21: 5, 22: 5, 23: 0, 24: -10,
    25: -5, 26: 0, 27: 5, 28: 5, 29: 5, 30: 5, 31: 0, 32: -5,
    33: 0, 34: 0, 35: 5, 36: 5, 37: 5, 38: 5, 39: 0, 40: -5,
    41: -10, 42: 5, 43: 5, 44: 5, 45: 5, 46: 5, 47: 0, 48: -10,
    49: -10, 50: 0, 51: 5, 52: 0, 53: 0, 54: 0, 55: 0, 56: -10,
    57: -20, 58: -10, 59: -10, 60: -5, 61: -5, 62: -10, 63: -10, 64: -20
}
kingTable = {
    64: -30, 63: -40, 62: -40, 61: -50, 60: -50, 59: -40, 58: -40, 57: -30,
    56: -30, 55: -40, 54: -40, 53: -50, 52: -50, 51: -40, 50: -40, 49: -30,
    48: -30, 47: -40, 46: -40, 45: -50, 44: -50, 43: -40, 42: -40, 41: -30,
    40: -30, 39: -40, 38: -40, 37: -50, 36: -50, 35: -40, 34: -40, 33: -30,
    32: -20, 31: -30, 30: -30, 29: -40, 28: -40, 27: -30, 26: -30, 25: -20,
    24: -10, 23: -20, 22: -20, 21: -20, 20: -20, 19: -20, 18: -20, 17: -10,
    16: 20, 15: 20, 14: 0, 13: 0, 12: 0, 11: 0, 10: 20, 9: 20,
    8: 20, 7: 30, 6: 10, 5: 0, 4: 0, 3: 10, 2: 30, 1: 20
}

#DEBUG
chessField = [  # fieldKey, fieldNumber, figure, figureTexture, leftX, yAbove, centerX, centerY, fieldTexture, figureColor, colum, row
    ("8a", 1, "black_1_rook", "chessblack_2.png", 0 , 0 , 50 , 50 , 1, "black", 1, 1), ("8b", 2, "black_knight", "chessblack_3.png", 100 , 0 , 150 , 50 , 1, "black", 1, 2), ("8c", 3, "black_bishop", "chessblack_4.png", 200 , 0 , 250 , 50 , 1, "black", 1, 3), ("8d", 4, "black_queen", "chessblack_1.png", 300 , 0 , 350 , 50 , 1, "black", 1, 4), ("8e", 5, "black_king", "chessblack_0.png", 400 , 0 , 450 , 50 , 1, "black", 1, 5), ("8f", 6, "black_bishop", "chessblack_4.png", 500 , 0 , 550 , 50 , 1, "black", 1, 6), ("8g", 7, "black_knight", "chessblack_3.png", 600 , 0 , 650 , 50 , 1, "black", 1, 7), ("8h", 8, "black_2_rook", "chessblack_2.png", 700 , 0 , 750 , 50 , 1, "black", 1, 8),
    ("7a", 9, "black_pawn", "chessblack_5.png", 0 , 100 , 50 , 150 , 1, "black", 2, 1), ("7b", 10, "black_pawn", "chessblack_5.png", 100 , 100 , 150 , 150 , 1, "black", 2, 2), ("7c", 11, "black_pawn", "chessblack_5.png", 200 , 100 , 250 , 150 , 1, "black", 2, 3), ("7d", 12, "black_pawn", "chessblack_5.png", 300 , 100 , 350 , 150 , 1, "black", 2, 4), ("7e", 13, "black_pawn", "chessblack_5.png", 400 , 100 , 450 , 150 , 1, "black", 2, 5), ("7f", 14, "black_pawn", "chessblack_5.png", 500 , 100 , 550 , 150 , 1, "black", 2, 6), ("7g", 15, "black_pawn", "chessblack_5.png", 600 , 100 , 650 , 150 , 1, "black", 2, 7), ("7h", 16, "black_pawn", "chessblack_5.png", 700 , 100 , 750 , 150 , 1, "black", 2, 8),
    ("6a", 17, "", "", 0 , 200 , 50 , 250 , 1, "", 3, 1), ("6b", 18, "", "", 100 , 200 , 150 , 250 , 1, "", 3, 2), ("6c", 19, "", "", 200 , 200 , 250 , 250 , 1, "", 3, 3), ("6d", 20, "", "", 300 , 200 , 350 , 250 , 1, "", 3, 4), ("6e", 21, "", "", 400 , 200 , 450 , 250 , 1, "", 3, 5), ("6f", 22, "", "", 500 , 200 , 550 , 250 , 1, "", 3, 6), ("6g", 23, "", "", 600 , 200 , 650 , 250 , 1, "", 3, 7), ("6h", 24, "", "", 700 , 200 , 750 , 250 , 1, "", 3, 8),
    ("5a", 25, "", "", 0 , 300 , 50 , 350 , 1, "", 4, 1), ("5b", 26, "", "", 100 , 300 , 150 , 350 , 1, "", 4, 2), ("5c", 27, "", "", 200 , 300 , 250 , 350 , 1, "", 4, 3), ("5d", 28, "", "", 300 , 300 , 350 , 350 , 1, "", 4, 4), ("5e", 29, "", "", 400 , 300 , 450 , 350 , 1, "", 4, 5), ("5f", 30, "", "", 500 , 300 , 550 , 350 , 1, "", 4, 6), ("5g", 31, "", "", 600 , 300 , 650 , 350 , 1, "", 4, 7), ("5h", 32, "", "", 700 , 300 , 750 , 350 , 1, "", 4, 8),
    ("4a", 33, "", "", 0 , 400 , 50 , 450 , 1, "", 5, 1), ("4b", 34, "", "", 100 , 400 , 150 , 450 , 1, "", 5, 2), ("4c", 35, "", "", 200 , 400 , 250 , 450 , 1, "", 5, 3), ("4d", 36, "", "", 300 , 400 , 350 , 450 , 1, "", 5, 4), ("4e", 37, "", "", 400 , 400 , 450 , 450 , 1, "", 5, 5), ("4f", 38, "", "", 500 , 400 , 550 , 450 , 1, "", 5, 6), ("4g", 39, "", "", 600 , 400 , 650 , 450 , 1, "", 5, 7), ("4h", 40, "", "", 700 , 400 , 750 , 450 , 1, "", 5, 8),
    ("3a", 41, "", "", 0 , 500 , 50 , 550 , 1, "", 6, 1), ("3b", 42, "", "", 100 , 500 , 150 , 550 , 1, "", 6, 2), ("3c", 43, "", "", 200 , 500 , 250 , 550 , 1, "", 6, 3), ("3d", 44, "", "", 300 , 500 , 350 , 550 , 1, "", 6, 4), ("3e", 45, "", "", 400 , 500 , 450 , 550 , 1, "", 6, 5), ("3f", 46, "", "", 500 , 500 , 550 , 550 , 1, "", 6, 6), ("3g", 47, "", "", 600 , 500 , 650 , 550 , 1, "", 6, 7), ("3h", 48, "", "", 700 , 500 , 750 , 550 , 1, "", 6, 8),
    ("2a", 49, "white_pawn", "chesswhite_5.png", 0 , 600 , 50 , 650 , 1, "white", 7, 1), ("2b", 50, "white_pawn", "chesswhite_5.png", 100 , 600 , 150 , 650 , 1, "white", 7, 2), ("2c", 51, "white_pawn", "chesswhite_5.png", 200 , 600 , 250 , 650 , 1, "white", 7, 3), ("2d", 52, "white_pawn", "chesswhite_5.png", 300 , 600 , 350 , 650 , 1, "white", 7, 4), ("2e", 53, "white_pawn", "chesswhite_5.png", 400 , 600 , 450 , 650 , 1, "white", 7, 5), ("2f", 54, "white_pawn", "chesswhite_5.png", 500 , 600 , 550 , 650 , 1, "white", 7, 6), ("2g", 55, "white_pawn", "chesswhite_5.png", 600 , 600 , 650 , 650 , 1, "white", 7, 7), ("2h", 56, "white_pawn", "chesswhite_5.png", 700 , 600 , 750 , 650 , 1, "white", 7, 8),
    ("1a", 57, "white_1_rook", "chesswhite_2.png", 0 , 700 , 50 , 750 , 1, "white", 8, 1), ("1b", 58, "white_knight", "chesswhite_3.png", 100 , 700 , 150 , 750 , 1, "white", 8, 2), ("1c", 59, "white_bishop", "chesswhite_4.png", 200 , 700 , 250 , 750 , 1, "white", 8, 3), ("1d", 60, "white_queen", "chesswhite_1.png", 300 , 700 , 350 , 750 , 1, "white", 8, 4), ("1e", 61, "white_king", "chesswhite_0.png", 400 , 700 , 450 , 750 , 1, "white", 8, 5), ("1f", 62, "white_bishop", "chesswhite_4.png", 500 , 700 , 550 , 750 , 1, "white", 8, 6), ("1g", 63, "white_knight", "chesswhite_3.png", 600 , 700 , 650 , 750 , 1, "white", 8, 7), ("1h", 64, "white_2_rook", "chesswhite_2.png", 700 , 700 , 750 , 750 , 1, "white", 8, 8)
]

#Funktion, die das aktuelle Board bewertet und einen Score anhand folgender Kriterien zurueckgibt:
# 1. Pure Materialkosten,
# 2. Position des Materials,
# (work in progress)
def evaluate(board):
    score = 0
    for field in board:
        # 0             1         2           3         4       5       6        7          8             9          10    11
        fieldKey, fieldNumber, figure, figureTexture, leftX, yAbove, centerX, centerY, fieldTexture, figureColor, column, row = field
        if figureColor == "black":
            if figure.endswith("pawn"):
                score += pawnTable[field[1]] + 100
            elif figure.endswith("knight"):
                score += knightTable[field[1]] + 320
            elif figure.endswith("bishop"):
                score += bishopTable[field[1]] + 330
            elif figure.endswith("rook"):
                score += rookTable[field[1]] + 500
            elif figure.endswith("queen"):
                score += queenTable[field[1]] + 900
            elif figure.endswith("king"):
                print("king")
                score += kingTable[field[1]] + 20000

        if figureColor == "white":
            if figure.endswith("pawn"):
                score -= 100
            elif figure.endswith("knight"):
                score -= 320
            elif figure.endswith("bishop"):
                score -= 330
            elif figure.endswith("rook"):
                score -= 500
            elif figure.endswith("queen"):
                score -= 900
            elif figure.endswith("king"):
                score -= 20000
    return score
#funktion, die den besten möglichen zug (aktuell noch tiefe 1) zurueckgibt
def search(board, moves):
    bestMove = ()
    bestValue = -2000000
    #durch alle möglichen zuege loopen und evaluaten wie gut der move ist
    for move in moves:
        #TODO: move temporär machen und das resultierende board evaluaten, vllt nur veränderung eval für schnelleren code (check promote true/false)
        value = evaluate(board)
        #undo move??
        if value > bestValue:
            bestMove = move
            bestValue = value
    return bestMove
print(evaluate(chessField))