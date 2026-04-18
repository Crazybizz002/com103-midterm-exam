heroes = [
    "",  
    ["Layla", "Marksman"],
    ["Tigreal", "Tank"],
    ["Gusion", "Assassin"],
    ["Kagura", "Mage"],
    ["Chou", "Fighter"]
]

ign = input("In-game name (IGN): ")
rank = input("Current rank: ")

print("\nHERO ROSTER")
for i in range(1, 6):
    print(i, heroes[i][0], "-", heroes[i][1])

print("\n")

matches = []
wins = 0
losses = 0


for i in range(4):
    print("MATCH", i + 1)

    hero = int(input("Hero number (0 to skip): "))

    if hero == 0:
        print("Skipped\n")
        continue

    if hero < 1 or hero > 5:
        print("Invalid hero\n")
        continue

    kills = int(input("Kills: "))
    deaths = int(input("Deaths: "))
    assists = int(input("Assists: "))
    result = input("Result (W/L): ").upper()

    
    if deaths == 0:
        deaths = 1

    kda = (kills + assists) / deaths

    
    if result == "W":
        wins = wins + 1
    else:
        losses = losses + 1

    
    if kda >= 5 and result == "W":
        tag = "DOMINATION!"
    elif kda >= 5 and result == "L":
        tag = "Carried Hard"
    elif kda < 5 and result == "W":
        tag = "Team Effort"
    else:
        tag = "Better Luck Next Game"

    matches.append([hero, kda, result, tag])
    print("\n")


best_index = 0
for i in range(len(matches)):
    if matches[i][1] > matches[best_index][1]:
        best_index = i


total_matches = len(matches)

if total_matches == 0:
    win_rate = 0
else:
    win_rate = int((wins / total_matches) * 100)


print("\n==============================")
print(ign, "-", rank)
print("==============================")

for i in range(len(matches)):
    hero_name = heroes[matches[i][0]][0]
    kda = matches[i][1]
    result = matches[i][2]
    tag = matches[i][3]

    print(i + 1, hero_name, "| KDA:", round(kda, 2), "|", result, "|", tag)

print("------------------------------")
print("Wins:", wins)
print("Losses:", losses)
print("Win Rate:", win_rate, "%")

if len(matches) > 0:
    best_hero = heroes[matches[best_index][0]][0]
    best_kda = matches[best_index][1]
    print("Best Match:", best_hero, "with KDA", round(best_kda, 2))

print("==============================")
