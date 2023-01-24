from enum import Enum, IntEnum
import random
import time

print("""---------- Zombie Hunter ----------

Coronavirus evolved and infected citizens.
The main danger is the virus can spread through the TV! 
Stop it before your family get infected!
You need to kill them before it spread everywhere! \n""")

time.sleep(0.5)
print("Loading the game... Please wait. \n")
time.sleep(2)

Player_Stats = Enum("Player_Stats", ["HP", "AttackPower", "Block", "Gold", "Mana"])

playerStatsDict = {Player_Stats.HP: 100,
                   Player_Stats.AttackPower: 7,
                   Player_Stats.Block: 35,
                   Player_Stats.Gold: 0,
                   Player_Stats.Mana: 0}

playerStatsValues = list(playerStatsDict.values())

Floor_Tickets = Enum("Floor_Tickets", ["Floor1", "Floor2", "Floor3"])

floorTicketsDict = {
                    Floor_Tickets.Floor1: 0,
                    Floor_Tickets.Floor2: 0,
                    Floor_Tickets.Floor3: 0,
                    }

floorTicketsValues = list(floorTicketsDict.values())


def shop_panel():
    shopBool = True
    while shopBool == True:
        print("------------------------------------------------- \n")
        print("""           ---------- SHOP ----------
        [******** (1) RANDOM CHEST  ********]
        [******** (2) HEALTH POTION ********]
        [******** (3) TOTAL GOLD    ********]
        [******** (4)   EXIT        ********]\n""")
        print("------------------------------------------------- \n")


        ChestChanceToDrop = Enum('ChestChanceToDrop', ["Common", "Rare", 'Epic', 'Legendary'])

        ItemsToDrop = Enum("ItemsToDrop", ["B.F_Sword", "Silver_Shield", "Amulet_of_Health", "Ring_of_Mana"])

        chestChanceDictionary = {ChestChanceToDrop.Common: 0.70,
                                 ChestChanceToDrop.Rare: 0.20,
                                 ChestChanceToDrop.Epic: 0.06,
                                 ChestChanceToDrop.Legendary: 0.04}

        chestColourList = list(chestChanceDictionary.keys())
        chestColourProbability = list(chestChanceDictionary.values())

        lootFromChest = {ChestChanceToDrop.Common: {"Small_Sword": 5},
                         ChestChanceToDrop.Rare: {"Cooper_Shield": 5},
                         ChestChanceToDrop.Epic: {"Big_Sword": 10},
                         ChestChanceToDrop.Legendary: {"Silver_Shield": 10}}

        itemsDict = list(lootFromChest.values())

        smallSword = list(itemsDict[0].keys())
        cooperShield = list(itemsDict[1].keys())
        bigSword = list(itemsDict[2].keys())
        silverShield = list(itemsDict[3].keys())

        itemNames = []

        itemNames.extend(smallSword)
        itemNames.extend(cooperShield)
        itemNames.extend(bigSword)
        itemNames.extend(silverShield)

        bigSwordValue = list(itemsDict[0].values())
        silverShieldValue = list(itemsDict[1].values())
        amuletOfHealthValue = list(itemsDict[2].values())
        ringOfManaValue = list(itemsDict[3].values())

        itemValues = []

        itemValues.extend(bigSwordValue)
        itemValues.extend(silverShieldValue)
        itemValues.extend(amuletOfHealthValue)
        itemValues.extend(ringOfManaValue)

        inventoryList = []

        shopChoice = int(input("What would you like to do? \n"))

       #ShopPlayer_Choice = IntEnum("ShopPlayer_Choice", "Chest Potion Gold Exit")



        if shopChoice == 1:
            if playerStatsValues[3] >= 100:
                drawnChest = random.choices(chestColourList, chestColourProbability)[0]
                print(f"You have drawn a {drawnChest.name} Chest. \n")
                playerStatsValues[3] -= 100
                time.sleep(1)
                print(drawnChest)
                if drawnChest == ChestChanceToDrop.Common:
                    print(f"You have drawned {itemNames[0].replace('_', ' ')}. It gives you {itemValues[0]} AP. ")
                    playerStatsValues[1] += itemValues[0]
                    inventoryList.append("Small_Sword")
                    print(inventoryList)
                    time.sleep(1)
                elif drawnChest == ChestChanceToDrop.Rare:
                    print(f"You have drawned {itemNames[1].replace('_', ' ')}. It gives you {itemValues[1]} block. ")
                    playerStatsValues[2] += itemValues[1]
                    inventoryList.append("Cooper_Shield")
                    print(inventoryList)
                    time.sleep(1)
                elif drawnChest == ChestChanceToDrop.Epic:
                    print(f"You have drawned {itemNames[2].replace('_', ' ')}. It gives you {itemValues[2]} AP. ")
                    playerStatsValues[1] += itemValues[2]
                    inventoryList.append(itemNames[2])
                    time.sleep(1)
                elif drawnChest == ChestChanceToDrop.Legendary:
                    print(f"You have drawned {itemNames[3].replace('_', ' ')}. It gives you {itemValues[3]} block. ")
                    playerStatsValues[2] += itemValues[3]
                    inventoryList.append(itemNames[3])
                    time.sleep(1)
                else:
                     print("You already got this item!")

            else:
                print("Not enough gold. Go back later. \n")
                time.sleep(1)

        elif shopChoice == 2:
            if playerStatsValues[3] >= 50:
                print("You have bought a Health Potion. +20 HP. ")
                playerStatsValues[0] += 20
                playerStatsValues[3] -= 50
                if playerStatsValues[0] > 100:
                    playerStatsValues[0] = 100
                    print(f'Your total HP is {playerStatsValues[0]} now.')
                    time.sleep(1)
                else:
                    print(f'Your total HP is {playerStatsValues[0]} now.')

            else:
                print("Not enough gold. \n")
                time.sleep(1)

        elif shopChoice == 3:
            print(f'You have got {playerStatsValues[3]} gold.')
            time.sleep(1)

        elif shopChoice == 4:
            shopBool = False
            print("Loading...")
            time.sleep(1)

def findApproximateValue(value, percentRange):
    lowestValue = int(value - (percentRange / 100) * value)
    highestValue = int(value + (percentRange / 100) * value)
    return random.randint(lowestValue, highestValue)

def block_enemy_attack(playerBlockRate):
    enemyHitChance = random.uniform(1, 100)
    if enemyHitChance > playerBlockRate:
        global playerBlock
        playerBlock = False
    else:
        playerBlock = True

def fight_panel(enemyHP, enemyAttackPower, gold):

    fightBool = True
    specialAttackCount = 0
    while fightBool == True:
        print("------------------------------------------------- \n")
        print("""******** (1) Attack ********
******** (2) Use Special Attack (2X DAMAGE, requires 15 mana) ********
******** (3) Spell Book (coming soon) ********\n""")
        print("------------------------------------------------- \n")

        fightChoice = int(input("What would you like to do?\n"))

        if fightChoice == 1:
            print("You're attacking an enemy...\n")
           # global ApproximatePlayerAP
            ApproximatePlayerAP = findApproximateValue(playerStatsValues[1], 25)
            enemyHP -= ApproximatePlayerAP
            time.sleep(1)
            print(f"Enemy lost {ApproximatePlayerAP} HP. Enemy HP: {enemyHP}. \n ") ## zamienic linijki aby wypisawalo enemy hp = 0 i gracza = 0 po przegranej jednej lub drugiej
            playerStatsValues[4] += 5
            time.sleep(1)

            if enemyHP <= 0:
                enemyHP == 0
                print("You won! \n")
                print(f"{gold} gold is added to your pouch! \n")
                print(f"You have gained 5 mana! Your total mana is: {playerStatsValues[4]}.\n")
                time.sleep(2)
                playerStatsValues[3] += gold
                fightBool = False

            elif enemyHP > 0:
                print("Enemy turn... \n")
                time.sleep(1)
                playerStatsValues[0] -= findApproximateValue(enemyAttackPower, 25)
                block_enemy_attack(playerStatsValues[2])
                if playerBlock == True:
                    print(f"You have successfully blocked an enemy attack due to player block chance: {playerStatsValues[2]}%! \n")
                    print(f"You have gained 5 mana! Your total mana is: {playerStatsValues[4]}.")
                    time.sleep(1)

                else:
                    print(f"You have lost {enemyAttackPower} HP. Player HP: {playerStatsValues[0]}\n")
                    print(f"You have gained 5 mana! Your total mana is: {playerStatsValues[4]}.")
                    time.sleep(1)
                    if playerStatsValues[0] <= 0:
                        playerStatsValues[0] = 0
                        print("You died... You have lost 10% of your gold.")
                        playerStatsValues[3] -= (playerStatsValues[3] * 0.1)
                        break

        elif fightChoice == 2:
            if playerStatsValues[4] >= 15:
                ApproximatePlayerAP = findApproximateValue(playerStatsValues[1], 25)
                enemyHP -= (ApproximatePlayerAP * 2)
                print(f"You have used Special Attack! Enemy lost {ApproximatePlayerAP * 2} HP. Enemy HP: {enemyHP}. \n")
                time.sleep(1)
                playerStatsValues[4] -= 15
                print("Enemy turn... \n")
                time.sleep(1)
                playerStatsValues[0] -= findApproximateValue(enemyAttackPower, 25)
                block_enemy_attack(playerStatsValues[2])

                if enemyHP <= 0:
                    enemyHP == 0
                    print("You won! \n")
                    print(f"{gold} gold is added to your pouch! ")
                    playerStatsValues[3] -= gold
                    fightBool = False

                elif playerBlock == True:
                    print(f"You have successfully blocked an enemy attack due to player block chance: {playerStatsValues[2]}%! \n")
                    time.sleep(1)

                else:
                    print(f"You have lost {enemyAttackPower} HP. Player HP: {playerStatsValues[0]}\n")
                    time.sleep(1)

                    if playerStatsValues[0] <= 0:
                        playerStatsValues[0] = 0
                        print("You died... You have lost 10% of your gold.")
                        playerStatsValues[3] -= (playerStatsValues[3] * 0.1)
                        break

            else:
                print("You can't attack now! Wait few rounds to get possibility to use your special attack! \n")
                time.sleep(1)


def battle_panel():

    Rydzyk_Blessings = Enum("Rydzyk_Blessings",["Good", "Bad"])


    blessingsDict = {Rydzyk_Blessings.Good: 0.5,
                     Rydzyk_Blessings.Bad: 0.5}

    blessingsKeys = list(blessingsDict.keys())
    blessingsProbability = list(blessingsDict.values())




    battleBool = True
    while battleBool == True:
        print("------------------------------------------------- \n")
        print("""   ---------- Battle Menu ----------
[********  (1) First floor    ********]
[******** (2) Second floor    ********]
[********  (3) Third floor    ********]
[********  (4) Fourth floor   ********]
[********   (5) EXIT          ********]
    * To reach higher floor you need to complete the one under. *\n""")
        print("------------------------------------------------- \n")

        floorChoice = int(input("Which floor do you wanna go?\n"))

        if floorChoice == 1:
            print("-------------------------------------------------")
            print("You see infected zombie. \n")
            time.sleep(1)
            floorTicketsValues[0] += 1
            fight_panel(20, 5, 50)


        elif floorChoice == 2:
            if floorTicketsValues[0] >= 1:
                print("-------------------------------------------------")
                print("You see infected boosted zombie. \n")
                time.sleep(1)
                fight_panel(30, 7, 75)
                floorTicketsValues[1] += 1
            else:
                print("You need to complete the first floor!")
                time.sleep(1)

        elif floorChoice == 3:
            if floorTicketsValues[1] >= 1:
                print("-------------------------------------------------")
                print("You see infected military zombie. \n")
                time.sleep(1)
                fight_panel(40, 10, 100)
                floorTicketsValues[2] += 1
            else:
                print("You need to complete the second floor!")
                time.sleep(1)

        elif floorChoice == 4:
            if floorTicketsValues[2] >= 1:
                rydzykBlessing = 1
                if rydzykBlessing == 1:
                    print("------------------------------------------------- \n ")
                    print("""You are at the highest floor at Zombie Tower.
In the corner you see a priest.
Priest is offering you a blessing. Let's what kind of blessings it is...\n """)
                    rydzykChoice = input("Do you accept it? \n")
                    time.sleep(2)
                    if rydzykChoice == "yes":
                        drawnBlessing = random.choices(blessingsKeys, blessingsProbability)[0]
                        if drawnBlessing == Rydzyk_Blessings.Bad:
                            print("""Bad priest said he saw you killing non-infected citizens!
He steals 20 HP and 2 attack power from your soul! \n""")
                            time.sleep(2)
                            playerStatsValues[0] -= 20
                            playerStatsValues[1] -= 2
                            rydzykBlessing -= 1
                        elif drawnBlessing == Rydzyk_Blessings.Good:
                            print("""Priest heals you with 30 HP and gives you 5 attack power! \n
                            ------------------------------------------------- \n """)
                            playerStatsValues[0] += 30
                            playerStatsValues[1] += 5
                            rydzykBlessing -= 1
                            if playerStatsValues[0] > 100:
                                playerStatsValues[0] = 100

                    print("You see infected enormous zombie. \n")
                    print("* Boss theme playing in the background * ")
                    time.sleep(1)
                    fight_panel(70, 10, 200)
            else:
                print("You need to complete the third floor!")
                time.sleep(1)
        elif floorChoice == 5:
            battleBool = False
            print("Loading...")
            time.sleep(1)

game = True
while game == True:
    print("------------------------------------------------- \n")
    print(f"""           ---------- MENU ----------
*       [********  (1) SHOP     ********]       *
*       [******** (2) BATTLE    ********]       *
*       [********   (3) EXIT    ********]       *

    [********  PLAYER HP: {playerStatsValues[0]}.      ********]
    [********  PLAYER AP: {playerStatsValues[1]}.      ********] 
    [********  PLAYER BLOCK: {playerStatsValues[2]}%   ********] \n""")
    print("------------------------------------------------- \n")

    mainChoice = int(input("Where do you wanna go? \n"))




    Player_Choice = IntEnum("Player_Choice", "Shop PlayerHP Battle Exit")

    if mainChoice == 1:
        print("Loading shop... \n")
        time.sleep(1)
        shop_panel()

    elif mainChoice == 2:
        if playerStatsValues[0] == 0:
            print("You need to heal yourself first. You HP is too low!")
        else:
            print("Let the battle begin! \n")
            print("Loading... \n")
            time.sleep(1)
            battle_panel()

    elif mainChoice == 3:
        game = False
        print("Loading... \n")
        time.sleep(1)

    else:
        print("Wrong choice!")
        time.sleep(1)
        continue
