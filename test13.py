players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

players_dic = {}
for n, player in enumerate(players):
    players_dic[player] = n
    print(n)
for call in callings:
    n = players_dic[call]
    players_dic[call] -= 1
    players_dic[players[n-1]] += 1
    players[n], players[n-1] = players[n-1], players[n]
print(players)
