# Understand: It looks like a problem using stack and calculating the cost
# of supply. We need to calculate the cost of supply for each item.
# Plan: Make final_cost a copy of costs to store the prices
# Make empty stack to keep track of items that have not had discout yet.
# Iterate through each item and check the stack:
# When the stack is not empty and the item cost is less than or equal to the cost
# of the item at the top of the stack, pop the item from the stack and apply the discout.
def final_supply_costs(costs):
    n = len(costs)
    stack = []
    final_costs = costs[:]

    for i in range(n):
        while stack and costs[stack[-1]] >= costs[i]:
            j = stack.pop()
            final_costs[j] -= costs[i]
        stack.append(i)
    return final_costs


print(final_supply_costs([8, 4, 6, 2, 3]))
print(final_supply_costs([1, 2, 3, 4, 5]))
print(final_supply_costs([10, 1, 1, 6]))
"""
[4, 2, 4, 2, 3]
[1, 2, 3, 4, 5]
[9, 0, 1, 6]
"""
