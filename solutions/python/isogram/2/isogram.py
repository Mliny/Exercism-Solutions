def is_isogram(phrase):
    phrase = phrase.lower().replace(" ","").replace("-","")
            
    return all(phrase.count(letter) == 1 for letter in phrase)
