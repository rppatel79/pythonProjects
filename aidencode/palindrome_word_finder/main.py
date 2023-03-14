# 1 - Download a dictionary
#from english_words import get_english_words_set
from nltk.corpus import words
import nltk
nltk.download('words')

def check_palindrome(word: str) -> bool:
    if word == word[::-1]:
        return True
    return False


if __name__ == '__main__':
    # 2 - Load the dictionary
    #word_list = get_english_words_set(['gcide'], lower=True)
    word_list = words.words()

    all_palindrome = []
    # 2a - for each word in the dictionary
    for word in word_list:
        # 2b - check if the word is the same forward and backwards
        is_palindrome: bool = check_palindrome(word)
        # 2c - if palindrome then add one
        if is_palindrome:
            all_palindrome.append(word)

    print(all_palindrome)
