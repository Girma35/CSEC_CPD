import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def amount_sec(n, h, k, heights):
    current_height = 0
    res = 0

    for i in range(n):
        if current_height + heights[i] > h:
            res += current_height // k
            current_height %= k

            if current_height + heights[i] > h:
                res += 1
                current_height = 0

        current_height += heights[i]

    if current_height > 0:
        res += (current_height + k - 1) // k

    return res

n, h, k = map(int, input().split())
heights = list(map(int, input().split()))

print(amount_sec(n, h, k, heights))
