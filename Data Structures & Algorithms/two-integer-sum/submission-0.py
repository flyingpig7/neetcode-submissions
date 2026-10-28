class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inds = {}
        for i, n in enumerate(nums):
            if target-n in inds:
                return [inds[target-n], i]
            else:
                inds[n] = i
        