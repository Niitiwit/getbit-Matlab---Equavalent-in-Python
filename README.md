# getbit-Matlab---Equavalent-in-Python
I did the reseach paper work based on the python environment which is open source and found out some problem to use some function from Matlab to Python which I found out the way to solve it as python based  function which I create by myself.

# How to use
1.Call call Decimal_To_Binary class from DecimalToBinary module<br/><br/>
EX: from DecimalToBinary import Decimal_to_Binary<br/>
Test = Decimal_to_Binary()<br/><br/>
2.Call Function dec2bin from Decimal_To_Binary class by giving argument with Array of Decimal Number and Number of bits location<br/><br/>
  EX: Test.dec2bin(Decnum, Bitnum)<br/>
  
# Function calling Example
Decnum = [11,12,16,17,18,19]<br/>
Bitnum = 8<br/>
Test = Decimal_to_Binary()<br/>
print(Test.dec2bin(Decnum, Bitnum))

# OUTPUT
['00001011', '00001100', '00010000', '00010001', '00010010', '00010011']
