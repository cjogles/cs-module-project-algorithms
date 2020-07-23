'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     sorted_arr = []
#     zeroes = []
#     result = []
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             zeroes.append(0)
#         else: 
#             sorted_arr.append(arr[i])
#     for i in sorted_arr:
#         result.append(i)
#     for i in zeroes:
#         result.append(i)
#     return result

#optimize:
def moving_zeroes(arr):
    # if left is zero, and right is non zero => swap, then increment left, decrement right
    # if left is non-zero => increment left
    # if right is zero => decrement right
    # if left > right, stop
    left = 0
    right = len(arr)-1
    while left <= right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        else: 
            arr_left = arr[left]
            arr_right = arr[right]
            if arr[left] != 0:
                left += 1
            if arr[right] == 0:
                right -= 1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")