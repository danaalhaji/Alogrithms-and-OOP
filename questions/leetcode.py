def kidsWithCandies(candies, extraCandies):
    newArray = []
    result = []
    greates = candies[0]
    for i in range (1, len(candies)):
        if candies[i] > greates:
            greates = candies[i]
    print(greates)
    for j in candies:
        newArray.append(j+extraCandies)
    print(newArray)
    for a in newArray:
        if a >= greates:
            result.append(True)
        else:
            result.append(False)
    return result

'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        l=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=m:
                l.append(True)
            else:
                l.append(False)
        return l
'''

array=[1,3,9]
print(kidsWithCandies(array,4))
