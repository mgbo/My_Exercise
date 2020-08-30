
class fraction(object):

    def __init__(self, n, d):
        self.numerator, self.denominator = fraction.reduce(n, d)
        
    @staticmethod
    def gcd(a,b):
        while b != 0:
            print (a,b)
            a, b = b, a%b
        return a

    @classmethod
    def reduce(cls, n1, n2):
        g = cls.gcd(n1, n2)
        return (n1 // g, n2 // g)

    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)

if __name__ == "__main__":
	f1 = fraction(3,8)
	print (f1)
