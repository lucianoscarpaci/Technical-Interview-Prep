def arrange_guest_arrival_order(arrival_pattern):
    guest_order = []
    digits = []
    n = len(arrival_pattern)
    for i in range(n + 1):
        digits.append(str(i + 1))
        if i == n or arrival_pattern[i] == "I":
            while digits:
                guest_order.append(digits.pop())
    return guest_order


print(arrange_guest_arrival_order("IDID"))
print(arrange_guest_arrival_order("III"))
