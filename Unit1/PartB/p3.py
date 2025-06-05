def delete_minimum_elements(hunny_jar_sizes):
    remove_elements = []
    while hunny_jar_sizes:
        min_element = min(hunny_jar_sizes)
        
        remove_elements.append(min_element)
        hunny_jar_sizes.remove(min_element)
    return remove_elements
    

hunny_jar_sizes = [5, 4, 3, 2, 1]
print(delete_minimum_elements(hunny_jar_sizes))