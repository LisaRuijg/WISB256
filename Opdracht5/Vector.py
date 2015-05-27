import math

class Vector():
    def __init__(self,n,a = 0):
        if type(a) == list:
            self.vector = a
        else:
            self.vector = [a]*n    
            
    def __str__(self):
        return "\n".join(str("{0:.6f}".format(x)) for x in self.vector)
    
    def scalar(self,alpha=1):
        return Vector(len(self.vector),[alpha * self.vector[i] for i in range(len(self.vector))])
        
    def lincomb(self,other,alpha,beta):    
        A = [alpha * self.vector[i] for i in range(len(self.vector))]
        B = [beta * other.vector[i] for i in range(len(other.vector))]
        return Vector(len(self.vector),[A[i]+B[i] for i in range(len(self.vector))])
        
    def inner(self,other):
        lijst = [ self.vector[i]*other.vector[i] for i in range(len(self.vector))]
        return math.fsum(lijst)
        
    def norm(self):
        kwadraat = self.inner(self)
        return math.sqrt(kwadraat)
        
    def proj(self,other):
        lijst_2 =[((self.inner(other))/(self.inner(self)))*self.vector[i] for i in range(len(self.vector))]
        return math.fsum(lijst_2)
    
    def GrammSchmidt(self,other):
        u_1 = self.vector
        u_2 = other.vector
        
