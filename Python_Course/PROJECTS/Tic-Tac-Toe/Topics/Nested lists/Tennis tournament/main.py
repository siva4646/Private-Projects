n = int(input())
players = [input() for n in range(n)]
for i in range(0, n):
    winners = 0
    winners_names = []
    if players[i].endswith('win'):
        winners += 1
        winners_names.append([i])

print(winners_names)
print(winners)