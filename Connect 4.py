#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Board():
    def __init__(self, cols=7, rows=6):
        self.cols=cols
        self.rows=rows
        self.data=[[' ' for i in range(self.cols)] for i in range (self.rows)]
    def __str__(self):
        s=''
        for i in range(self.rows):
            for j in range(self.cols):
                s=s+'|'
                s=s+self.data[i][j]
            s=s+'|\n'
        s=s+'---------------\n 0 1 2 3 4 5 6 \n'
        return s
    def is_valid_move(self, col):
        if col>=0 and col<=6 and self.data[0][col]==' ':
            return True
        else:
            return False
    
    def add_marker(self, col, marker):
        for i in range(self.rows-1,-1,-1):
            if self.data[i][col]==' ':
                self.data[i][col]=marker
                break
            else:
                continue
            
    def del_marker(self, col):
        for i in range(self.rows):
            if self.data[i][col]=='X' or self.data[i][col]=='O':
                self.data[i][col]=' '
                break
    def reset_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j]=' '

    def set_board(self, cols, marker):
        board.reset_board()
        if marker=='X':
            judge=0
            for i in cols:
                if judge%2==0:
                    board.add_marker(int(i),'X')
                if judge%2==1:
                    board.add_marker(int(i),'O')
                judge+=1
        if marker=='O':
            judge=0
            for i in cols:
                if judge%2==0:
                    self.add_marker(int(i),'O')
                if judge%2==1:
                    self.add_marker(int(i),'X')
                judge+=1
    
    def is_full(self):
        count=0
        for i in range(self.cols):
            if self.data[0][i] != ' ':
                count+=1
        if count==7:
            return True
        else:
            return False
    
    def is_winner(self, marker):
        count=0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j]==marker:
                    if i-3>=0 and self.data[i-1][j]==marker and self.data[i-2][j]==marker and self.data[i-3][j]==marker:
                        count+=1
                    if i-2>=0 and i+1<=5 and self.data[i+1][j]==marker and self.data[i-1][j]==marker and self.data[i-2][j]==marker:
                        count+=1
                    if i-1>=0 and i+2<=5 and self.data[i-1][j]==marker and self.data[i+1][j]==marker and self.data[i+2][j]==marker:
                        count+=1
                    if i+3<=5 and self.data[i+1][j]==marker and self.data[i+2][j]==marker and self.data[i+3][j]==marker:
                        count+=1
                    #verticle
                    if j+3<=6 and self.data[i][j+1]==marker and self.data[i][j+2]==marker and self.data[i][j+3]==marker:
                        count+=1
                    if j+2<=6 and j-1>=0 and self.data[i][j+1]==marker and self.data[i][j+2]==marker and self.data[i][j-1]==marker:
                        count+=1
                    if j+1<=6 and j-2>=0 and self.data[i][j+1]==marker and self.data[i][j-1]==marker and self.data[i][j-2]==marker:
                        count+=1
                    if j-3>=0 and self.data[i][j-1]==marker and self.data[i][j-2]==marker and self.data[i][j-3]==marker:
                        count+=1
                    #horizental
                    if i-3>=0 and j+3<=6 and self.data[i-1][j+1]==marker and self.data[i-2][j+2]==marker and self.data[i-3][j+3]==marker:
                        count+=1
                    if i-2>=0 and j+2<=6 and i+1<=5 and j-1>=0 and self.data[i-1][j+1]==marker and self.data[i-2][j+2]==marker and self.data[i+1][j-1]==marker:
                        count+=1
                    if i-1>=0 and j+1<=6 and i+2<=5 and j-2>=0 and self.data[i-1][j+1]==marker and self.data[i+1][j-1]==marker and self.data[i+2][j-2]==marker:
                        count+=1
                    if i+3<=5 and j-3>=0 and self.data[i+1][j-1]==marker and self.data[i+2][j-2]==marker and self.data[i+3][j-3]==marker:
                        count+=1
                    if i+3<=5 and j+3<=6 and self.data[i+1][j+1]==marker and self.data[i+2][j+2]==marker and self.data[i+3][j+3]==marker:
                        count+=1
                    if i+2<=5 and i-1>=0 and j+2<=6 and j-1>=0 and self.data[i+1][j+1]==marker and self.data[i+2][j+2]==marker and self.data[i-1][j-1]==marker:
                        count+=1
                    if i+1<=5 and i-2>=0 and j+1<=6 and j-2>=0 and self.data[i+1][j+1]==marker and self.data[i-1][j-1]==marker and self.data[i-2][j-2]==marker:
                        count+=1
                    if i-3>=0 and j-3>=0 and self.data[i-1][j-1]==marker and self.data[i-2][j-2]==marker and self.data[i-3][j-3]==marker:
                        count+=1
        if count==0:
            return False
        else:
            return True
import random
class Player():
    def __init__(self, marker, kind, strategy='RAND', level=0):
        self.kind=kind
        self.marker=marker
        self.strategy=strategy
        self.level=level
    def __str__(self):
        if self.kind=='HUMAN':
            return 'HUMAN ('+self.marker+')'
        else:
            return 'AI ('+self.marker+'): '+self.strategy+', lvl: '+str(self.level)
    def human_move(self, board):
        while True:
            try:
                a=int(input('Please enter which column you want to move: '))
                board.add_marker(a,self.marker)
                break
            except:
                print('Invalid input, please try again: ')
    
    def choose_move(self, scores):
        L=[]
        for i in range(len(scores)):
            if scores[i]==max(scores):
                L.append(i)
        if self.strategy=='LEFT':
            return L[0]
        if self.strategy=='RIGHT':
            return L[-1]
        if self.strategy=='RAND':
            return L[random.randint(0,len(L)-1)]
    
    def get_move_scores(self, board):
        # YOUR CODE HERE
        def compS(nowbroad,mark,lv):
            if mark=='X':
                p1,p2='X','O'
            else:
                p1,p2='O','X'
            ans=[]
            
            for i in range(len(board.data[0])):
                if board.data[0][i]!=' ':
                    ans.append(-1.0)
                else:
                    if lv==0:
                        if board.is_winner(p1)==True:
                            ans.append(1.0)
                        elif board.is_winner(p2)==True:
                            ans.append(0.0)
                        else:
                            ans.append(0.5)
                    else:
                        board.add_marker(i,p1)
                        new=1-max(compS(board,p2,lv-1))
                        ans.append(new)
                        board.del_marker(i)
            return ans
        
        return compS(board,self.marker,self.level)

    
    def AI_move(self, board):
        # YOUR CODE HERE
        scorelist=self.get_move_scores(board)
        return self.choose_move(scorelist)

    def next_move(self, board):
        # YOUR CODE HERE
        board.add_marker(self.AI_move(board),self.marker)
class Game():
    def __init__(self, cols, rows, p1, p2):
        # YOUR CODE HERE
        self.board=Board(cols,rows)
        self.p1=p1
        self.p2=p2
        
    def __str__(self):
        # YOUR CODE HERE
        return self.board.__str__()+'\n1: '+self.p1.__str__()+'\n2: '+self.p2.__str__()+'\n'
    
    def play(self, display=True):
        count = 0
        while True:
            if self.p1.kind == 'HUMAN':
                self.p1.human_move(self.board)
            else:
                self.p1.next_move(self.board)
            count += 1
            if display:
                print(self.board)
            if self.board.is_winner(self.p1.marker):
                return (1, count)
            if self.board.is_full():
                return (0, count)

            if self.p2.kind == 'HUMAN':
                self.p2.human_move(self.board)
            else:
                self.p2.next_move(self.board)
            count += 1
            if display:
                print(self.board)
            if self.board.is_winner(self.p2.marker):
                return (-1, count)
            if self.board.is_full():
                return (0, count)
print("Welcome to play connect 4")
print("-1 means the 1st player wins, -1 means the 2nd player wins.O means ended in a draw! The last number means the total step")
print("Play alone or with a friend? if alone, type 1, otherwise 2")
mode=int(input())
if mode==1:
    difficulty=int(input("Enter the difficulty, from 1 to 3, 1 is easy, 2 is normal, 3 is hard"))
    print("You wanna to be first or second? if first type 1, otherwise 2")
    submode=int(input())
    if submode==1:
        print("Your marker is O, Let's start!")
        g = Game(7, 6, Player('O', 'HUMAN'), Player('X', 'AI', 'RAND', difficulty))
    else:
        print("Your marker is X, Let's start!")
        g = Game(7,6,Player('X','AI','RAND',difficulty),Player('O','HUMAN'))
else:
    print("1st player's marker is X, 2nd player's marker is O. Let's start!")
    g = Game(7, 6, Player('O', 'HUMAN'), Player('X', 'HUMAN'))
#g = Game(7,6,Player('X','AI','RAND',difficulty),Player('O','HUMAN'))
# Create the Game object with the human player ('O') going first
#g = Game(7, 6, Player('O', 'HUMAN'), Player('X', 'AI', 'RAND', 2))
g.play()

