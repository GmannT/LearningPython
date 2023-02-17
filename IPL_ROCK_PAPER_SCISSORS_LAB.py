#IPL_ROCK_PAPER_SCISSORS_LAB
import random


def game():
    userChoice = int(input("Rock(1) Paper(2) or Scissors(3) ? "))

    if userChoice == 1:
        play = "Rock"
    elif userChoice == 2:
        play = "Paper"
    elif userChoice == 3:
        play = "Scissors"
    else:
        play = "Invalid Choice."
        userChoice = -1
        
    computerOptions = [1, 2 ,3]
    computerChoice = random.choice(computerOptions)
    
    if computerChoice == 1:
        computerPlay = "Rock"
    elif computerChoice == 2:
        computerPlay = "Paper"
    else:
        computerPlay = "Scissors"
        
    print(userName + " plays " + play)
    
    print("The computer plays " + computerPlay)
    
    return userChoice, computerChoice



def whoWon(userChoice, computerChoice):
    global pWinCount
    global cWinCount
    
    if userChoice == -1:
        winner = 2
    elif ((userChoice == 1) and (computerChoice == 2)):
        winner = 2
    elif ((userChoice == 2) and (computerChoice == 3)):
        winner = 2
    elif ((userChoice == 3) and (computerChoice == 1)):
        winner = 2
    elif ((userChoice == 1) and (computerChoice == 3)):
        winner = 1
    elif ((userChoice == 2) and (computerChoice == 1)):
        winner = 1
    elif ((userChoice == 3) and (computerChoice == 2)):
        winner = 1
    else:
        winner = 0
    
    personWins = ["You have won this round...", "Lucky", "The computer lost", "Let's see you do that again"]
    computerWins = ["You lose.", "It seems the human is inferior", "The computer wins, as expected.", "Unfortunately for you"]
    
    if winner == 1:
        print(random.choice(personWins))
        pWinCount += 1
    elif winner == 2:
        print(random.choice(computerWins))
        cWinCount +=1
    else:
        print("A draw...")
   
    print("The score is: computer " + str(cWinCount) + " human " + str(pWinCount))
    print()

def gameOver():
    if ((pWinCount == 3) or (cWinCount == 3)):
        return True
    else:
        return False




userName = str(input("What is your name? "))

print("Are you ready to play Rock Paper Scissors?")
print("The first to 3 in a best of 5 game wins!")

pWinCount = 0
cWinCount = 0

if gameOver() == False:
    userChoice, computerChoice = game()
    whoWon(userChoice, computerChoice)

if gameOver() == False:
    userChoice, computerChoice = game()
    whoWon(userChoice, computerChoice)

if gameOver() == False:
    userChoice, computerChoice = game()
    whoWon(userChoice, computerChoice)

if gameOver() == False:
    userChoice, computerChoice = game()
    whoWon(userChoice, computerChoice)

if gameOver() == False:
    userChoice, computerChoice = game()
    whoWon(userChoice, computerChoice)

if gameOver() == False:
    userChoice, computerChoice = game()
    whoWon(userChoice, computerChoice)

if gameOver() == False:
    userChoice, computerChoice = game()
    whoWon(userChoice, computerChoice)

if gameOver() == False:
    userChoice, computerChoice = game()
    whoWon(userChoice, computerChoice)

if gameOver() == False:
    userChoice, computerChoice = game()
    whoWon(userChoice, computerChoice)

if gameOver() == False:
    userChoice, computerChoice = game()
    whoWon(userChoice, computerChoice)

    
if pWinCount == cWinCount:
    print("You have had an almost statisticly impossible game, wow!")
elif cWinCount > pWinCount:
    print("Computer Wins.")
else:
    print(userName + " wins")
    

