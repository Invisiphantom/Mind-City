import random


def COUNTING_SORT(nums, k, map=lambda x: x):
    out = [0] * len(nums)
    posSum = [0] * (k + 1)

    # 统计每种元素的个数 Θ(n)
    for i in range(len(nums)):
        posSum[map(nums[i])] += 1

    # 累加小于等于i的元素个数 Θ(k)
    for i in range(1, k + 1):
        posSum[i] += posSum[i - 1]

    # 从后往前遍历，保证稳定性 Θ(n)
    for i in range(len(nums) - 1, -1, -1):
        # 此时小于等于nums[i]的未分配元素个数
        leq_num = posSum[map(nums[i])]
        # nums[i]应放在这些元素的最末尾位置
        out[leq_num - 1] = nums[i]
        posSum[map(nums[i])] -= 1

    return out


def RADIX_SORT(nums, k, d):
    """k:基数, d:最大位数"""
    map = lambda x: (x // (k ** i)) % k
    for i in range(d):
        nums = COUNTING_SORT(nums, k, map)
    return nums


nums = random.sample(range(100), 10)
nums = RADIX_SORT(nums, 10, 2)
print(nums)
