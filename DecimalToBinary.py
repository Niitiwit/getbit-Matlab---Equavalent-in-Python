import numpy as np

class Decimal_to_Binary:
    def __init__(self):
        #array of Decimal Number
        #BitNum is the number of binary position to have
        self.Decnum = []
        self.arrayBinChar = []
        
    def dec2bin(self,Decnum,Bitnum):
        #to store value of Dec2bin as str not none
        ArrayOfDec2Bin = []
        i = 0
        for i in range(0,len(Decnum)):
            tranverseArray = int(Decnum[i])
            self.arrayBinChar = ArrayOfDec2Bin.append(np.binary_repr(tranverseArray,width=Bitnum))
            i = i+1
        return ArrayOfDec2Bin

Decnum = [11,12,16,17,18,19]
Bitnum = 8
Test = Decimal_to_Binary()
print(Test.dec2bin(Decnum, Bitnum))