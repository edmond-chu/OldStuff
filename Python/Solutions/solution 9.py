# Given a rod of length n and a dictionary mapping the length
# of a rod to the price you can get for it, determine the max
# value you can obtain by cutting the rod into smaller pieces.
# You may cut the rod into as many pieces as necessary to
# obtain the max value.

#This dynamic programming method takes two parameters, a length and
#a dictionary that is a hashmap. it checks for the edge cases and then
#returns 0 if so. The program creates a new array to keep track of the max
#rod sums at specific rod lengths, and each call in the iteration checks
#all possible cuts and updates the max. The final max would be at the end
#of the stored list. This is run in O(n^2) time and O(n) space for the extra
#array
def rod_cutter(length, prices):
    if (length == 0)or (prices == None):
        return 0
    arr = [0 for g in range(length)]
    val = 0
    for x in range (0,length):
        if (x+1 in prices):
            arr[x] = prices[x+1]
        if (x > 0):
            q = int(x/2)+1
            for y in range(0,q):
                val = arr[y] + arr[x-y-1]
                if (arr[x]<val):
                    arr[x] = val
    return arr[length-1]
