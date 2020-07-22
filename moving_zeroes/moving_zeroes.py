'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    sorted_arr = []
    zeroes = []
    result = []
    for i in range(len(arr)):
        if arr[i] == 0:
            zeroes.append(0)
        else: 
            sorted_arr.append(arr[i])
    for i in sorted_arr:
        result.append(i)
    for i in zeroes:
        result.append(i)
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")