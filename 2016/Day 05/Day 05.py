puzzleinput = 'ojvtpuvg'

import hashlib

def findHash(puzzleinput):
    '''part one'''
    index = 0
    password = ''
    while len(password) < 8:
        hashstring = puzzleinput + str(index)
        hash = hashlib.md5(hashstring.encode('utf-8')).hexdigest()
        if hash.startswith('00000'):
            password += hash[5]
        index += 1
    return password

def getPassword(puzzleinput):
    '''part two'''
    index = 0
    password = ['_'] * 8
    while '_' in password:
        hashstring = puzzleinput + str(index)
        hash = hashlib.md5(hashstring.encode('utf-8')).hexdigest()
        if hash.startswith('00000'):
            try:
                if password[int(hash[5])] == '_':
                    password[int(hash[5])] = hash[6]
            except:
                pass
        index += 1
    return ''.join(password)

# i have no idea as to how to make a 'cinematic "decrypting" animation' in python.
# i'm sure i could do it with a bunch of print statements, but that would add a stupid
# amount of time to the program. i'm sure there's a better way, but i don't know it.


print(findHash(puzzleinput))
print(getPassword(puzzleinput))
