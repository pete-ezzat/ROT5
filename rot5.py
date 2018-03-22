def letter_converter(mode, input_char):
	abc123 = "0123456789"

	# Number to Code
	if mode == 1	:
		found = abc123.find(input_char)
		if found > -1: return found
		else		 : return 0

	# Code to Number
	elif mode == 2	: return abc123[int(input_char)]

###-----------------------------------------------------------------

def encrypt():
	plaintext = input("Plaintext> ").lower()
	ciphertext = ""

	for char in plaintext:
		ascii_letter = letter_converter(1, char)
		ascii_letter = (ascii_letter + 5) % 10
		ciphertext += letter_converter(2, ascii_letter)

	ciphertext = ciphertext.upper()
	print(ciphertext, '\n')

###-----------------------------------------------------------------

def decrypt():
	ciphertext = input("Ciphertext> ").lower()
	plaintext = ""

	for char in ciphertext:
		ascii_letter = letter_converter(1, char)
		ascii_letter = (ascii_letter - 5) % 10
		plaintext += letter_converter(2, ascii_letter)

	print(plaintext, '\n')

###-----------------------------------------------------------------

while True:
	user_input = input("(E)ncrypt or (D)ecrypt> ").upper()
	user_input = user_input[0]

	if user_input == 'E'	: encrypt()
	elif user_input == 'D'	: decrypt()
	elif user_input == 'Q'  : exit()
	else: print("E/D/Q allowed only.\n")
