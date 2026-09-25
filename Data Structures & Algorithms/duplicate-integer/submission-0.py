class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates_hash = {}

        for num in nums:
            if num in duplicates_hash:
                return True
            duplicates_hash[num] = 1

        return False