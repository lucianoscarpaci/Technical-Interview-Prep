def can_place_flowers(flowerbed, n):
    count = 0
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0:
            # Check if the previous and next plots are empty or out of bounds
            if (i == 0 or flowerbed[i - 1] == 0) and (
                i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            ):
                flowerbed[i] = 1  # Plant a flower here
                count += 1
        i += 1
    return count >= n


flowerbed = [1, 0, 0, 0, 1]
n = 1
print(can_place_flowers(flowerbed, n))
