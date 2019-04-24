# input = open("../student/networkroute.txt", "r")
input = open("../sample_data/networkroute.txt", "r")
lines = input.readlines()
computers = []
names = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
source = 0
dest = 0
for line in lines:
    parts = line.split(',')
    if line.startswith('Message'):
        source = names[parts[0][-1]]
        dest = names[parts[1].strip()]
    else:
        computers.append([p.strip() for p in parts[1:]])

def shortest_route(computers, source, dest, visited):
    if source == dest:
        return 0
    new_sources = [names[x] for x in computers[source] if names[x] not in visited]
    return min(1 + shortest_route(computers, new_source, dest, visited+[new_source]) for new_source in new_sources)

print(shortest_route(computers, source, dest, [source]))
