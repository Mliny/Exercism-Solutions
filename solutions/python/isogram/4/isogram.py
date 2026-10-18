def is_isogram(phrase):
    """Checks if a phrase is an isogram"""
    
    phrase = phrase.lower().replace(" ","").replace("-","")
            
    return all(phrase.count(letter) == 1 for letter in phrase)