def count_unique_characters(script):
    unique_characters = set()
    for character in script:
        unique_characters.add(character)
    return len(unique_characters)


script = {
    "Alice": ["Hello there!", "How are you?"],
    "Bob": ["Hi Alice!", "I'm good, thanks!"],
    "Charlie": ["What's up?"],
}
print(count_unique_characters(script))

script_with_redundant_keys = {
    "Alice": ["Hello there!"],
    "Alice": ["How are you?"],
    "Bob": ["Hi Alice!"],
}
print(count_unique_characters(script_with_redundant_keys))
