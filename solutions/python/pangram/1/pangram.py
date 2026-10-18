def is_pangram(sentence):
    lcs = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for v in alphabet:
        if v not in lcs:
            return False
    return True
    pass