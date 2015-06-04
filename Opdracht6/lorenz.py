import numpy as np
import scipy as sp
from scipy.linalg import eigvals
from scipy.integrate import odeint

class Lorenz():
    def __init__(self, lijst, sigma=10, rho=28, beta=(8/3)):
        self.x_0 = lijst[0]
        self.y_0 = lijst[1]
        self.z_0 = lijst[2]
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
    
    def functies(self, x, t):
        x_dot = self.sigma*(x[1]-x[0])
        y_dot = x[0]*(self.rho-x[2])-x[1]
        z_dot = x[0]*x[1]-self.beta*x[2]
        return np.array([x_dot, y_dot, z_dot])

    def solve(self,T,dt):    
        self.times = np.arange(0,T,dt)
        self.initialisatie = [self.x_0, self.y_0, self.z_0]
        self.oplossen = odeint(self.functies, self.initialisatie, self.times)
        return self.oplossen
        
    def df(self,u):
        matrix = np.array([[ -self.sigma, self.sigma, 0],
                           [ self.rho - u[2], -1, -u[0]],
                           [ u[1], u[0], -self.beta]])
        return matrix
    
    def isStable(self,u):
        eigenwaarden_matrix = eigvals(self.df(u))
        if eigenwaarden_matrix[0] < 0 and eigenwaarden_matrix[1] < 0 and eigenwaarden_matrix[2] < 0:
            return True
        else:
            return False