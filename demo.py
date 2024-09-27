# 计数排序

def COUNTING_SORT(nums, out, k):
    posSum = [0] * (k + 1)
    # 统计每种元素的个数
    for i in range(len(nums)):
        posSum[nums[i]] += 1
    # 累加小于等于i的元素个数
    for i in range(1, k + 1):
        posSum[i] += posSum[i - 1]
    # 从后往前遍历，保证稳定性
    for i in range(len(nums) - 1, -1, -1):
        out[posSum[nums[i]] - 1] = nums[i]
        posSum[nums[i]] -= 1


A = [2, 5, 3, 0, 2, 3, 0, 3]
B = [0] * len(A)
k = max(A)
COUNTING_SORT(A, B, k)
print(B)