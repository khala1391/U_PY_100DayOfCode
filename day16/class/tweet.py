class Tweet:
    def __init__(self, id, text, year):
        self.id=id
        self.text=text
        self.year=year
    
    def wordcount(self):
        return len(self.text.split(" "))