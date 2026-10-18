def is_isogram(phrase):
    """Module providing a function printing python version."""
    
    phrase = phrase.lower().replace(" ","").replace("-","")
            
    return all(phrase.count(letter) == 1 for letter in phrase)