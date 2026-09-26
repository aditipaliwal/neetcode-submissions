class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        iters = {}
        i=0
        majority_element_occurance = 0
        majority_element = 0
        while i < len(nums):
            if nums[i] in iters.keys():
                iters[nums[i]] +=1
            else:
                iters[nums[i]]=1
            i+=1
        for key, val in iters.items():
            if val > majority_element_occurance:
                majority_element_occurance = val
                majority_element = key 
        return majority_element