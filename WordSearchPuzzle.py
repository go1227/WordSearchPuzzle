__author__ = "Guilherme Ortiz"
__version__ = "1.0"
__date_last_modification__ = "12/13/2018"
__python_version__ = "1"


import numpy as np
import random
import string


#During development time, it's best to print out '-' so you can see the empty spots of the array
def random_generator(size, chars):
    return ''.join(random.choice(chars) for x in range(size))
    #return '-'

#Creates the board with the sized defined via parameter
def make_board(boardsize):
    for j in range(0, boardsize):
        tmp = []
        for i in range(0, boardsize):
            tmp.append(random_generator(1, string.ascii_uppercase))
        board.append(tmp)
    return(np.array(board))


#this function is very handy to print the array in a clean fashion
def printArrayNoComma(arr):
    line = ''
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            line = line + arr[i][j] + '  '
        print(line)
        line = ''
    print('\n')

def write_word(tmp_array, word, orientation): #left to right / right to left
    if (orientation == 'RIGHT_TO_LEFT' or orientation == 'BOTTOM_TO_TOP'):
        word = word[::-1]
    used_starting_points = []
    candidate_list = []

    #check all available spots. If no good available spot is found, don't use the word in the board
    for n in range(0, len(tmp_array)**2):
        #get random starting point
        startline = random.randint(0,len(tmp_array)-1)
        startcolumn = random.randint(0,len(tmp_array)-1)
        curr_pos = (startline, startcolumn)

        if (curr_pos not in used_starting_points and curr_pos not in spotsinuse):
            if (orientation == 'RIGHT_TO_LEFT' or orientation == 'LEFT_TO_RIGHT'):
                start = startcolumn
            else:
                start = startline
            end = len(tmp_array)
            candidate_list.clear()
            if (int(end - start) >= int(len(word))): #this checks if the word fits in the upcoming slots
                for pos in range(0, len(word)):
                    if (orientation == 'RIGHT_TO_LEFT' or orientation == 'LEFT_TO_RIGHT'):
                        next_pos = (startline, startcolumn + pos)
                    else:
                        next_pos = (startline + pos, startcolumn)
                    if (next_pos not in spotsinuse):
                        candidate_list.append((next_pos))
                    else:
                        candidate_list.clear()
                        break

            if (len(candidate_list) == len(word)):
                for i in candidate_list:
                    spotsinuse.add(i)
                #if at the end of the entire FOR loop 'perfect_fit' remains True, use this spot for this word
                #use positions from candidate_list into tmp_array
                t = 0
                for x in candidate_list:
                    tmp_array[int(x[0])][int(x[1])] = word[t]
                    t += 1
                break
    return tmp_array


bsize = 15
spotsinuse = set()
board = []

#Create basic board, containing only random letters (A-Z)
board = make_board(bsize)

write_options = ['BOTTOM_TO_TOP','TOP_TO_BOTTOM','LEFT_TO_RIGHT','RIGHT_TO_LEFT']
list_of_words = ['CLOCK','LIST','BOOKS','GREEN','CANDLE','XEROX']
random.shuffle(list_of_words)

print('\nWords to look for:')
for item in list_of_words:
    print(item)
    write_word(board,item,random.choice(write_options))

print('\n')
printArrayNoComma(board)
