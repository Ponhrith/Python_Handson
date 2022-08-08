class Characters:
    def __init__(self) :
        pass
    
    def capital alphabets(self) :
        capital_letters = list(string.ascii_uppercase)
        return capital_letters
    
    def small_alphabets(self):
        small_letters = string.ascii_lowercase
        return small_letters
    
    def numbers(self):
        pass
    
    def symbols(self): 
        pass
        
ch = Characters()
print(ch.capital_alphabets())
print(ch.small_alphabets())