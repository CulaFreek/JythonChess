import socket
import threading

games = {}

def handleClient(clientSocket):
    try:
        # Liste der offenen Gamerooms an den Client senden
        openGames = ', '.join(games.keys()) or "Keine offenen Games"
        clientSocket.send("Verfügbare Games: {}".format(openGames))
        # Game-Code vom Client erhalten
        gameCode = clientSocket.recv(1024)

        # Überprüfen, ob das Game bereits existiert oder erstellt werden muss
        if gameCode not in games:
            # Neues Game erstellen
            games[gameCode] = [clientSocket]
            clientSocket.send("Game {} erstellt. Warte auf weitere Mitglieder...".format(gameCode))
            print("Game {} erstellt.".format(gameCode))
        else:
            # Bestehendem Game beitreten
            if len(games[gameCode]) >= 2:
                clientSocket.send("Das Game {} ist voll! Bitte erstelle ein neus Game oder joine einem anderem".format(gameCode))
            else:
                games[gameCode].append(clientSocket)
                clientSocket.send("Du bist dem Game {} beigetreten.".format(gameCode))

            # Warte auf den zweiten Client, bevor Nachrichten gesendet werden können
            while len(games[gameCode]) < 2:
                clientSocket.send("Warte auf weiteren Spieler...")
            
            member = games[gameCode]
            member[0].send("black")
            # Gegner an Member senden
            clientSocket.send("white")

        while True:
            data = clientSocket.recv(1024)
            if not data:
                break
            message = data
            broadcast("{}".format(message), games[gameCode], clientSocket)
            

    except Exception as e:
        print("Fehler beim Umgang mit Client: {}".format(e))
    finally:
        # Client aus dem Game entfernen
        for code, members in games.items():
            if clientSocket in members:
                members.remove(clientSocket)
                if not members:
                    # Lösche das Game, wenn keine Mitglieder mehr vorhanden sind
                    del games[code]
                break
        clientSocket.close()

def broadcast(message, members, senderSocket):
    # Sende die Nachricht an alle Mitglieder des Games
    for memberSocket in members:
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