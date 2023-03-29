from random import *
from pprint import pprint
import json

class HoneyEncrypt():


    def honeyEncrypt(self,userName, userPass, message):

        
        passwordsToSeeds = {}   # dictionary
        seedsToMessages = {}    # dictionary
        data = {} #new
        trueSeed = randint(10, 27)    # Random seed value
        states = {  # U.S States as secret messages
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
        }
        ' Verify input with the user '
        print("Your password is " + userPass
            + ", your seed value is " + str(trueSeed)
            + ", and your secret message is " + message
            + "\n=====================================")

        # Seed generator + Sweetwords generator
        # Manipulate the password input by the user
        #   Add a string to that password
        #   Seeds should remain as integers that
        #   be converted into binary digits
        passwordsToSeeds[userPass] = trueSeed
        seedsToMessages[trueSeed] = message
        #print('sseed',trueSeed,message,passwordsToSeeds,seedsToMessages)

        passwordsToSeeds[userPass + str(trueSeed - 1)] = trueSeed + 1
        seedsToMessages[trueSeed + 1] = states['AL']
        #print('93sseed',passwordsToSeeds,seedsToMessages)

        passwordsToSeeds[userPass + str(trueSeed - 2) + "1"] = trueSeed + 2
        seedsToMessages[trueSeed + 2] = states['CA']
        #print('97sseed',passwordsToSeeds,seedsToMessages)

        passwordsToSeeds[userPass.lower()] = trueSeed + 3
        seedsToMessages[trueSeed + 3] = states['FL']

        passwordsToSeeds[userPass.lower() + str(trueSeed + 1) + "3"] = trueSeed + 4
        seedsToMessages[trueSeed + 4] = states['TX']
        #print('104sseed',passwordsToSeeds,seedsToMessages)


        passwordsToSeeds[userPass.upper()] = trueSeed + 5
        seedsToMessages[trueSeed + 5] = states['TN']

        passwordsToSeeds[userPass.upper() + str(trueSeed + 2) + "5"] = trueSeed + 6
        seedsToMessages[trueSeed + 6] = states['WA']
        #print("passwordsToSeeds:",passwordsToSeeds)
        #print("seedsToMessages:",seedsToMessages)

        

        # ENCRYPTION: c = sk XOR sm
        cipher = int(passwordsToSeeds[userPass]) ^ trueSeed
        #print("userPass, passwordsToSeeds, seedsToMessages,cipher,trueSeed",userPass, passwordsToSeeds, seedsToMessages,cipher,trueSeed)
        return userPass, passwordsToSeeds, seedsToMessages,cipher,trueSeed,states
#print("passwordsToSeeds:",passwordsToSeeds)
#print("seedsToMessages:",seedsToMessages)
