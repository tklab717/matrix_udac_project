import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

def factorial(n):
    """
    Calculate factorial
    """
    if n == 1:
        return 1
    return n*factorial(n-1) 

def permutation(S,T,num):
    """
    Calculate permutation
    """
    print(S)
    if len(S)==1:
        #return　S.append(T[0])
        pass
        
    
    list_p = []
    for i in range(len(S)-1)
        ind = [True for i in range(len(S))]
        ind[num]=False 
        list_p.append(permutation(S[ind],T.append(S[num]),i))
    return list_p
    
    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 

    
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        num_value = factorial(self.w)
        listh = []
        for i in range(num_value):
            listw = []
            for j in range(self.h):
                listw.append(self.g[j][-i])
            listh.append(listw)
        return Matrix(listh)     
        
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        trace = 0
        # TODO - your code here
        for i in range(self.w):
            trace += self.g[i][i]
        return trace
        
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        listh = []
        for i in range(self.w):
            listw = []
            for j in range(self.h):
                listw.append(self.g[j][-i])
            listh.append(listw)
        return Matrix(listh)       
        
        

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        lista = []
        for i in range(self.w):
            listb = []
            for j in range(self.h):
                listb.append(self.g[j][i])
            lista.append(listb)
        return Matrix(lista)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        listi=[]
        for i in range(self.h):
            listj =[]
            for j in range(self.w):
                listj.append(self.g[i][j]+other.g[i][j])
            listi.append(listj)
        return Matrix(listi)
                
                
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        listi=[]
        for i in range(self.h):
            listj =[]
            for j in range(self.w):
                listj.append(-self.g[i][j])
            listi.append(listj)
        return Matrix(listi)        
        
        

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """

        listh=[]
        for i in range(self.h):
            listw =[]
            for j in range(self.w):
                listw.append(self.g[i][j]-other.g[i][j])
            listh.append(listw)
        return Matrix(listh)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if not self.w == other.h:
            raise(ValueError, "Cannot calculate these matrix.")
        listh=[]
        for i in range(other.w):
            listw =[]
            for j in range(self.h):
                listw.append(sum([self.g[i][k]+other.g[k][j] for k in range(self.w)]))
            listh.append(listw)
        return Matrix(listh)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        listh=[]
        if isinstance(other, numbers.Number):
            for i in range(self.h):
                listw=[]
                for j in range(self.w):
                    listw.append(self.g[i][j]*other)
                listh.append(listw)
            return Matrix(listh)