'''
Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order.
'''


def topKFrequent( nums ,k) :
    _dict={}
    result=[]
    for i in nums:
        _dict[i]=0
    for i in nums:
        if i in _dict.keys():
            _dict[i] += 1
    print(_dict)
    
    _dict=dict(sorted(_dict.items(), key=lambda x:x[1], reverse = True))
    sorted_dict=dict(_dict)
    print(sorted_dict)
    for i in range(0,k):
        res = list(sorted_dict.keys())[i]
        print(res)
        result.append(res)
    return result
    
num=[3,0,1,0]
print(topKFrequent(num,1))

'''
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_arr = []
        count_nums = Counter(nums)
        sort_val = set(sorted(count_nums.values())[::-1][:k])
        for key in count_nums:
            if count_nums[key] in sort_val:
                f_arr.append(key)
        return f_arr
'''