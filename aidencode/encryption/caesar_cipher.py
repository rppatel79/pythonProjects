import string

seed_value=1

def encrypt_char(char: str) -> int:
	if len(char) != 1:
		raise RuntimeError('cannot encrypt a str of more than 1 character')

	char_ordinal = seed_value
	# loop across all the lower case letter
	for letter in string.ascii_lowercase[0:26]:
		if letter == char:
			return char_ordinal
		else:
			char_ordinal  = char_ordinal + 1
	#unknown character
	return -500

def main():
	#the phrase to encrypt
	phrase_to_encrypt = 'how is you day'

	# loop over each character in the phrase
	for element in range(0, len(phrase_to_encrypt)):
		print(encrypt_char(phrase_to_encrypt[element]))

if __name__ == "__main__":
    # execute only if run as a script
    main()
