def manage_character_arc(events):
    stack = []
    processed_arc = []
    for event in events:
        stack.append(event)
        processed_arc.append(stack.pop())
    return processed_arc


events = [
    "Character is introduced.",
    "Character faces a dilemma.",
    "Character makes a decision.",
    "Character grows stronger.",
    "Character achieves goal.",
]

processed_arc = manage_character_arc(events)
print(processed_arc)

events = [
    "Character enters a new world.",
    "Character struggles to adapt.",
    "Character finds a mentor.",
    "Character gains new skills.",
    "Character faces a major setback.",
    "Character overcomes the setback.",
]

processed_arc = manage_character_arc(events)
print(processed_arc)