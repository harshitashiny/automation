class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        n = len(arr)
        mid = (n + 1) // 2
        nums[::2] = arr[:mid][::-1]
        nums[1::2] = arr[mid:][::-1]