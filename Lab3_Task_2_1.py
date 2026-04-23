def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body. 4, 13, 15, 16
    return total

result = tally([4, 9, 2, 1])