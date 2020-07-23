'''
Input: an integer
Returns: an integer
'''

# recursive calls use a stack data structure
# as such its a depth first traversal to every node
# meaning it goes level by level visiting every node
# where a node is either a function call or a stack frame
# i'm going to count all the nodes that I visit, and if the nodes that I visit
# lead me to an answer below 0, then I don't count those. Because
# that would mean the cookie monster ate more cookies then were present in the cookie jar

def eating_cookies(n, cache=None):
    # recursive case
    if n > 0:
        if cache != None:
            my_sum = 0
            # if its available lets use it
            # check if I've already computed the result already, if so,
            # then return that saved result instead
            # ask cache for the n that I care about, and cache will tell if it has a value for that n available
            if n-1 >= 0 and cache[n - 1] != 0:
                my_sum += cache[n-1]
            else:
                cache[n-1] = eating_cookies(n - 1, cache)
                my_sum += cache[n-1]
            if n-2 >= 0 and cache[n - 2] != 0:
                my_sum += cache[n - 2]
            else:
                cache[n-2] = eating_cookies(n - 2, cache)
                my_sum += cache[n-2]
            if n-3 >= 0 and cache[n - 3] != 0:
                my_sum += cache[n - 3]
            else:
                cache[n-3] = eating_cookies(n - 3, cache)
                my_sum += cache[n-3]
            return my_sum
        # invoking recursively the eating_cookies funciton
        else:
            return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    # base cases
    # for chaching, I would never save anything because I would only see n = 0 or n < 0 none of which are interesting to me
    # tried eating more cookies then were there
    if n < 0:
        return 0
    # ate all the cookies successfully
    if n == 0:
        return 1


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 6

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

print(len('1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527'))