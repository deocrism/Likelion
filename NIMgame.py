import random
#class PLAYER
#global 0 object
#player should have function to add to global object
#can have player names
#should be able to add to number
#there should be turns
#there should be terminating condition
class Player:
    #__init__ is run immediately when class Car is run, always run.
    #self creates an empty object, and in the self, fill in the different params from user
    #class type automagically creates the self ={}
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.loses = 0
    
    def addNumber(self):
        print(f"{self.name}'s turn.")
        inputNumber = int(input("Add number between 1-3?: "))
        while inputNumber > 3 or inputNumber < 1:
            inputNumber = int(input("It must be a number between 1-3: "))
        return inputNumber
    

print("Rules of the game: There will be two players competing against each other. Each player will get a turn to add a number between 1-3, and the first to hit 30 loses the match. The starting number is 0 and the starting player is chosen at random.")
player1 = Player(input("Enter Player 1's name: "))
player2 = Player(input("Enter Player 2's name: "))
totalRounds = int(input("The winner will be the best of how many matches? "))
matches = totalRounds//2+1
startgame = input(f"The player who wins {matches} matches first wins. Continue [Yes/No]? ")
while 'no' in startgame.lower():
    totalRounds = int(input("Then how many matches should it be? "))
    startgame = input(f"Then the first to {totalRounds//2+1} points wins. Are you sure [Yes/No]? ")
matches = totalRounds//2+1


def startNewGame():
    #print (player1.name)
    print(f"Current Score:\n\
        {player1.name}: {player1.wins}\n\
        {player2.name}: {player2.wins}")
    counter = 0
    turnPlayer1 = bool(random.getrandbits(1))
    while counter < 30:
        if counter == 0:
            print("The starting number is 0.")
        else:
            print(f"The number is now: {counter}")
        if turnPlayer1 == True:
            playerincrement = player1.addNumber()
            turnPlayer1 = False
        else:
            playerincrement = player2.addNumber()
            turnPlayer1 = True
        counter += playerincrement

    #Whose the winner
    if turnPlayer1 == True:
        print(f"{player1.name} wins this round.")
        player1.wins += 1
        player2.loses += 1
    else:
        print(f"{player2.name} wins this round.")
        player2.wins += 1
        player1.loses += 1
    if player1.wins == matches:
        print(f"Congratulations {player1.name}! You have won the game. You won {matches} out of {totalRounds} rounds. ")
        print(f"{player2.name}, you should be ashamed of yourself.")
    elif player2.wins == matches:
        print(f"Congratulations {player2.name}! You have won the game. You won {matches} out of {totalRounds} rounds. ")
        print(f"{player1.name}, you should be ashamed of yourself.")
    else:
        input("Starting new round. Press Enter to continue")
        startNewGame()

#HOMEWORK - start new game (have option to choose best of #)
#And terminate whoever wins when best reached

startNewGame()
