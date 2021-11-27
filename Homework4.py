
#Write a Fraction(num, denominator) class that implements the following methods:
class Fraction(object):
    #__init__ : instance numerator and denominator
    def __init__(self,num,den):
        self.num=num
        self.den=den
    
    #__str__ : display "numerator/counter"
    def __str__(self):
        return f'{self.num}/{self.den}'

    #return a new fraction representing the addition
    def __add__(self,otherfraction):
        new_num = self.num * otherfraction.den + self.den * otherfraction.num
        new_den = self.den * otherfraction.den
        return f'{new_num}/{new_den}'

    #return a new fraction representing the subtraction
    def __sub__(self,otherfraction):
        new_num = self.num * otherfraction.den - self.den * otherfraction.num
        new_den = self.den * otherfraction.den
        return f'{new_num}/{new_den}'

    #return a new fraction (the inverse of the fraction)
    def inverse(self):
        return Fraction(self.den,self.num)

