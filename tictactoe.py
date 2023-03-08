
game = {
        'topleft' : ' ', 
        'topmid' : ' ',  
        'topright' : ' ',  
        'midleft' : ' ',  
        'midmid' : ' ', 
        'midright' : ' ', 
        'lowleft' : ' ', 
        'lowmid' : ' ', 
        'lowright' : ' ', 
        }
gamerunner = True
currentplayer = 'X'
    
    
    
def printgame(game) :
        print(" | " + game['topleft'] + " | " + game['topmid'] + " | " + game['topright'] + " | ")
        print("---------------")
        print(" | " + game['midleft'] + " | " + game['midmid'] + " | " + game['midright'] + " | ")
        print("---------------")
        print(" | " + game['lowleft'] + " | " + game['lowmid'] + " | " + game['lowright'] + " | ")


       
    
def gameplay(game) :
        key = list(game.keys())
        while True :
                play = input(currentplayer + " turn, please enter where you want to place : ")
                if (play in key) and (game[play] != 'X' and game[play]  != 'O'):
                        game[play] = currentplayer 
                        break
                        
                        
                else :
                        print("Wrong input, either you've entered in a wrong value or reentered. Try again")
                        continue
                
                
def checkcross(game) :
        if (game['topleft'] == game['midmid'] == game['lowright'] and (game['topleft'] == 'O' or game['topleft'] == 'X')) or (game['topright'] == game['midmid'] == game['lowleft'] and (game['topright'] == 'O' or game['topright'] == 'X')) :
                return True

def checkcolumn(game) :
        if (game['topleft'] == game['midleft'] == game['lowleft'] and (game['topleft'] == 'O' or game['topleft'] == 'X')) or (game['topmid'] == game['midmid'] == game['lowmid'] and (game['topmid'] == 'O' or game['topmid'] == 'X')) or (game['topright'] == game['midright'] == game['lowright'] and (game['topright'] == 'O' or game['topright'] == 'X')) :
                return True

def checkrow(game) :
        if (game['topleft'] == game['topmid'] == game['topright'] and (game['topleft'] == 'O' or game['topleft'] == 'X')) or (game['midleft'] == game['midmid'] == game['midright'] and (game['midleft'] == 'O' or game['midleft'] == 'X')) or (game['lowleft'] == game['lowright'] == game['lowmid'] and (game['lowleft'] == 'O' or game['lowleft'] == 'X')) :
                return True
               

   
def checkwin() :
        global gamerunner
        global winner
        if checkcross(game) or checkcolumn(game) or checkrow(game) :
                winner = currentplayer
                print("Winner: " + winner)
                gamerunner = False
    
    
def checktie(game) :
        global gamerunner
        if (game['topleft'] != ' ') and (game['topmid'] != ' ') and (game['topright'] != ' ') and (game['midleft'] != ' ') and (game['midmid'] != ' ') and (game['midright'] != ' ') and (game['lowleft'] != ' ') and (game['lowmid'] != ' ') and (game['lowright'] != ' ') and checkcross(game) != True :
                print("It's a tie")
                gamerunner = False
                
        
        
               
    
def switchplayer() : 
        global currentplayer
        if currentplayer == 'X':
                currentplayer = 'O'
        elif currentplayer == 'O' :
                currentplayer = 'X'
    
def main() :
        print("Welcome to tictactoe")

if __name__ == "__main__" :
        main()
        while gamerunner :
            printgame(game)
            gameplay(game)
            checkwin()
            checktie(game)
            switchplayer()
        printgame(game)


        
       
        

        

    
