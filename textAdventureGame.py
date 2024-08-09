#Imports
import random

def main():
    encounterProb = 80  # probability of encountering a monster
    #List of gold , lowest damage, highest damage, charcter health,player strength,sword,armor,gun, player shield   
    dataAmount = [100,1,10,100,0,0,0,0,0]
    damagerange = random.randint(0,10)
    print()
    #Introduction to the game 
    print("Welcome to our fantasy RPG!")
    print("There are ten encounters that will occur throughout this game")
    print("This is an interactive game to keep you thinking on your decision throughout")
    print("Good luck defeating the monster and surviving!")
    print()
    rulesgame()
    step = 0
    monsterDictionary = readfile()
    print()
    print("You are a player in a dungeon.")
    print("There are different types of monsters that are in the dungeon")
    print("You have to start your adventure to surivive safely.")
    print("Make sure to choose the correct direction.Choose carefully!")
    print()
    print("These are your stats at the beginning of the game")
    printPlayerStats(dataAmount)
    while step < 10:
        playerHP = dataAmount[3]
        choice = mainMenu(dataAmount)
        if random.randint(0, 100) < encounterProb:
            storechoice = input("\nDo you want to shop at the store(yes/no)?")
            while storechoice != "no" and storechoice != "yes":
                storechoice = input("\nDo you want to shop at the store(yes/no)?")
            if storechoice == "yes":
                store(dataAmount)
            battle(monsterDictionary,dataAmount)
            playerHP = dataAmount[3]
        else:
            storechoice = input("\nDo you want to shop at the store(yes/no)?")
            while storechoice != "no" and storechoice != "yes":
                storechoice = input("\nDo you want to shop at the store(yes/no)?")
            if storechoice == "yes":
                store(dataAmount)
            print("\nThe room is empty.")
        printPlayerStats(dataAmount)
        step = step + 1
        if playerHP <= 0:
            playerHP = dataAmount[3] 
            step = 100
            print("Your're player has died!")
    print("Thank you for playing the game")
    print("\nYou exit the adventure with" , str(dataAmount[0]) , "gold")

#Shop with the gold that the player will be able to buy within the 10 rounds of the game 
def store(dataAmount):
    print()
    print("Welcome to the Store!")
    print("You will have a chance to shop at the store each round")
    print("The Store's stock today includes: ")
    print("1: +2 to sword costs:  75 gold.")
    print("2: +1 to armor costs: 50 gold.")
    print("3: +2 gun and +2 sheild cost: 100 gold.")
    print("4: +2 player strength cost: 75 gold.")
    purchaseOption = -1
    while(purchaseOption != 0):
        try:
            while((purchaseOption != 0) and (purchaseOption != 1) and (purchaseOption != 2) and (purchaseOption != 3) and (purchaseOption != 4)):
                purchaseOption = int(input("Type the number of the object you'd like to buy.  Type 0 to exit"))
            if(purchaseOption != 0):
                #If statement, selecting the exact item for purchase
                if(purchaseOption == 1) and dataAmount[0] >= 50:
                    dataAmount[0] -= 75 
                    dataAmount[5] += 1
                    print("The level of your sword has been upgraded to :" , dataAmount[5])
                    print("You currently have:" , dataAmount[0] ,"gold left")
                    print("Thanks for shopping here!")
                    print("Thanks for your purchase!")
                elif(purchaseOption == 2) and dataAmount[0] >=15:
                    dataAmount[0] -= 50
                    dataAmount[6] += 1
                    print("The level of your armor has been upgraded to :" , dataAmount[6])
                    print("You currently have:" , dataAmount[0] ,"gold left")
                    print("Thanks for shopping here!")
                    print("Thanks for your purchase!")
                elif(purchaseOption == 3) and dataAmount[0] >= 75:
                    dataAmount[0] -= 100  
                    dataAmount[7] += 1 
                    dataAmount[8] += 1
                    print("The level of your gun and sheild has been upgraded to :" , dataAmount[7])
                    print("You currently have:" , dataAmount[0] ,"gold left")
                    print("Thanks for shopping here!")
                    print("Thanks for your purchase!")
                elif(purchaseOption == 4) and dataAmount[0] >= 40:
                    dataAmount[0] -= 75
                    dataAmount[4] += 1
                    print("The level of your strength has been upgraded to :" , dataAmount[4])
                    print("You currently have:" , dataAmount[0] ,"gold left")
                    print("Thanks for shopping here!")
                    print("Thanks for your purchase!")
            #Check if the user has enough gold 
                else:
                    print("Not enough coins!")
                purchaseOption = -1
        except ValueError:
            print("This was not a valid integer")

#Reads in the file and check input validation to make sure that the sure inputs the correct file name 
def readfile():
    a = True 
    while a:
        try:
            infile = input("Enter the monster file name: (.txt)")
            while not infile.endswith(".txt"):
                infile = input("Invalid file name! Enter another monster file name: (.txt)")
            openFile = open(infile,"r")
            a = False
        except FileNotFoundError:
            print("There is no file that exists.")
    md = {}
    monster = openFile.readline()
    while monster != "":
        split = monster.split(";")
        md[split[0]] = [int(intsplit)for intsplit in split[1:]]
        monster = openFile.readline()
    return md
        
#display the menu and returns the desired move 
def mainMenu(dataAmount):
    #Adds to the storyline
    adventurechoice = ["You are in a castle that is dark.", "You are in the middle of the woods." , "You are in the middle of a rural area."]
    randAdventureChoice = random.choice(adventurechoice)
    print(randAdventureChoice)
    print("What do you want to do?")
    if dataAmount[0] > 0:
        move = input("Move (n)orth, (s)outh, (e)ast, (w)est, or (r)est>") 
        while  move != "n" and move != "s" and  move != "e" and move != "w" and move != "r":
            move = input("Move (n)orth, (s)outh, (e)ast, (w)est, or (r)est")
            if move == "n" and move == "e" and move == "s" and move == "w" and move == "r" and dataAmount[0] > 0:
                return move
#Adds the level of each print
#Print the player stats and show the information 
def printPlayerStats(dataAmount):
    print()
    print("******************************")
    print("Player Gold:" , dataAmount[0])
    print("Player Health:" , dataAmount[3])
    print("Player Strength Level:" ,  dataAmount[4])
    print("Player Sword Level:" , dataAmount[5])
    print("Player Armor Level:" , dataAmount[6])
    print("Player Gun Level:" , dataAmount[7])
    print("Player Sheild Level:" , dataAmount[8])
    print("******************************") 
    print()

#Loops until there is a winner in the game  
def battle(md,dataAmount):
    mKey = selectMonster(md)
    #continue the storyline
    walking = ["in the rain forest" , " in the desert" , "in the mountains"]
    randwalking = random.choice(walking)
    print()
    print("You are walking" , randwalking , "\nand you have encountered a" , mKey)
    print("What do you think is best to do?")
    monsterHP = random.randint(md[mKey][1] , md[mKey][2])
    monsterGold = random.randint(md[mKey][5] , md[mKey][6])
    playerHP = dataAmount[3] 
    print()
    while playerHP > 0 and monsterHP > 0:
        playerDMG = random.randint(dataAmount[1],dataAmount[2])
        monsterDMG = random.randint(md[mKey][3] , md[mKey][4])
        playerDMG += dataAmount[5] * 2 
        monsterDMG -= dataAmount[6] 
        playerDMG += dataAmount[7] * 2
        monsterDMG -= dataAmount[8] * 2
        playerDMG += dataAmount[4] * 2
        print("If you deicde to cast a spell, you will alter the enemy's stats")
        fightchoice = input("Do you decide to  (f)ight the monster , (r)un away , c)ast a spell")
        if fightchoice != "f" and fightchoice != "r" and fightchoice != "c":
            fightchoice = input("Do you decide to f)ight the monster , r)un away, c)ast a spell")
        print("If you deicde to cast a spell, you will alter the enemy's stats")
        if fightchoice == "f":
            monsterHP -= playerDMG
            print(f"Player gave {playerDMG} damage to the monster")
            if monsterHP > 0:
                playerHP -= monsterDMG
                print(f"Monster gave {monsterDMG}damage to the player")
                if dataAmount[6] > 0:
                    monsterDMG -= 1
                if dataAmount[8] > 0:
                    monsterDMG -= 1
            if playerHP > 0:
                monsterHP  -= playerDMG
        elif fightchoice == "r":
            print("You have decided to run away.")
            retreat = 20 
            if random.randint(1,100) < retreat:
                dataAmount[3] = playerHP
                print("You have successfully run away!")
            else:
                print("You have to fight the monster.")
                playerHP -= monsterDMG
                if playerHP > 0:
                    monsterHP -= playerDMG
                if monsterHP > 0:
                    playerHP -= playerDMG 
        elif fightchoice == "c":
            print("You have changed the monster stats: ")
            monsterDMG -= 2
            monsterHP -= 2     
            print(f"Monster's damage is currently" , {monsterDMG} , "Monster's hit point is currently" , {monsterHP})        
    dataAmount[3] = playerHP
    if playerHP > 0:
        dataAmount[0] += monsterGold 

#Returns a randomly selected key(monsters name) 
def selectMonster(md):
    # Create 2d list of monster names and likelihoods.
    allMonsters = []
    for key in md:
        allMonsters.append([key, md[key][0]])
    # Find total of all likelihoods.
    total = 0
    for m in allMonsters:
        total = total + m[1]
    # Randomly, generate a number within the total
    selection = random.randint(0, total-1)
    # find the key based on random number
    highpoint = 0
    for m in allMonsters:
        highpoint = highpoint + m[1]
        if selection < highpoint:
            return m[0]

#Rules to the game 
def rulesgame():
    print()
    print("These are the rules to the game:")
    print("You will have to fight the monster until you or the monster dies")
    print("If you have no more health left then you die.\nOr if the monster does not have any more health left.")
    print("You will not be able to buy more attributes in the game if you do not have any gold left.")
    print("You have to enter an valid user input for every encounter that will occur.")
    print("You will be able to collect gold if player defeat the monster.")
    print("If the monster defeats player , player will lose gold.")
    print("You will only be allowed to use gold in the store to upgrade stats.")
    print()

#Calls the main function 
main()
