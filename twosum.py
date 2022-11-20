#We will create a dicitionary that will hold every value's index in the list
#as value and the original value as it's key
#e.g; consider a list, [2,3,4]
#the dicitionary will look like this--> 
#{2:0, 3:1, 4:2}
#at the meantime in the loop we check if the diff. btw.
#the target and the current value is already exists in the dict. as a key
#if it exists we will return the key's value and the current index
#else will keep on adding the current value and it's key top the dict
def twosum(nums, target):
    values = {}
    for idx, num in enumerate(nums):
        if target - num in values:
            return [values[target - num], idx]
        else:
            values[num] = idx

print(twosum([5,3,4,0,2],5))
