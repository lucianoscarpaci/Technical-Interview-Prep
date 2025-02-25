def max_audience_performances(audiences):
    max_audience = 0
    max_audience_performances = []
    for audience in audiences: # 120, 180, 220, 150, 220
        if audience > max_audience:
            max_audience = audience
            max_audience_performances = audience
        elif audience == max_audience:
            max_audience_performances += audience
    return max_audience_performances

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
