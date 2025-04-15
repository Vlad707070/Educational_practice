def replay(nums):
    return len(nums) != len(set(nums))

nums1 = [1,2,3,4]
nums2 = [1,1,1,3,3,4,3,2,4,2]
nums3 = [1,2,3,1]

print(replay(nums1))
print(replay(nums2))
print(replay(nums3))
