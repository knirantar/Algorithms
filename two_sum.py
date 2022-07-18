'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''


def array_two_sum(arr, target):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                print(i, j)
                break


# For above answer time complexity will be O(N^2)
# No extra space is used hence space complexity O(1)

def array_two_sum_v2(arr, target):
    d = {}

    for i in range(0, len(arr)):
        if target - arr[i] in d:
            print(d[target-arr[i]], i)
        else:
            d[arr[i]] = i


# For above answer time complexity will be O(N)
# Dictionary with extra space is used hence space complexity O(N)

array_two_sum_v2([3, 2, 4, 5], 6)
