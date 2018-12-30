
def DisplayBoard(B):
    print("\033[H\033[J")
    print(f"        |          |        ")
    print("˜˜˜˜˜˜˜˜|˜˜˜˜˜˜˜˜˜˜|˜˜˜˜˜˜˜˜")
    print(f"        |          |        \n    {B[7]}   |    {B[8]}     |    {B[9]}   ")
    print("˜˜˜˜˜˜˜˜|˜˜˜˜˜˜˜˜˜˜|˜˜˜˜˜˜˜˜")
    print(f"        |          |        \n    {B[4]}   |    {B[5]}     |    {B[6]}   ")
    print("˜˜˜˜˜˜˜˜|˜˜˜˜˜˜˜˜˜˜|˜˜˜˜˜˜˜˜")
    print(f"        |          |        \n    {B[1]}   |    {B[2]}     |    {B[3]}   ")
    print("        |          |        ")
    print("˜˜˜˜˜˜˜˜|˜˜˜˜˜˜˜˜˜˜|˜˜˜˜˜˜˜˜")

def Player_input():
    marker=''
    while not (marker=='X' or marker=='0'):
        marker=input("Player 1: Do you wanna be '0' or 'X'").upper()
    if marker=='X':
        return ('X','0')
    else:
        return ('0','X')

def Place_marker(B,marker,position):
    B[position]=marker

def Win_check(B,mark):
    return (B[7]==mark and B[8]==mark and B[9]==mark) or (B[4]==mark and B[5]==mark and B[6]==mark) or (B[1]==mark and B[2]==mark and B[3]==mark) or (B[1]==mark and B[4]==mark and B[7]==mark) or (B[2]==mark and B[5]==mark and B[8]==mark) or (B[3]==mark and B[6]==mark and B[9]==mark) or (B[1]==mark and B[5]==mark and B[9]==mark) or (B[3]==mark and B[5]==mark and B[7]==mark)

def Choose_first():
    import random
    if random.randint(0,1)==0:
        return 'Player 1'
    else:
        return playerId

def Space_check(B,position):
    if B[position] in '1 2 3 4 5 6 7 8 9'.split():
        return True

def full_board_check(B):
    for i in range(1,10):
        if Space_check(B,i):
            return False
    return True

def Computer_choice(B,m1,m2):
        import random
        position=0
        while not Space_check(B,position):
            if level=='E':# all diagonals and board no 1,3,5,7,9 in defence
                
                #All possible matchings algorithm
                
                if (B[2]==m2 and B[3]==m2 and Space_check(B,1)==True) or (B[4]==m2 and B[7]==m2 and Space_check(B,1)==True) or (B[5]==m2 and B[9]==m2 and Space_check(B,1)==True):
                    position=1
                elif (B[1]==m2 and B[3]==m2 and Space_check(B,2)==True) or (B[5]==m2 and B[8]==m2 and Space_check(B,2)==True):
                    position=2
                elif (B[1]==m2 and B[2]==m2 and Space_check(B,3)==True) or (B[6]==m2 and B[9]==m2 and Space_check(B,3)==True) or (B[5]==m2 and B[7]==m2 and Space_check(B,3)==True):
                    position=3
                elif (B[1]==m2 and B[7]==m2 and Space_check(B,4)==True) or (B[5]==m2 and B[6]==m2 and Space_check(B,4)==True):
                    position=4
                elif (B[1]==m2 and B[9]==m2 and Space_check(B,5)==True) or (B[3]==m2 and B[7]==m2 and Space_check(B,5)==True) or (B[2]==m2 and B[8]==m2 and Space_check(B,5)==True) or (B[4]==m2 and B[6]==m2 and Space_check(B,5)==True):
                    position=5             
                elif (B[3]==m2 and B[9]==m2 and Space_check(B,6)==True) or (B[4]==m2 and B[5]==m2 and Space_check(B,6)==True):
                    position=6
                elif (B[1]==m2 and B[4]==m2 and Space_check(B,7)==True) or (B[8]==m2 and B[9]==m2 and Space_check(B,7)==True) or (B[3]==m2 and B[5]==m2 and Space_check(B,7)==True):
                    position=7            
                elif (B[7]==m2 and B[9]==m2 and Space_check(B,8)==True) or (B[2]==m2 and B[5]==m2 and Space_check(B,8)==True):
                    position=8
                elif (B[7]==m2 and B[8]==m2 and Space_check(B,9)==True) or (B[1]==m2 and B[5]==m2 and Space_check(B,9)==True) or (B[3]==m2 and B[6]==m2 and Space_check(B,9)==True):
                    position=9
                
                #Defensive algorithms below
                
                elif (B[1]==m1 and B[3]==m1 and Space_check(B,2)==True) or (B[5]==m1 and B[8]==m1 and Space_check(B,2)==True):
                    position=2        
                elif (B[1]==m1 and B[2]==m1 and Space_check(B,3)==True) or (B[5]==m1 and B[7]==m1 and Space_check(B,3)==True) or (B[6]==m1 and B[9]==m1 and Space_check(B,3)==True):
                    position=3
                elif (B[1]==m1 and B[7]==m1 and Space_check(B,4)==True) or (B[5]==m1 and B[6]==m1 and Space_check(B,4)==True):
                    position=4    
                elif (B[2]==m1 and B[8]==m1 and Space_check(B,5)==True) or (B[4]==m1 and B[6]==m1 and Space_check(B,5)==True) or (B[1]==m1 and B[9]==m1 and Space_check(B,5)==True) or (B[3]==m1 and B[7]==m1 and Space_check(B,5)==True):
                    position=5
                elif (B[3]==m1 and B[9]==m1 and Space_check(B,6)==True) or (B[4]==m1 and B[5]==m1 and Space_check(B,6)==True):
                    position=6                   
                elif (B[7]==m1 and B[9]==m1 and Space_check(B,8)==True) or (B[2]==m1 and B[5]==m1 and Space_check(B,8)==True):
                    position=8               
                elif (B[7]==m1 and B[8]==m1 and Space_check(B,9)==True) or (B[1]==m1 and B[5]==m1 and Space_check(B,9)==True) or (B[3]==m1 and B[6]==m1 and Space_check(B,9)==True):
                    position=9                                
               
                else:        
                    position=random.randint(1,9)        
            if level=='M': # all diagonal and Board no 2,3,4,6,8,9 firewalls and matching ability with all 
                
                # All possible matchings algorithms below
                
                if (B[2]==m2 and B[3]==m2 and Space_check(B,1)==True) or (B[4]==m2 and B[7]==m2 and Space_check(B,1)==True) or (B[5]==m2 and B[9]==m2 and Space_check(B,1)==True):
                    position=1
                elif (B[1]==m2 and B[3]==m2 and Space_check(B,2)==True) or (B[5]==m2 and B[8]==m2 and Space_check(B,2)==True):
                    position=2
                elif (B[1]==m2 and B[2]==m2 and Space_check(B,3)==True) or (B[6]==m2 and B[9]==m2 and Space_check(B,3)==True) or (B[5]==m2 and B[7]==m2 and Space_check(B,3)==True):
                    position=3
                elif (B[1]==m2 and B[7]==m2 and Space_check(B,4)==True) or (B[5]==m2 and B[6]==m2 and Space_check(B,4)==True):
                    position=4
                elif (B[1]==m2 and B[9]==m2 and Space_check(B,5)==True) or (B[3]==m2 and B[7]==m2 and Space_check(B,5)==True) or (B[2]==m2 and B[8]==m2 and Space_check(B,5)==True) or (B[4]==m2 and B[6]==m2 and Space_check(B,5)==True):
                    position=5             
                elif (B[3]==m2 and B[9]==m2 and Space_check(B,6)==True) or (B[4]==m2 and B[5]==m2 and Space_check(B,6)==True):
                    position=6
                elif (B[1]==m2 and B[4]==m2 and Space_check(B,7)==True) or (B[8]==m2 and B[9]==m2 and Space_check(B,7)==True) or (B[3]==m2 and B[5]==m2 and Space_check(B,7)==True):
                    position=7            
                elif (B[7]==m2 and B[9]==m2 and Space_check(B,8)==True) or (B[2]==m2 and B[5]==m2 and Space_check(B,8)==True):
                    position=8
                elif (B[7]==m2 and B[8]==m2 and Space_check(B,9)==True) or (B[1]==m2 and B[5]==m2 and Space_check(B,9)==True) or (B[3]==m2 and B[6]==m2 and Space_check(B,9)==True):
                    position=9
                
                #Defensive algorithm here below
                
                elif (B[2]==m1 and B[3]==m1 and Space_check(B,1)==True) or (B[5]==m1 and B[9]==m1 and Space_check(B,1)==True) or (B[4]==m1 and B[7]==m1 and Space_check(B,1)==True):
                    position=1
                elif (B[1]==m1 and B[3]==m1 and Space_check(B,2)==True) or (B[5]==m1 and B[8]==m1 and Space_check(B,2)==True):
                    position=2
                elif (B[1]==m1 and B[2]==m1 and Space_check(B,3)==True) or (B[5]==m1 and B[7]==m1 and Space_check(B,3)==True) or (B[6]==m1 and B[9]==m1 and Space_check(B,3)==True):
                    position=3
                elif (B[1]==m1 and B[7]==m1 and Space_check(B,4)==True) or (B[5]==m1 and B[6]==m1 and Space_check(B,4)==True):
                    position=4
                elif (B[2]==m1 and B[8]==m1 and Space_check(B,5)==True) or (B[4]==m1 and B[6]==m1 and Space_check(B,5)==True) or (B[1]==m1 and B[9]==m1 and Space_check(B,5)==True) or (B[3]==m1 and B[7]==m1 and Space_check(B,5)==True):
                    position=5
                elif (B[3]==m1 and B[9]==m1 and Space_check(B,6)==True) or (B[4]==m1 and B[5]==m1 and Space_check(B,6)==True):
                    position=6
                elif (B[1]==m1 and B[4]==m1 and Space_check(B,7)==True) or (B[3]==m1 and B[5]==m1 and Space_check(B,7)==True) or (B[8]==m1 and B[9]==m1 and Space_check(B,7)==True):
                    position=7
                elif (B[7]==m1 and B[9]==m1 and Space_check(B,8)==True) or (B[2]==m1 and B[5]==m1 and Space_check(B,8)==True):
                    position=8
                elif (B[7]==m1 and B[8]==m1 and Space_check(B,9)==True) or (B[1]==m1 and B[5]==m1 and Space_check(B,9)==True) or (B[3]==m1 and B[6]==m1 and Space_check(B,9)==True):
                    position=9
                
                #anti-ssuper trick
                elif (B[2]!=m2 and B[3]==m1 and Space_check(B,7)==True) or (B[6]!=m2 and B[3]==m1 and Space_check(B,7)==True):
                    position=7
                else:        
                    position=random.randint(1,9)        
                    
            if level=='T': # Every possible chances blocked except one diagonal other than main plus contains anti-super tricks
                
                # All possible matchings algorithm
                
                if (B[2]==m2 and B[3]==m2 and Space_check(B,1)==True) or (B[4]==m2 and B[7]==m2 and Space_check(B,1)==True) or (B[5]==m2 and B[9]==m2 and Space_check(B,1)==True):
                    position=1
                elif (B[1]==m2 and B[3]==m2 and Space_check(B,2)==True) or (B[5]==m2 and B[8]==m2 and Space_check(B,2)==True):
                    position=2
                elif (B[1]==m2 and B[2]==m2 and Space_check(B,3)==True) or (B[6]==m2 and B[9]==m2 and Space_check(B,3)==True) or (B[5]==m2 and B[7]==m2 and Space_check(B,3)==True):
                    position=3
                elif (B[1]==m2 and B[7]==m2 and Space_check(B,4)==True) or (B[5]==m2 and B[6]==m2 and Space_check(B,4)==True):
                    position=4
                elif (B[1]==m2 and B[9]==m2 and Space_check(B,5)==True) or (B[3]==m2 and B[7]==m2 and Space_check(B,5)==True) or (B[2]==m2 and B[8]==m2 and Space_check(B,5)==True) or (B[4]==m2 and B[6]==m2 and Space_check(B,5)==True):
                    position=5             
                elif (B[3]==m2 and B[9]==m2 and Space_check(B,6)==True) or (B[4]==m2 and B[5]==m2 and Space_check(B,6)==True):
                    position=6
                elif (B[1]==m2 and B[4]==m2 and Space_check(B,7)==True) or (B[8]==m2 and B[9]==m2 and Space_check(B,7)==True) or (B[3]==m2 and B[5]==m2 and Space_check(B,7)==True):
                    position=7            
                elif (B[7]==m2 and B[9]==m2 and Space_check(B,8)==True) or (B[2]==m2 and B[5]==m2 and Space_check(B,8)==True):
                    position=8
                elif (B[7]==m2 and B[8]==m2 and Space_check(B,9)==True) or (B[1]==m2 and B[5]==m2 and Space_check(B,9)==True) or (B[3]==m2 and B[6]==m2 and Space_check(B,9)==True):
                    position=9
                
                #Defensive algorithm here below
                
                elif (B[2]==m1 and B[3]==m1 and Space_check(B,1)==True) or (B[5]==m1 and B[9]==m1 and Space_check(B,1)==True) or (B[4]==m1 and B[7]==m1 and Space_check(B,1)==True):
                    position=1
                elif (B[1]==m1 and B[3]==m1 and Space_check(B,2)==True) or (B[5]==m1 and B[8]==m1 and Space_check(B,2)==True):
                    position=2
                elif (B[1]==m1 and B[2]==m1 and Space_check(B,3)==True) or (B[5]==m1 and B[7]==m1 and Space_check(B,3)==True) or (B[6]==m1 and B[9]==m1 and Space_check(B,3)==True):
                    position=3
                elif (B[1]==m1 and B[7]==m1 and Space_check(B,4)==True) or (B[5]==m1 and B[6]==m1 and Space_check(B,4)==True):
                    position=4
                elif (B[2]==m1 and B[8]==m1 and Space_check(B,5)==True) or (B[4]==m1 and B[6]==m1 and Space_check(B,5)==True) or (B[1]==m1 and B[9]==m1 and Space_check(B,5)==True) or (B[3]==m1 and B[7]==m1 and Space_check(B,5)==True):
                    position=5
                elif (B[3]==m1 and B[9]==m1 and Space_check(B,6)==True) or (B[4]==m1 and B[5]==m1 and Space_check(B,6)==True):
                    position=6
                elif (B[1]==m1 and B[4]==m1 and Space_check(B,7)==True) or (B[3]==m1 and B[5]==m1 and Space_check(B,7)==True) or (B[8]==m1 and B[9]==m1 and Space_check(B,7)==True):
                    position=7
                elif (B[7]==m1 and B[9]==m1 and Space_check(B,8)==True) or (B[2]==m1 and B[5]==m1 and Space_check(B,8)==True):
                    position=8
                elif (B[7]==m1 and B[8]==m1 and Space_check(B,9)==True) or (B[1]==m1 and B[5]==m1 and Space_check(B,9)==True) or (B[3]==m1 and B[6]==m1 and Space_check(B,9)==True):
                    position=9
                    
                #Super tricks detector and destroyer algorithm below
                
                elif (B[2]!=m2 and B[1]==m1 and Space_check(B,5)==True) or (B[4]!=m2 and B[1]==m1 and Space_check(B,5)==True) or (B[9]!=m2 and B[1]==m1 and Space_check(B,5)==True):
                    position=5
                elif (B[4]!=m2 and B[7]==m1 and Space_check(B,5)==True) or (B[8]!=m2 and B[7]==m1 and Space_check(B,5)==True) or (B[3]!=m2 and B[7]==m1 and Space_check(B,5)==True):
                    position=5                
                elif (B[2]!=m2 and B[3]==m1 and Space_check(B,7)==True) or (B[6]!=m2 and B[3]==m1 and Space_check(B,7)==True):
                    position=7
                elif (B[8]!=m2 and B[9]==m1 and Space_check(B,1)==True) or (B[6]!=m2 and B[9]==m1 and Space_check(B,1)==True):
                    position=1
                else:
                    position=random.randint(1,9)
        return position 
    
def Player_choice(B):
    position=''
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not Space_check(B,int(position)):
        position=input("Choose your next position (1-9)\n")
    return int(position)

def replay():
    return input("Do you wanna continue to play? Enter yes or No\n").lower().startswith('y')
    
def levelchange():
    print("\nSelect the difficulty level")
    lvl=input("E-->Easy/ M-->medium/ T-->tough ").upper()    
    return lvl
        

 #The game starts from here

import androidhelper
droid = androidhelper.Android()
droid.ttsSpeak("Welcome to Tic Tac Toe!!!!\n")
player1_score=0
player2_score=0
level=''
print("Welcome to Tic Tac Toe!!!!\n")
playerId=''
droid.ttsSpeak("Please choose the Game mode:")
print("Please choose the Gamemode: ")
droid.ttsSpeak("Either play with Computer or with your friend?")
mode=input("1-->Play with Computer?\n2-->Play with your friend\n")
if mode=='1':
    playerId='Computer'
    droid.ttsSpeak("Select the difficulty level! Either Easy or Medium or Tough ?")
    level=levelchange()
else:
    playerId='Player 2'
while True:
  
    #board=['']*10
    board=['0','1','2','3','4','5','6','7','8','9']
    droid.ttsSpeak("Player 1 Choose either 0 or cross")
    Player1_marker,Player2_marker=Player_input()
    turn=Choose_first()
    droid.ttsSpeak(turn + " will go first")
    print(turn + " will go first")
    game_on=True
    while game_on:
        if turn=='Player 1':            
            DisplayBoard(board)
            droid.ttsSpeak("Player 1 turn:")
            print(f"Player 1:{Player1_marker}")
            position=Player_choice(board)
            droid.ttsSpeak(f"Position {position} choosen!")
            Place_marker(board,Player1_marker,position)
            if Win_check(board,Player1_marker):
                player1_score+=1
                DisplayBoard(board)
                droid.ttsSpeak("Congratulations! Player 1 won the game")
                print("Congratulations! Player 1 won the game")
                game_on=False
            else:
                if full_board_check(board):
                    DisplayBoard(board)
                    droid.ttsSpeak("Game draw")
                    print("The game ends in a Draw!!")
                    break
                else:
                    turn='Player 2'
                    
        else:   #for player 2 (Computer)          
            DisplayBoard(board)
            let=''
            if mode=='1' and let!='n':
                droid.ttsSpeak(f"Its {playerId} turn!")
                print("Its computer's turn now!")
                let=input(f"Press Enter to let computer set next position:{Player2_marker}")
                position=Computer_choice(board,Player1_marker,Player2_marker)
                droid.ttsSpeak(f"Position {position} choosen!")
            else:
                droid.ttsSpeak(f"{playerId} turn:")
                print(f"Player 2:{Player2_marker} ")
                position=Player_choice(board)
                droid.ttsSpeak(f"Position {position} choosen!")
            Place_marker(board,Player2_marker,position)
            if Win_check(board,Player2_marker):
                player2_score+=1
                DisplayBoard(board)                        
                droid.ttsSpeak(f"Congratulations! {playerId} won the game")
                print(f"Congratulations! {playerId} won the game")
                game_on=False
            else:
                if full_board_check(board):
                    DisplayBoard(board)
                    droid.ttsSpeak("Game Draw")
                    print("The game ends in a Draw!!")
                    break
                else:
                    turn='Player 1'
                                    
    if not replay():
        print(f"Total score of Player 1: {player1_score}")
        print(f"Total score of Player 1: {player2_score}")
        if player1_score > player2_score:
            droid.ttsSpeak("Player 1 is the winner from the entire game")
            print("Player 1 is the winner from the entire game")
        elif player1_score < player2_score:
            droid.ttsSpeak(f"{playerId} is the winner from the entire game")
            print(f"{playerId} is the winner from the entire game")
        else:
            droid.ttsSpeak("Both of you share the equal scores. So both of you are winner!!!")
            print("Both of you share the equal scores. So both of you are winner!!!")
        break