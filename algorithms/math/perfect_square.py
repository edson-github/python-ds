def is_perfect_square(num):
    """
    Given a positive integer num, write a function which returns True if num is a perfect square else False.

    Note: Do not use any built-in library function such as `sqrt`.

    :type num: int
    :rtype: bool
    """
    i = 0
    while i**2 < num:
        i += 1
    return i**2 == num
        

# Test
print(is_perfect_square(16))
print(is_perfect_square(14))
