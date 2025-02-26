#function takes in a list of dictionaries named species_list
# as a parameter. Each dictionary represents data about a species
# including its name, habitat, and population. The function should
# return the name of the species with the smallest population.

def most_endangered(species_list):
    smallest_population = species_list[0].get("population")
    name = species_list[0].get("name")
    for species in species_list:
        population = species.get("population")
        if population < smallest_population:
            smallest_population = population
            name = species.get("name")
    return name

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))