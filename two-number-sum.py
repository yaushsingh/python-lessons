""" #using for loops 
#runs at O(n^2) time and O(1) space 
def twoNumberSum(array, targetSum):
    for i in range (len(array)-1): # -1 is used for going upto second last element
        firstNum = array[i]
        for j in range(i+1,len(array)):
            secoundNum = array[j]
            if firstNum + secoundNum == targetSum:
                return [firstNum,secoundNum] #retuning an array
    return[] #returns empty array if we never hit above return [ firstnum, secondnum] """

#O(n) time/O(n) space
#using hash tables
def twoNumberSum(array,targetSum):
    nums = {} #dictionary hash tables
    print(type(nums))
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch,num]
        else:
            nums[num] = True 

    return []

#o(nlog(n)) time / O(1) space 
def tns(array,targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
        currentSum = array[left]+ array[right]
        if currentSum == targetSum:
            return [array[left],array[right]]
        elif currentSum < targetSum:
            left += 1 
        elif currentSum > targetSum:
            right -= 1
    return []




array = []
lenarray = int(input("please enter length of array"))
try:
    for i in range(lenarray):
        x = int(input("please enter elements"))
        array.append(x)
except ValueError:
    exit ('Enter integer only')

targetSum = int(input('enter the target sum'))
print(twoNumberSum(array,targetSum))    
print(tns(array,targetSum))