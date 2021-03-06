'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# def sliding_window_max(nums, k):
#     window_sums = []
#     for i in range(len(nums)):
#         if i+k == len(nums)+1:
#             return window_sums
#         new_array = nums[i:i + k]
#         sum = new_array[0]
#         for i in new_array:
#             if i > sum:
#                 sum = i
#         window_sums.append(sum)

# optimize:
def sliding_window_max(nums, k):
    results = [0] * (len(nums) - (k - 1))
    max_idx = 0
    for j in range(0, k):
        if nums[j] > nums[max_idx]:
            max_idx = j
    for i in range(0, len(nums) - (k - 1)):
        if nums[i+k-1] > nums[max_idx]:
            max_idx = i + k - 1
        elif max_idx < i:
            max_idx = i
            for j in range(i+1, i+k):
                if nums[j] > nums[max_idx]:
                    max_idx = j
        results[i] = nums[max_idx]
    return results


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
