def hulk_smash(n):
    answer = []
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("Hulksmash")
        elif i % 3 == 0:
            answer.append("Hulk")
        elif i % 5 == 0:
            answer.append("Smash")
        else:
            answer.append(str(i))
    return answer


n = 3
print(hulk_smash(n))
n = 5
print(hulk_smash(n))
n = 15
print(hulk_smash(n))
