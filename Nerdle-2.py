import Draw
import random 

#I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus and the academic integrity policy of the CS department.

NEXT_CHAR = 100
LEFT_MARGIN=84.5
NEXT_RECT=43
SIDE_LENGTH=40

def getEqnList(fileName):
    #open the file of equations 
    fin=open(fileName)
    line=fin.readline()
    Eqns=[]
    #make a list of all the possible equations
    while line:
        Eqns.append(line)
        line=fin.readline()
    fin.close()
    return Eqns

def getKey():
    while True:
        #if the player has typed a valid key, return that key in its proper format
        if Draw.hasNextKeyTyped():
            key=Draw.nextKeyTyped()
            if key in "0123456789" or key=="BackSpace" or key=="Return":
                return key
            elif  key=="equal":
                return "="
            elif key=="plus":
                return "+"
            elif key=="minus":
                return "-"
            elif key=="asterisk":
                return "*"
            elif key=="slash":
                return "/"
            
def getGuess(tryNum):
    #returns the player's final guess
    guess=""
    #get the valid key that the player pressed
    while True:
        key=getKey()
    #if the player pressed backspace, change&redraw their guess with the last character sliced off
        if key=="BackSpace" and len(guess)>0:
            guess=guess[:-1]
            redrawGuess(guess,tryNum)
    #if the player pressed a valid key, add that to their guess and redraw
        elif key in "0123456789" and len(guess)<8:
            guess+=key
            redrawGuess(guess,tryNum)
        elif (key=="+" or key=="-" or key=="/" or key=="*" or key=="=")and len(guess)<8:
            guess+=key
            redrawGuess(guess,tryNum)                 
    #if the player pressed enter, check that they filled all 8 boxes and return their guess
        elif key=="Return" and len(guess)==8 and isValid(guess):
            return guess
        
        
def redrawGuess(guess, tryNum):
    #redraws the player's current guess when they type a valid key
    Draw.setFontFamily("Courier")  
    Draw.setFontSize(14)
    #compute yTop from tryNum
    yTop=tryNum*55+85
    #draw filled rectangle at yTop:
    Draw.setColor(Draw.BLACK)
    for i in range(8):
        Draw.filledRect(LEFT_MARGIN+i*NEXT_RECT,yTop,SIDE_LENGTH,SIDE_LENGTH)
    #draw each character of the player's updated guess:
    Draw.setColor(Draw.WHITE)
    for i in range(8):
        Draw.string(guess[i:i+1],i*NEXT_RECT+NEXT_CHAR,yTop+10)
    Draw.show()

def letterFind(guessLetter,goal):
    #checks if the letter of the player's guess us somewhere in the solution, and returns its location
    for j in range(len(goal)):
        if guessLetter==goal[j]:
            return j
    #if that letter is not in the solution, return -1
    return -1
    
def drawColoredGuess(goal,guess,tryNum):
    #evaluates player's complete guess and displays colors accordingly
    #(greeen= correct yellow=character is somewhere else in solution  black=character is nowhere in solution)
    numGreens=0
    goal=[j for j in goal]
    yTop=tryNum*55+85
    #evaluate player's guess, character by character
    for j in range(len(guess)):
        #if the character is correct:
        if guess[j]==goal[j]:
            #make that character's rectangle green
            myGreen=Draw.color(2,100,2)
            Draw.setColor(myGreen)
            Draw.filledRect(LEFT_MARGIN+j*NEXT_RECT,yTop,SIDE_LENGTH,SIDE_LENGTH)
            #make sure that character is only counted once
            goal[j]="Green"
            #increment numGreens
            numGreens+=1
    for j in range(len(guess)):
        if goal[j]!="Green":
            #if the character is not correct:
            found=letterFind(guess[j],goal)
            if found!=-1:
                #if the character is somewhere else in solution, make its rectangle yellow                
                myYellow=Draw.color(200,178,30)
                Draw.setColor(myYellow)
                #make sure that character is only counted once
                goal[found]=None
            else:
                #if character is nowhere in solution, make its rectangle black
                Draw.setColor(Draw.BLACK)
            Draw.filledRect(LEFT_MARGIN+j*NEXT_RECT,yTop,SIDE_LENGTH,SIDE_LENGTH)
        #redraw the rectangle and character
        Draw.setColor(Draw.WHITE)
        Draw.string(guess[j:j+1],j*NEXT_RECT+NEXT_CHAR,yTop+10) 
    Draw.show()
    return numGreens

def drawBoard():
    for row in range(6):
        #draws board grid of six rows, eight boxes in each
        yTop=row*55+85
        for col in range(8):
            Draw.filledRect(LEFT_MARGIN+col*NEXT_RECT,yTop,SIDE_LENGTH,SIDE_LENGTH)
        Draw.setFontSize(30)
        Draw.setFontFamily("Calibri")
        Draw.string("NERDLE!",185,15)

def isValid(guess):
    #checks that the user entered a valid equation:
    for i in range(len(guess)-1):
        #check that there aren't two operation symbols in a row 
        if guess[i]=="+" and guess[i+1]=="+":
            print("hi")
            return False
        elif guess[i]=="/" and guess[i+1]=="/":
            return False
        elif guess[i]=="*" and guess[i+1]=="*":
            return False
        elif guess[i]=="-" and guess[i+1]=="-":
            return False        
   
    i = guess.rfind('=')
    #check that there are no operation symbols after equal sign (if not an expression)
    if i==5 and (guess[i+1]=="+" or guess[i+1]=="-"):
        return False
    elif i==4 and (guess[i+1]=="+" or guess[i+1]=="-"):
        return False
    #check that equation is accurate
    if i < 0: return False
    t = guess[:i] + '==' + guess[i+1:]
    ans = False
    try:
        ans = eval(t)
    except:
        ans = False  
    return ans


def playGame():
    #choose a random equation from list
    goal=random.choice(getEqnList('NerdleEqns.txt'))
    print(goal)
    tryNum=0
    for row in range(6):
        #for each of 6 guesses, get the player's guess
        guess=getGuess(tryNum)
        #draw board accordingly
        numGreens=drawColoredGuess(goal,guess,tryNum)
        #keep track of what try player is on
        tryNum+=1        
        if numGreens==8:
            #if the player guessed correctly, display winning message and stop running
            Draw.setColor(Draw.BLACK)
            Draw.setFontSize(24)
            Draw.string("You win!",180,430)
            Draw.show()
            return
    #player made 6 guesses and was not correct, display losing message
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(14)
    Draw.string("Better luck next time! Answer: "+goal,48,430)
    Draw.show()

def main():
    drawBoard()
    playGame()
    
main()

