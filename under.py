import random
import numpy
import json

board=numpy.zeros((4,4))
with open("GameBoard.json", "w") as outfile: 
    outfile.write(json.dumps(board.tolist()))




class Data():
    def __init__(self):
        with open("GameBoard.json", "r") as outfile: 
            self.board=numpy.array( json.loads(outfile.read()))
            self.offset=(200,100)
            print("wczytane")





print(board)
Data()
