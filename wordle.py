import requests
import random

max_tries = 6
word_length = 5
game_board = [['*'] * 5 for i in range(max_tries)]
keyboard = [
    {'Q':'q', 'W':'w', 'E':'e', 'R':'r', 'T':'t', 'Y':'y', 'U':'u', 'I':'i', 'O':'o', 'P':'p'},
    {'A':'a', 'S':'s', 'D':'d', 'F':'f', 'G':'g',  'H':'h', 'J':'j', 'K':'k', 'L':'l'}, 
    {'Z':'z', 'X':'x', 'C':'c', 'V':'v', 'B':'b', 'N':'n', 'M':'m'}
]

def getFiveLetterWords():
    global five_letter_words
    headers = {
        'authority': 'raw.githubusercontent.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '^\\^',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '^\\^Windows^\\^',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.google.com/',
        'accept-language': 'en-US,en;q=0.9',
        'if-none-match': 'W/^\\^b895f6094906d86db93e4b808e8006e1a0de58fde7cd24b412eab3562d0a00fc^\\^',
    }

    response = requests.get('https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt', headers=headers)
    five_letter_words = response.text.split('\n')

def isValidWord(word):
    if len(word) != word_length:
        return False
    if word not in five_letter_words:
        return False
    return True

def updateGameBoard(word):
    for i in range(0,5):
        if word[i] in correct_word:
            letter = word[i].upper()
            if word[i] != correct_word[i]:
                letter = letter.lower()
        else:
            letter = '*'
        game_board[6-max_tries][i] = letter

def updateKeyboard(word):
    for i in range(0,5):
        if word[i] in correct_word:
            key = word[i].upper()
            if word[i] != correct_word[i]:
                key = word[i].lower()
        else:
            key = '*'
        letter = word[i].upper()
        for r in keyboard:
            if letter in r:
                r[letter] = key
                break
	    
def printGameBoard():
    print('\n----Game Board----')

    for r in game_board:
        print(''.join(r))

def printKeyboard():
    print('\n----Key Board-----')

    for r in keyboard:
        print(' '.join(r.values()))
    
def main():
    global max_tries
    global correct_word
    word_found = False
    print("-----------------Rules-------------------\n")
    print("Capital Letters are letters in the correct location")
    print("Lowercase Letters are within the word, but not the correct location")
    print("-------------------------------------------------------------------")
    getFiveLetterWords()
    correct_word = random.choice(tuple(five_letter_words))
    print(correct_word)
    while max_tries > 0 and not word_found:
        word = input(f"{max_tries} Tries left. Enter a valid {word_length} letter word: ").lower()
        if isValidWord(word):
            updateGameBoard(word)
            updateKeyboard(word)
            printGameBoard()
            printKeyboard()
            max_tries = max_tries-1
            if word == correct_word:
                word_found = True
        else:
            print(f'Invalid input <{word}>.')
    if word_found:
        print(f'\nYOU FOUND THE WORD WITH {max_tries} TRIES LEFT!!\n')
    else:
        print(f'\nNo more tries. The word was "{correct_word.upper()}"\n')


if __name__=="__main__":
    main()
