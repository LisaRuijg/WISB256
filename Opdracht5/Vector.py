import math

class Vector():
    def __init__(self,n,a = 0):
        if type(a) == list:
            self.vector = a
        else:
            self.vector = [a]*n    
            
    def __str__(self):
        return "\n".join(str("{0:.6f}".format(x)) for x in self.vector)+'\n'
    
    def scalar(self,alpha=1):
        return Vector(len(self.vector),[alpha * self.vector[i] for i in range(len(self.vector))])
        
    def lincomb(self,other,alpha=1,beta=1):    
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
        lijst_2 =((self.inner(other))/(self.inner(self)))
        resultaat = self.scalar(lijst_2)
        return resultaat
    
    def normal(self):
        return self.scalar(1/self.norm())

def projoptellen(lijst,v):
    p=[]
    for i in range(0,len(lijst)):
        p.append(lijst[i].proj(v[len(lijst)]))
    waarden=p[0]
    for i in range(1,len(p)):
        waarden=waarden.lincomb(p[i])
    som=waarden.scalar(-1)
    return som

def GrammSchmidt(v):
    lijst=[v[0]]
    for i in range(1,len(v)):
        lijst.append(v[len(lijst)].lincomb(projoptellen(lijst,v)))
    e=[]
    for i in lijst:
        e.append(i.normal())
    return e    