import socket
import threading
import random

games = {}

def handleClient(clientSocket):
    try:
        openGames = ', '.join(games.keys()) or "Keine offenen Games" # Liste der offenen Gamerooms an den Client senden
        clientSocket.send("Verfügbare Games: '{}'".format(openGames))
        gameCode = clientSocket.recv(1024) # Auf Beitrittsentscheidung des Clients warten
        
        if gameCode not in games: # Überprüfen, ob das Game bereits existiert oder erstellt werden muss
            games[gameCode] = [clientSocket] # Falls das Spiel nicht existiert neues erstellen
            clientSocket.send("Game {} erstellt. Warte auf weitere Mitglieder...".format(gameCode))
            print("Game {} erstellt.".format(gameCode))
        else:
            if len(games[gameCode]) >= 2: # Bestehendem Game beitreten
                clientSocket.send("Das Game {} ist voll! Bitte erstelle ein neus Game oder joine einem anderem".format(gameCode))
            else:
                games[gameCode].append(clientSocket)
                clientSocket.send("Du bist dem Game {} beigetreten.".format(gameCode))

            while len(games[gameCode]) < 2: # Auf Beitritt des 2.ten Spielers warten
                clientSocket.send("Warte auf weiteren Spieler...")
            
            randomNumber = random.randint(0,1) # Farbenzufallsgenerator, damit der Spieler, der sich als erstes verbindet nicht zwangsweise Weiß spielt
            if randomNumber == 0:
                member = games[gameCode]
                member[0].send("black")
                clientSocket.send("white")
            else:
                member = games[gameCode]
                member[0].send("white")
                clientSocket.send("black")

        while True:
            data = clientSocket.recv(1024)
            if not data:
                break
            message = data
            broadcast("{}".format(message), games[gameCode], clientSocket)
            

    except Exception as e:
        print("Fehler beim Umgang mit Client: {}".format(e))
    finally: # Client aus dem Game entfernen wenn ein Fehler vorliegt
        for code, members in games.items():
            if clientSocket in members:
                members.remove(clientSocket)
                if not members:
                    del games[code]
                break
        clientSocket.close()

def broadcast(message, members, senderSocket):
    for memberSocket in members: # Sende die Nachricht an alle Mitglieder des Games
        try:
            memberSocket.send(message)
        except Exception as e:
            print("Fehler beim übermittlen der Nachricht: {}".format(e))

def startServer():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('0.0.0.0', 8888))
    serverSocket.listen(787)

    print("Server gestartet auf Port 8888...")

    try:
        while True:
            clientSocket, addr = serverSocket.accept()
            print("Verbindung von: {}".format(addr))
            clientHandler = threading.Thread(target = handleClient, args = (clientSocket,))
            clientHandler.start()
    except KeyboardInterrupt:
        print("Server faehrt herunter...")
    finally:
        serverSocket.close()

if __name__ == "__main__":
    startServer()