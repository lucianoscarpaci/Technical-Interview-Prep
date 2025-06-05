def sum_honey(hunny_jars):
    count = 0
    for i in hunny_jars:
        count += i
    return count


hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))
