import sys

def max_consecutive_ones(n):
    binary_rep = bin(n)[2:]
    ones_groups = binary_rep.split('0')
    max_ones = max(len(group) for group in ones_groups)
    return max_ones

if __name__ == '__main__':
    n = int(input().strip())
    print(max_consecutive_ones(n))
    