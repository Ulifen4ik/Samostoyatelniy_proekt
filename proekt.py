class Drob:
    def __init__(self,numerator,znamenatel):
        self.numerator = numerator
        self.znamenatel = znamenatel

    def inputdrobi(self):
        self.numerator = int(input())
        self.znamenatel = int(input())
    
    def printdrob(self):
        print(self.numerator,"/",self.znamenatel)

    def plus(self,fraction2):
        new_numerator=self.numerator*fraction2.znamenatel+(fraction2.numerator*self.znamenatel)
        new_denominator=self.znamenatel*fraction2.znamenatel
        return Drob(new_numerator,new_denominator)

    def minus(self,fraction2):
        new_numerator=self.numerator*fraction2.znamenatel-(fraction2.numerator*self.znamenatel)
        new_denominator=self.znamenatel*fraction2.znamenatel
        return Drob(new_numerator,new_denominator)

    def multiply(self,fraction2):
        new_numerator=self.numerator*fraction2.numerator
        new_denominator=self.znamenatel*fraction2.znamenatel
        return Drob(new_numerator,new_denominator)

    def divide(self,fraction2):
        new_numerator=self.numerator*fraction2.znamenatel
        new_denominator=self.znamenatel*fraction2.numerator
        return Drob(new_numerator,new_denominator)


if __name__ == "__main__":
    fraction1 = Drob(4,8)
    fraction2 = Drob(1,2)
    result = fraction1.plus(fraction2)
    result.printdrob()
    result = fraction1.minus(fraction2)
    result.printdrob()
    result = fraction1.multiply(fraction2)
    result.printdrob()
    result = fraction1.divide(fraction2)    
    result.printdrob()
    
    
