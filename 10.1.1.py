import os

def welcom_screen():
	"""
	This function print the 'HANGMAN' title and get from the user the word file path and the insex of the word he would like to use.
	:parm: none
	:type: none
	:return: user_path, index
	:rtype:string, index
	"""
	print("""  _    _                                         
 | |  | |           
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""") #Game's title.
	
	user_path = input("Enter file path: ")
	index = input("Enter index: ")
	
	return(user_path, int(index))

def choose_word(file_path, index):
	"""
	This function get a file path and an index of word that take from the file and return a word.
	:parm: file_path, index.
	:type: string, integer.
	:return: words_number, words_list[index]
	:rtype: integer, string.
	"""
	file = open(file_path, 'r') # Open the file 
	
	data = file.read() # Reading the file into a string
	
	words_list = data.split(' ') # Make a list of words.
	
	
	
	for word in words_list:
		
		while words_list.count(word) > 1:
			words_list.remove(word) # Remove all the words that appears in the file more the one time.
	
	words_number = len(words_list)
	
	if index >= words_number: # Keep counting circular.
		index -= words_number
	
	return(words_list[index])	

def show_hidden_word(secret_word , old_letters_guessed):
	"""
	This function get the secret word and the 'old letter guessed' list and return the user "status" on the game. 
	:parm: secret_word, old_letters_guessed
	:type: string, list
	:return: user_status
	:rtype: string
	"""
	
	template = []
	
	for j in range(len(secret_word)): # made the 'base' list full of "_" at the len of the secret_word.
		template.append(' _ ')
	
	
	for letter in old_letters_guessed:
		if letter in secret_word: # if the letter in the 'old_letters_guessed' list, get the word index and switch the '_' with the right character.
			for i in range(len(secret_word)):
				if letter == secret_word[i]:
					template[i] = ' ' + letter + ' '
					
	user_status = ''.join(template) # Make the template to a list.
	
	return(user_status)

def print_hangman(num_of_tries):
	
	HANGMAN_PHOTOS = {0 : """    x-------x""", 1 : """    x-------x
    |
    |
    |
    |
    |""", 2 : """    x-------x
    |       |
    |       0
    |
    |
    |""", 3 : """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 4 : """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 5 : """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 6 : """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}
	
	
	print(HANGMAN_PHOTOS[num_of_tries])

def check_valid_input(letter_guessed, old_letters_guessed):
	"""
	This function checks if the guessed letter is valid
	:parm: letter_guessed, old_letters_guessed.
	:type: Char / str, list.
	:return: True / False.
	:rtype: Bool.
	"""

	if ((len(letter_guessed) > 1) or (not letter_guessed.isalpha()) or (letter_guessed in old_letters_guessed)): # Check if the value of "letter_guessed" is only an alphabetic char.
		return False

	else:
		return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	
	"""
	This function update the 'old_letters_guessed' list as long as it valid input
	:parm: letter_guessed, old_letters_guessed.
	:type: str, list.
	:return: True / False.
	:rtype: Bool.
	"""
	if (check_valid_input (letter_guessed, old_letters_guessed)):
		old_letters_guessed.append(letter_guessed) #if the user enter a valid input, it append to the 'old_letters_guessed' list.
		return True
	else:
		old_letters_guessed.sort() # sorted alphabeticly the list.
		temp_list = "->".join(old_letters_guessed) # temp list for the guessed letters with the '->' between.
		
		print("X")
		print(temp_list)
		
		return False

def check_win(secret_word, old_letters_guessed):
	"""
	This function check if the user guessed all the words in the secret_word.
	:parm: secret_word, old_letters_guessed
	:type: string, list
	:return: result
	:rtype:bool
	"""
	result = True
	
	for letter in secret_word:
		if letter in old_letters_guessed:
			result = True
		else:
			result = False
			break
	
	if result: # Check the last value of the result to know if the user win
		print("WIN")
	
	return(result)



def main():
	
	old_letters_guessed = []
	mistakes = 0 # User mistakes number
	letter_guessed = ''
	
	clear = lambda: os.system('cls') # Define a function the clear the cmd screen
	
	path, index = welcom_screen() 
	
	secret_word = choose_word(path, index) 
	
	clear()
	
	print("Let's start!")
	print_hangman(mistakes)
	print('\n', show_hidden_word(secret_word, old_letters_guessed), '\n') # Show the user the word he need to guess
	
	while not(check_win(secret_word, old_letters_guessed)): # While user not win yet, keep get a letter. 
		
		letter_guessed = input("Guess a letter: ").lower() # Get the letter and make sure it lower.
		try_update_letter_guessed(letter_guessed, old_letters_guessed)
		
		if letter_guessed in secret_word: 
			print('\n', show_hidden_word(secret_word, old_letters_guessed), '\n')	
		else:
			if letter_guessed.isalpha(): #if letter guessed is alpha but still not indlude in the word, it's a mistake 
				mistakes += 1
				print(":(")
				print_hangman(mistakes)
			
			if mistakes == 6:
				print_hangman(mistakes)
				print("LOSE")
				break
			
			else:
				print('\n', show_hidden_word(secret_word, old_letters_guessed), '\n')
				


if __name__ == "__main__":
	main()