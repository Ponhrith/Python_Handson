import string

class Characters:
    def __init__(self, symbols) :
        self.symbols = symbols
    
    def capital alphabets(self) :
        capital_letters = list(string.ascii_uppercase)
        return capital_letters
    
    def small_alphabets(self):
        small_letters = string.ascii_lowercase
        return small_letters
    
    def numbers(self):
        numbers = ""
        for num in range(0, 10):
            numbers += f"{num}"
        return numbers.split(" ")
    
    def symbols(self): 
        symbols = self.symbols
        return symbols.split("")

symbols = "! @ # $ % ^ & * ( ) + - / [ ] { } ~ ` ' < > = . , : ; _ | "       
ch = Characters(symbols)
print(ch.capital_alphabets())
print(ch.small_alphabets())