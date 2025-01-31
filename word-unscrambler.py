from nltk.corpus import words
from itertools import permutations
import inflect

english_words = set(words.words())
converter = inflect.engine()

scrambled = input("Input some scrambled letters: ").lower()
print("")

word_ctr = 0
for length in range(4, len(scrambled)+1):
    valid_words = set()
    for perm in permutations(scrambled, length):
        word = "".join(perm)
        if word in english_words:
            valid_words.add(word)
        
    word_ctr += len(valid_words)
    for word in list(valid_words):
        print(word)

    if len(valid_words) > 0:
        print(f"Found {len(valid_words)} {converter.number_to_words(length)}-letter words!")

print(f"Found {word_ctr} total words from input {scrambled.upper()}!")