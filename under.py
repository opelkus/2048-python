import random
import numpy
import json

board=numpy.zeros((4,4))
with open("GameBoard.json", "w") as outfile: 
    outfile.write(json.dumps(board.tolist()))



def gen_psy(board):
    for i in range(4):
        for j in range(4):
            if board[i][j]==0:
                board[i][j]=random.randint(1,2)
    return board


class Data():
    def __init__(self):
        with open("GameBoard.json", "r") as outfile: 
            self.board=numpy.array( json.loads(outfile.read()))
            self.offset=(200,100)
            if not self.board.any():
                self.gen_klocki()
                self.gen_klocki()
            print(self.board)
            print("wczytane")
    def gen_klocki(self):
        self.klocki=[2,2,2,4]
        puste=list(zip(numpy.where(board==0)[0],numpy.where(board==0)[1]))
        if len(puste)>0:
            x,y=random.choice(puste)
            board[x][y]=random.choice(self.klocki)
            with open("GameBoard.json", "w") as outfile: 
                outfile.write(json.dumps(board.tolist()))
            print(board)
        else:
            self.koniec=True





print(board)
Data()
