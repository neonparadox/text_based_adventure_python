import time
import random
#inspired by adarkroom
print("Welcome to the text based adventure\nType \"help\" to get started!\n")
inventory = {
    "crate": 1,
    "match": 5,
    "dictionary": 1,
}
goto = ["door","candle","trapdoor","stairs","chest"]
rooms = ["dark room","basement","yard","living room"]

connect_entry={
    0: "dark room",
    1: "dark room",
    2: "dark room",
    3: "basement",
    4: "basement",
}

connect_exit={
    0:"yard",
    2:"basement",
    3:"living room",
}

used_interactions = {
    1:False,
    4:False,
}

is_dictionary={
    "game": "good"
}
game_over = False
current_loc = "dark room"
def inventorycheck():
    for i in list(inventory.keys()):
        if inventory[i] == 0:
            inventory.pop(i)
                
while game_over == False:
    inventorycheck()
    prompt = input("> ").split(" ")
   
    print("")
    if prompt[0] == "help":
        if len(prompt) == 1:
            print("HELP PAGE:")
            print("**********")
            print("help: displays this help message")
            print("help <command name>: displays extra info about a command")
            print("info <item name>: displays info about an item")
            print("inventory: displays your inventory [alias inv]")
            print("where: displays current location")
            print("use <item>: uses the item specified if it is in your inventory")
            print("look: look around your current room")
            print("go <place>: go to a certain place. You can find such places with the \"look\" command.")
            print("**********")
        elif len(prompt) > 2:
            print("Invalid syntax! You may check the syntax using \"help\"")
           
           
        else:
            pass
    elif prompt[0] == "where":
        print("**********")
        print("Currently in: " + current_loc)
        print("**********")
    elif prompt[0] == "inventory" or prompt[0] == "inv":
        print("You open your goatskin bag containing all your precious belongings.")
   
        item_list = inventory.keys()
        for i in item_list:
            number_of_item = inventory[i]
            print(i + " (" + str(number_of_item) + " available)")
    elif len(prompt) == 3:
        if prompt[1] == "is" and len(prompt) == 3:
            print("Added to dictionary: " + prompt[0] + " and " + prompt[2])
            is_dictionary[prompt[0]] = prompt[2]
    elif prompt[0] == "use":
   
        if prompt[1] in inventory.keys():
            if prompt[1] == "dictionary":
                print("You open your dictionary.")
                for key in is_dictionary.keys():
                    print(key + " is " + is_dictionary[key])
            elif prompt[1] == "crate":
                print("You open your crate.")
                
                 
                match_add = random.randint(5,10)
                print("You find " + str(match_add) + " matches.")
                if "match" in inventory.keys():
                    inventory["match"] += match_add
                else:
                    inventory["match"] = match_add
                inventory["crate"] -= 1
            else:
                pass
        else:
            print("You don't own this item")
                
    elif prompt[0] == "look":
        possible_interaction = []
        for i in connect_entry.keys():
            if connect_entry[i] == current_loc:
                possible_interaction.append(goto[i])
        for i in connect_exit.keys():
            if connect_exit[i] == current_loc:
                possible_interaction.append(goto[i])
        message = "**********\nYou can go to:"
        
        for i in possible_interaction: 
            message += "\n"
            message += i
    

        print("You look around the " + current_loc + ".\n"+message+"\n**********")


        
    elif prompt[0] == "go":
        
        interact = prompt[1]
        if interact not in goto:
            print("That doesnt exist :^)")
        else:
            interaction = goto.index(interact)
            if interaction in connect_entry:
                if interaction in connect_exit:
                    if current_loc == connect_entry[interaction]:
                        print("You use the " + interact + " and you enter the " + connect_exit[interaction])
                        #too lazy to make this more sophisticated
                        current_loc = connect_exit[interaction]
                    elif current_loc == connect_exit[interaction]:
                        print("You use the " + interact + " and you enter the " + connect_entry[interaction])
                        current_loc = connect_entry[interaction]
                    else:
                        print("You're not in the right room to go here!")
                else:
                    if used_interactions[interaction] == False:
                        used_interactions[interaction] = True
                    else:
                        print("You've already gone here, there's nothing left!")
                        continue
                    print("You go to the " + interact)
                    
                    if interact == "candle":
                        if "key" in inventory.keys():
                            inventory["key"] += 1
                            
                        else:
                            inventory["key"] = 1
                        print("You looked under the candle and you found a key :O")
                    elif interact == "chest":
                        open_or_no = input("Do you want to open the chest? y/n\n")
                        if open_or_no == "y":
                            if "key" in inventory.keys():
                                if inventory["key"] > 0:
                                    inventory["key"] -= 1
                                    print("Yay! You opened the chest with a key :D")
                                    if "axe" not in inventory.keys():
                                        inventory["axe"] = 1
                                    else:
                                        inventory["axe"] += 1
                                    print("\nYou found an axe! You can now use it to break stuff :O")

                                else:
                                    print("You need a key to open this chest :(")
                            else:
                                print("You need a key to open this chest :(")
                        else:
                            print("Aw :(")
                    else:
                        pass
                    #should be a conditional statement for each possible interaction...
            else:
                print("Does not exist!")
