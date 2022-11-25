import hashlib

filepath = "Day 4 key.txt"

def readKey(filepath):
    '''reads the key from a file'''
    file = open(filepath, "r") # opens the file
    key = file.read() # reads the file
    return key

# why are we using MD5 for crypto? i mean i hate crypto enough as-is,
# but built upon a fundamentally broken hash function? why?

'''i'm not too familiar with the MD5 algorithm, so i'm going to use a really fucking stupid
brute force method to solve this problem: the string we're hashing starts with our secret key,
then has a number appended to it, then we hash it. so basically we're adding two strings, that's 
easy enough -- we then compute the hash for our new string using encode() and hashlib.md5(), and 
check if the first five characters of the hash are zeroes. if they are, we know our string is valid,
and we can return the number that we appended as our answer. otherwise, we increment the number and
try again -- we can start at 0 and increment by 1, because we know that the answer is a positive
integer. however, looking at the size of some of these numbers, who knows how long this might take. 
that's why i think this is a really really dumb approach, but i'm not familiar enough to do it a
different way yet, and i'm also sleep deprived and it's midnight. maybe it's not dumb. who knows? lesgo.'''

def findAnswer(key):
    '''finds the answer to part one'''
    num = 0
    while True:
        string = key + str(num) # add the key and the number together
        hash = hashlib.md5(string.encode()) # encode our string and hash it
        if hash.hexdigest()[0:5] == "00000": # check if the first five characters of the hash are zeroes
            return num # if they are, return the number
        num = num + 1 # otherwise, increment the number and try again

# wow that actually fucking worked for part one
# i'm not sure if i should be proud or ashamed
# oh part two is the same thing but with six zeroes LOL WE GO AGAIN

def findAnswer2(key):
    '''finds the answer to part two'''
    num = 0
    while True:
        string = key + str(num) # add the key and the number together
        hash = hashlib.md5(string.encode()) # encode our string and hash it
        if hash.hexdigest()[0:6] == "000000": # check if the first SIX characters of the hash are zeroes
            return num # if they are, return the number
        num = num + 1 # otherwise, increment the number and try again
        # wow all my comments and shit are almost exactly the same i wonder WHYYYYYY

def main():
    '''main, puts everything together'''
    key = readKey(filepath) # reads the key from the file
    print("The answer to part one is", findAnswer(key)) # prints the answer to part one
    print("The answer to part two is", findAnswer2(key)) # prints the answer to part two

# yup running part 2 actually took more than an instant, but at least it was still only a couple seconds.
# i don't wanna think about doing any more numbers than that. god save my cpu. 

if __name__ == "__main__":
    main()
