def count_unique_species(ecosystem_data):
    modified_data = []
    for char in ecosystem_data:
        if char.isalpha() or char.isdigit():
            modified_data.append(char)
        else:
            modified_data.append(" ")
    modified_data = "".join(modified_data)
    # Split the string by spaces to get all species counts
    species_counts = modified_data.split()
    # Convert counts to integers to remove leading zeros
    print(species_counts)
    unique_counts = set()
    for count in species_counts:
        print(count)
        if count:
            unique_counts.add(count)  
    return len(unique_counts)


ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print(count_unique_species(ecosystem_data1))
print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))
