# i refuse to use regex
# i also refuse to implement the really stupid solution i 
# told a friend about, because, as i said, "Could there possibly
# be a worse way to solve this than {REALLY dumb implementation}??"

# anyhow we're still going to use a bad solution, bc i'm lazy
# and i don't want to think about this problem anymore, so instead of 
# making a loop to check letters im just going to make a list of triplets
# to compare against for criterion 1 and 2. thank god the english alphabet
# only has 26 letters, and that i'm not doing this one against the clock.

# you could honestly think of this as a base 26 number system, with I O and L
# being invalid chars, but you could also think of this as being a really 
# annoying string

# FUCK i have to use regex to check for doubled letters
import re

password = 'hxbxwxba' # input

def splitstring(s):
    '''splits a string into everything before the last char and the last char'''
    left, right = s[:-1], s[-1]
    return left, right

def increment(s):
    '''increments a string by one'''
    left, right = splitstring(s) # split the string
    if right == 'z':
        return increment(left) + 'a' # if the last char is z, increment the rest of the string
    else:
        return left + chr(ord(right) + 1)

def valid_password(s):
    '''knock out those invalid chars'''
    if sum(map(s.count, 'iol')) == 0: # doesn't have the disallowed chars
        if sum(map(s.count, ['abc', 'bcd', 'cde', 
                     'def', 'efg', 'fgh', 
                     'pqr', 'qrs', 'rst', 
                     'stu', 'tuv', 'uvw', 
                     'vwx', 'wxy', 'xyz'])): # i shouldn't have hardcoded these but I DID
            # too late to do anything about it now :)
            # ah fuck i guess i have to use regex to check for doubled letters
            if len(set(re.findall(r'(.)\1', s))) > 1:
                return True # password is valid, let's go on to the next step
    return False # password is invalid, let's give the next function
    # a signal to increment it until it's valid

def next_password(s):
    '''increments a password until it's valid'''
    while not valid_password(s): # self-explanatory
        s = increment(s) # increment until it's valid
    return s # return the valid password

def main():
    '''puts it all together'''
    p1 = next_password(password)
    print(p1) # part one
    p2 = next_password(increment(p1))
    print(p2) # part two

if __name__ == "__main__":
    main()
