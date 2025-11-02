# Use binary search to find Kth bit in Nth Binary String
def find_kth_bit(n, k):
    if n == 1:
        return "0"

    length = 2**n - 1
    mid = length // 2 + 1

    if k == mid:
        return "1"
    elif k < mid:
        return find_kth_bit(n - 1, k)
    else:
        bit = find_kth_bit(n - 1, length - k + 1)
        return "1" if bit == "0" else "0"


n = 4
k = 11
print(find_kth_bit(n, k))  # Output: '1'
n = 3
k = 1
print(find_kth_bit(n, k))  # Output: '0'
