def move_zeroes(lst):
    #Find the number of zeroes in the list
    count = 0
    for num in lst:
        if num == 0:
            count += 1
   # move all zeros to the end of the list
    for i in range(count):
        lst.remove(0)
        lst.append(0)
    print(lst)
    return lst 

lst = [1, 0, 2, 0, 3, 0]
move_zeroes(lst)