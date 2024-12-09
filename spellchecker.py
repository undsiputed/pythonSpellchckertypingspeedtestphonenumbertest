from spellchecker import SpellChecker

spell = SpellChecker()

def check_spelling(word):
    corrected_word = spell.correction(word)
    if corrected_word == word:
        return f"The word '{word}' is spelled correctly."
    else:
        return f"The word '{word}' is not spelled correctly. The correct spelling is '{corrected_word}'."

word = input("Enter a word: ")
print(check_spelling(word))