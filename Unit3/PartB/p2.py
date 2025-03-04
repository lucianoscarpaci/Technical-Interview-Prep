from collections import deque

def process_performance_requests(requests):
    q = sorted(requests, key=lambda x: x[0])

    q = deque(q)

    performance_types = []

    while q:
        priority, performance_type = q.popleft()
        performance_types.append(performance_type)
    return performance_types[::-1]

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))