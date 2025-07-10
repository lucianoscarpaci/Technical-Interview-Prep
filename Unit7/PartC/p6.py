def decode_scroll(scroll):
    stack = []
    current_string = ""
    current_num = 0

    for char in scroll:
        if char.isdigit():
            # Build the number (could be more than one digit)
            current_num = current_num * 10 + int(char)
        elif char == "[":
            # Push the current number and current string to the stack
            stack.append((current_string, current_num))
            # Reset the current string and number
            current_string = ""
            current_num = 0
        elif char == "]":
            # Pop the last string and number from the stack
            prev_string, num = stack.pop()
            # Repeat the current string num times and add it to the previous string
            current_string = prev_string + current_string * num
        else:
            # Regular character, just add it to the current string
            current_string += char

    return current_string


def decode_scroll_recursive(scroll):
    def helper(index):
        decoded_string = ""
        while index < len(scroll):
            if scroll[index].isdigit():
                num = 0
                while index < len(scroll) and scroll[index].isdigit():
                    num = num * 10 + int(scroll[index])
                    index += 1
                index += 1
                decoded_substring, index = helper(index)
                decoded_string += decoded_substring * num
            elif scroll[index] == "]":
                return decoded_string, index + 1
            else:
                decoded_string += scroll[index]
                index += 1
        return decoded_string, index

    final_decoded_string, _ = helper(0)
    return final_decoded_string


scroll = "3[Coral2[Shell]]"
print(decode_scroll(scroll))
scroll = "4[Coral3[Shell]]"
print(decode_scroll(scroll))
scroll = "2[Poseidon3[Sea]]"
print(decode_scroll(scroll))
