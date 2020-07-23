'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# def single_number(arr):
#     temp = []
#     for i in arr:
#         if i in temp:
#             temp.remove(i)
#         else:
#             temp.append(i)
#     return temp[0]

# optimize:
def single_number(arr): # 0(2n) = o(n)
    counts = {}
    for i in arr: # o(n)
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1 
    for k, v in counts.items(): # o(n)
        if v == 1:
            return k 

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")