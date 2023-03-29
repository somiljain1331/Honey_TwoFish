#import import_ipynb
import sys
import timeit
from datetime import datetime
import honey
import twoFish
from random import *
from pprint import pprint
import random
import testData as testData
import aes
from os import urandom
i=0
s1= None
s2= None
while i < len(testData.testdata):
    output={}
    #print(i)
    if i>21:
        break
    j=i
    userName = testData. testdata[i] 
    userPass = testData.testdata[i+1]
    message = testData.testdata[i+2]
    key = testData.testdata[i+3]
    i+=3
    #print(i,userName,'-- ',userPass,message,key)
    i+=1

    size_of_key= sys.getsizeof(key)
    size_userPass= sys. getsizeof(userPass)

    #print("Size of key in bytes",size_of_key)
    #print("Size of message in bytes",size_userPass)

    print('Honey Encryption Initialisation...')
    executionStart=timeit.default_timer()

    password,passwordsToSeeds,seedsToMessages,cipher,trueSeed,states = honey.HoneyEncrypt().honeyEncrypt(userName,userPass,message)
    #print(cipher)
    #print(trueSeed)

    print("passwordsToSeeds:\n",passwordsToSeeds)
    print("seedsToMessages:\n",seedsToMessages)
    # Goodbye message
    print("\nHoney Encryption Done...")
    print('=====================================\n')

    print('Two Fish Encryption Initialisation...')
    encTimeStart=timeit.default_timer()
    two_fish=twoFish.tfencrypt(password,key)
    if j==0:
        s1=str(two_fish)[1:]
        #print(s1 ,"")
    elif j==4:
        s2=str(two_fish)[1:]
        #print(s2 , "")


    print('Encrypted Password: ',two_fish)
    encTimeEnd=timeit.default_timer()
    encTotalTime=encTimeEnd-encTimeStart
    encTotalTime*=1000
    print("encTotalTime : " ,encTotalTime)
    print('=====================================\n')

    print('Two Fish Decryption Inititalisation...')
    decStartTime=timeit.default_timer()
    decrypt_=twoFish.tfdecrypt(two_fish, key)
    print("decrypt:",str(decrypt_)[1::])    
    # print(decrypt_)
    decEndTime=timeit.default_timer()
    decTotalTime=decEndTime-decStartTime
    decTotalTime*=1000
    print("decTotalTime : ",decTotalTime)
    print('=====================================\n')

    # print('AES Encryption Initialisation...')
    # iv = urandom(16)
    # aes_key= urandom(16) 
    # aes_encTimeStart=timeit.default_timer()
    # enc_aes_pass=aes.Enc_AES(userPass,aes_key,iv)
    # print('Encrypted Password: ',enc_aes_pass)
    # aes_encTimeEnd=timeit.default_timer()
    # aes_encTotalTime=aes_encTimeEnd-aes_encTimeStart
    # aes_encTotalTime*=1000
    # print("encTotalTime : " ,aes_encTotalTime)
    # print('=====================================\n')

    # print('AES Decryption Inititalisation...')
    # aes_decStartTime=timeit.default_timer()
    # decrypt_=aes.Dec_AES(enc_aes_pass, aes_key,iv)
    # print("decrypt:",str(decrypt_)[1::])    
    # # print(decrypt_)
    # aes_decEndTime=timeit.default_timer()
    # aes_decTotalTime=aes_decEndTime-aes_decStartTime
    # aes_decTotalTime*=1000
    # print("decTotalTime : ",aes_decTotalTime)
    # print('=====================================\n')

    passwords = list(passwordsToSeeds.keys())
    shuffle(passwords)                   # Shuffle the passwords
    #print(passwords)
    #print(passwordsToSeeds,seedsToMessages,cipher,trueSeed)                           # Display results

    # Prompt the user to crack this password
    print('Decoding Password and Fetching Secret message from Honey encryption: ')
    p = passwordsToSeeds.keys()
    query = 'spiderman@batman'
    if query!=decrypt_ and query not in passwords:
        print('wrong Password...')
        executionEnd=timeit.default_timer()
        executionTime=executionEnd-executionStart
        executionTime*=1000
        print("executionTime : ",executionTime)
        print('=====================================\n')
        # sys.exit()
    try:
                
        # print('decrypt_',decrypt_.decode("utf-8"))
        keySeed = passwordsToSeeds[query]
        # print('decrypt_',keySeed)

        # DECRYPTION: m = sk XOR c
        m = keySeed ^ cipher                     # ^ == XOR
        # print('decrypt_')
        if message in states.keys():
            if m != trueSeed:                       # Honey checker
                print("Intruder! Sound alarm!")
                print('Fetching Secret Message from Honey Encryption: ',seedsToMessages[keySeed])

        # Check seeds
            else:
                #print('Password Decrypted: ',query)
                print('Fetching Secret Message from Honey Encryption: ',states[seedsToMessages[m]])
                print('=====================================\n')
        else:
            if query == password:
                #print('Password Decrypted: ',query)
                state=random.choice(list(states.keys()))
                print('Fetching Secret Message from Honey Encryption: ',message)
                print('=====================================\n')
            else:
                print("Intruder! Sound alarm!")
                print('Password Decrypted: ',query)
                state=random.choice(list(states.keys()))
                print('Fetching Secret Message from Honey Encryption: ',states[state])
    except KeyError:
        print('Fetching Secret Message from Honey Encryption: ')
        print('=====================================\n')
    executionEnd=timeit.default_timer()
    executionTime=executionEnd-executionStart
    executionTime*=1000
    print("executionTime : ",executionTime,)
    print('=====================================\n')
    print('AES Encryption Initialisation...')
    iv = urandom(16)
    aes_key= urandom(16) 
    aes_encTimeStart=timeit.default_timer()
    enc_aes_pass=aes.Enc_AES(userPass,aes_key,iv)
    print('Encrypted Password: ',enc_aes_pass)
    aes_encTimeEnd=timeit.default_timer()
    aes_encTotalTime=aes_encTimeEnd-aes_encTimeStart
    aes_encTotalTime*=1000
    print("encTotalTime : " ,aes_encTotalTime)
    print('=====================================\n')

    print('AES Decryption Inititalisation...')
    aes_decStartTime=timeit.default_timer()
    decrypt_=aes.Dec_AES(enc_aes_pass, aes_key,iv)
    print("decrypt:",str(decrypt_)[1::])    
    # print(decrypt_)
    aes_decEndTime=timeit.default_timer()
    aes_decTotalTime=aes_decEndTime-aes_decStartTime
    aes_decTotalTime*=1000
    print("decTotalTime : ",aes_decTotalTime)
    print('=====================================\n')


    output['size_userPass']=size_userPass
    output['size_of_key']=size_of_key
    output['encTotalTime']=encTotalTime
    output['decTotalTime']=decTotalTime
    #output['executionTime']=executionTime
    output['aes_encTotalTime']=aes_encTotalTime
    output['aes_decTotalTime']=aes_decTotalTime
    output['executionTime']=executionTime
    # outputData[runId]=output
    from csv import DictWriter
    
    # list of column names
    field_names = ['size_userPass', 'size_of_key', 'encTotalTime','decTotalTime','aes_encTotalTime', 'aes_decTotalTime','executionTime']
    
 
    # Open CSV file in append mode
    # Create a file object for this file
    with open('results.csv', 'a') as f_object:
    
        # Pass the file object and a list
        # of column names to DictWriter()
        # You will get a object of DictWriter
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
        # Pass the dictionary as an argument to the Writerow()
        dictwriter_object.writerow(output)
    
        # Close the file object
        f_object.close()
import compare_bits as cb
cb.comp_count(s1,s2)

