class hesap_makinesi:
    def __init__(self):
        self.x = 5
        self.y = 20
    
    def toplama(self):
        return self.x + self.y
    def cikarma(self):
        return self.x - self.y
    def bolme(self):    
        return self.x / self.y
    def carpma(self):
        return self.x * self.y
    
deneme = hesap_makinesi()
    
    
print(deneme.bolme())
print(deneme.carpma())
print(deneme.toplama())
print(deneme.cikarma())

