__author__ = "Guilherme Ortiz"
__version__ = "1.2"
__date_last_modification__ = "1/4/2019"


import numpy as np
import random
import string
import time
from urllib.request import urlopen


#Program that pulls from the web random words and make them available in the puzzle for the user to search for words.

#Step 1: Ask user how many words should the program use in the game (min. 1, max 10)
words_qty = -1
valid_entry = False
while valid_entry is False:
    words_qty = input("\nHow many words would you like to search in the puzzle? [min 1, max 10]:\n")
    if words_qty.isdigit():
        if int(words_qty) >= 1 and int(words_qty) <= 10:
            valid_entry = True
    else:
        print("This is an invalid number. Try again.")


#Step 2: Gather words from web (or use hard-coded option if web attempt fails)
siteokay = False

backup_words = []
file = open("backupwords.txt", "r")
for line in file:
    line = line.strip('\n').upper()
    backup_words.append(line)
file.close()

list_of_words = set() #this set  will contain the FINAL list of words to be used in the game.


#the auto words web search should abort automatically if web is not responding after 30 seconds
time.perf_counter()

print("\nPlease wait...")
while int(words_qty) > len(list_of_words):
    link = "http://jimpix.co.uk/generators/word-generator.asp"
    try:
        f = urlopen(link)
        myfile = str(f.read())
        siteokay = True
    except:
        siteokay = False

    if siteokay:
        is_eligible_word = False
        result = myfile.find("&bull;")  # We must find at least one bullet point, because that's where the key words are.
        tmp = str(myfile[result - 12:result]).rstrip().lstrip()

        #print("Checking this string... [" + tmp + "]")

        random_word = ''
        if (tmp.find(">") != -1):
            gt_position = tmp.find(">")
            random_word = tmp[gt_position + 1:].upper()
            if len(random_word) >= 3 and len(random_word) <= 10:
                is_eligible_word = True

        if round(time.perf_counter()) < 30 and is_eligible_word == True:
            #use the word found online: it meets the criteria
            list_of_words.add(random_word)
        else:
            random_word = random.choice(backup_words)
            list_of_words.add(random_word)




#Step 3: Distribute the words in the game board.


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

print('\nWords to look for:')
for item in list_of_words:
    print(item)
    write_word(board,item,random.choice(write_options))

print('\n')
printArrayNoComma(board)
