class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            nums.insert(0,nums[-1])
            nums.pop()
        """
        Do not return anything, modify nums in-place instead.
        """
        