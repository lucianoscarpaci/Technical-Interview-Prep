def max_k_repeating(sequence, move):
    k = 0
    while (move * (k+1)) in sequence:
        k += 1
    return k

print(max_k_repeating("airairwater", "air"))
print(max_k_repeating("fireearthfire", "fire"))
print(max_k_repeating("waterfire", "air"))
print(max_k_repeating("waterwater", "water"))