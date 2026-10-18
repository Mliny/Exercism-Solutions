def is_pangram(sentence):
    lcs = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    return not any(letter not in lcs for letter in alphabet)