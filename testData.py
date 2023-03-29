import sys


p_t = 'spiderman@batman' 
#print("Password-",p_t)
#print("****Conversion in bits****")
b_t=''.join(format(ord(i), '02b') for i in p_t)
#print(b_t)
if b_t[-1] == '0':
    b = b_t[-1].replace("0","1")
else: 
    b=b_t[-1].replace("1","0")

bin_data = b_t[0:len(b_t)-1]+b #String 

def BinaryToDecimal(binary):  
    string = int(binary, 2)
     
    return string
  
# print("****Change in 1 bit (last bit is flipped)****")
# print(bin_data)
# print("****Conversion of bits to string****")


  
str_data =''
  

for i in range(0, len(bin_data), 7):
     
    
    temp_data = bin_data[i:i + 7]
      

    decimal_data = BinaryToDecimal(temp_data)

    str_data = str_data + chr(decimal_data)

#print(str_data)
size= sys.getsizeof(p_t)
#print(size)

testdata = ['user1',p_t,'CA','key',
            'user2',str_data,'CA','key',
            'user3','spiderman@batmad','CA','key',
            'user4','spiderman@batmal','CA','key',
            'user5','spiderman@batmae','CA', 'key',
            'user6','spiderman@batmaw','CA', 'key',
            'user7','spiderman@batmaa','CA','key']