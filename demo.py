import time
import random


def partition(nums, lI, rI):
    pivot = nums[lI]
    i, j = lI + 1, rI

    while True:
        # 从左往右 找到大于pivot的元素
        while nums[i] <= pivot and i < rI:
            i += 1
        # 从右往左 找到小于等于pivot的元素
        while nums[j] > pivot and j > lI:
            j -= 1
        if i < j:
            (nums[i], nums[j]) = (nums[j], nums[i])
            i, j = i + 1, j - 1
        else:
            break

    # 此时j指向的是 最后一个 小于等于pivot的元素
    # 与pivot交换后, 能够保证左边元素都小于等于pivot, 右边元素都大于pivot
    (nums[lI], nums[j]) = (nums[j], nums[lI])
    return j

def rand_partition(nums, lI, rI):
    # 随机选取主元, 并交换到首位
    i = random.randint(lI, rI)
    (nums[lI], nums[i]) = (nums[i], nums[lI])
    return partition(nums, lI, rI)

def rand_quicksort(nums, lI, rI):
    if lI < rI:  # nums[lI,rI].length >= 2
        posI = partition(nums, lI, rI)
        rand_quicksort(nums, lI, posI - 1)
        rand_quicksort(nums, posI + 1, rI)



start_time = time.time()
for _ in range(100000):
    nums = random.sample(range(100000), 100)
    rand_quicksort(nums, 0, len(nums) - 1)
end_time = time.time()


print("Time cost: ", end_time - start_time)

for i in range(1, len(nums)):
    assert nums[i] >= nums[i - 1]