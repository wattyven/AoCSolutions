filepath = 'Day 12 input.json'

# GOOD FUCKING GOD I HAVE TO USE REGEX TO PARSE JSON
# STOP GIVING ME REGEX STUFF I HATE THIS

from json import loads
import re

def sum_numbers(fpath):
    '''does what it says'''
    with open(fpath, 'r') as f:
        text = loads(f.read())
    nums = [int(x) for x in re.findall(r'-?\d+', str(text))]
    return sum(nums)
    
if __name__ == "__main__":
    sum_of_all = sum_numbers(filepath)
    print("The sum of all the numbers in your file is: ", sum_of_all) # part one
    # haven't figured out part two yet i really hate this stuff and i'm not good with it
    # will come back to it -- currently 11/27/2022, 22:51 PST
