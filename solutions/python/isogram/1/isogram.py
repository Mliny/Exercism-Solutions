def is_isogram(phrase):
    phrase = phrase.lower().replace(" ","").replace("-","")
    for letter in phrase:
        if phrase.count(letter) > 1:
            return False
            
    return True
