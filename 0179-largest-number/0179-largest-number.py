class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = map(str,nums)
        
        nums = sorted(nums, key=CustomSmallerNumber)[::-1]
        
        answer = ''.join(nums)
        
        if answer[0] == "0":
            return "0"
        else:
            return answer
    

class CustomSmallerNumber(str):
    def __lt__(self, other):
        return self + other < other + self
    
    
    
"""
__lt__ is a magic method that lets you change the behavior of the < operator. sorted uses the < operator to compare values. So when python is comparing two values with < it checks to see if those objects have the magic method __lt__ defined. If they do, then it uses that method for the comparison. The variables x and y in the example are the two variables being compared. So if you had a line of code like x < y, then x and y would be passed as arguments to __lt__. Sorted presumably does have that line of code. But you don't have to call them 'x' and 'y', you can call them whatever you want. Often you will see them called self and other.

sorted works by comparing two items at a time. For example, let's call them x and y. So somewhere sorted has to compare them, probably with a line that looks like:

if x < y:
However, if you pass sorted a key argument, then it instead compares them more like this:

if key(x) < key(y):
Since the example passes LargerNumKey as the key, it ends up looking like this after python looks up key:

if LargerNumKey(x) < LargerNumKey(y):
When python then sees the < operator, it looks for the __lt__ method, and because it finds it turns the statement into basically:

if LargerNumKey(x).__lt__(LargerNumKey(y)):
Because __lt__ is a method on an object, the object itself becomes the first argument (x in this case). Also, because LargerNumKey is a subclass of str it behaves exactly like a regular string, except fo the __lt__ method that you overrode.

This is a useful technique when you want things to be sortable. You can use __lt__ to allow your objects to be sorted in any way you wish. And if the objects you are sorting have the __lt__ method defined, then you don't have to even pass key. But since we are working with different types of objects and don't want to use the default __lt__ method, we use key instead.

"""
    

        