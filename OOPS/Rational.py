class Rational:
    def __init__(self,numer,denom):
        self.numer=numer
        self.denom=denom
        self._reduce()
    
    def numerator(self):
        return self.numer
    
    def denominator(self):
        return self.denom
    
    def _reduce(self):
        divisor=self._gcd(self.numer,self.denom)
        self.numer=self.numer//divisor
        self.denom=self.denom//divisor

    def gcd(self,a,b):

        if b == 0:
            return a
        else:
            return self.gcd(self,b, a % b)

        