# You are given a 0-indexed integer array species_populations of even
# length, where each element represents the population of
# a particular species in a wildlife reserve.
def distinct_averages(species_populations):
  # find the species with the minimum population and use .remove() to remove it
  #min_species = min(species_populations) # 200
  #species_populations.remove(min_species) # 300
  #first = species_populations[0] # 300 # 
  #second = min_species
  # return int((first + second) / 2)
  species_populations.sort()
  average = set()
  l, r = 0, len(species_populations) - 1
  while l < r:
    average.add((species_populations[l] + species_populations[r]) / 2)
    l += 1
    r -= 1
    return len(average)
    
species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]
print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 