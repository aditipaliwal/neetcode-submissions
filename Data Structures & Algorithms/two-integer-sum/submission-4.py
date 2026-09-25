class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions = {}
        for i in range(len(nums)):
            if (2*nums[i] == target and (nums[i] in positions.keys())):
                return [positions[nums[i]],i]
            else:
                positions[nums[i]]=i
            
        for key in positions.keys():
            if (target - key) in positions.keys() and (key!=target - key):
                return [positions[key],positions[target - key]]