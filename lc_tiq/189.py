# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# #1 - if k > n => k % n gives the index that should be the first element. So copy over from that element to end, and put it before the first section of the array

from typing import List

class Solution2:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

        return nums


sol2 = Solution2()


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        return nums[-k:] + nums[:-k]

sol = Solution()

nums = [1,2,3,4,5,6,7]

print(sol2.rotate([1,2,3,4,5,6,7], 3))

print(sol2.rotate([-1,-100,3,99], 2))

print(sol2.rotate([1,2,3,4,5,6,7], 10))

print(sol2.rotate([1,2,3,4,5,6,7], 14))
