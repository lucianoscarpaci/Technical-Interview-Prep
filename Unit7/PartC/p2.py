def reverse_helper(words):
    if len(words) == 0:
        return ""
    if len(words) == 1:
        return words[0]
    return reverse_helper(words[1:]) + " " + words[0]

def reverse_orders(sandwich):
    words = sandwich.split()
    return reverse_helper(words)

print(reverse_orders("Bagel Sandwich Coffee"))