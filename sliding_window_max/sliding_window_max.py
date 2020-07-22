'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    window_sums = []
    for i in range(len(nums)):
        if i+k == len(nums)+1:
            return window_sums
        new_array = nums[i:i + k]
        sum = new_array[0]
        for i in new_array:
            if i > sum:
                sum = i
        window_sums.append(sum)


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1,3,-1,-3,5,3,6,7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
