def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body. ([5], 4), ([5,10], 9), ([5, 10, 3], 2), ([5, 10, 3, 2], 1)
    return new_list

result = increment_all([4, 9, 2, 1])