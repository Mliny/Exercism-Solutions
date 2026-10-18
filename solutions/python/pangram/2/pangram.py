def is_pangram(sentence):
    lcs = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in lcs:
            return False
    return True