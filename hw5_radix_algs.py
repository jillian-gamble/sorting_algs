import sys

buckets = [[],[],[],[],[],[],[],[],[],[]]

#the actual sorting portion
def radix_sort(numbers):
    maxDigits = getNumDigits(max(numbers))
    output = numbers
    #iterating through the places (1s, 10s, 100s, etc)
    for place in range(maxDigits):
        buckets = [[],[],[],[],[],[],[],[],[],[]]
        #iterating through each number to be sorted
        for number in output:
            digits = get_digit(number,place)
            buckets[digits].append(number)
        output = bucketsToList(buckets)
        print("Round ", place, " buckets: ", buckets)


    return output    

#retrieves the digit from a certain place in a number    
def get_digit(num, place):
    if num < 10**place:
        return 0
    num = str(num)[::-1]
    digit = num[place]
    return int(digit)
        
#gets the number of digits    
def getNumDigits(num):
    numDig = len(str(num))
    return numDig

#reads buckets l to r    
def bucketsToList(buckets):
    list = []
    for bucket in buckets:
       list.extend(bucket)
    return list 



file = open(sys.argv[1])
inp = []

#turning file input into a list
for num in file:
    inp.append(int(num))


print(inp)
print(list(radix_sort(inp)))
