"""Summation"""

def sum(n):
    """Return the sum of the first n natural numbers.

    >>> sum(10)
    55
    >>> sum(100)
    5050
    """
    i, total = 0, 0
    while i<=n:
        i, total = i+1, total+i
    return total

def sum_test():
    assert sum(5)==15, "sum of 1 to 5 should be 15"
    assert sum(10)==55, "sum of 1 to 10 should be 55"
    assert sum(100)==5051, "sum of 1 to 100 should be 5051, (this is false on purpose)"