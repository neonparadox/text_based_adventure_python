import time
import random
#inspired by adarkroom
print("Welcome to the text based adventure\nType \"help\" to get started!\n")
inventory = {
    "crate": 1,
    "match": 5,
    "wood": 10,
    "dictionary": 1
}
goto = ["door","candle"]
rooms = ["dark room","basement","yard"]
connect_entry={
    0: "dark room",
    1: "dark room"
}
connect_exit={
    0:"yard"
}
#this part is sad
is_dictionary={
    "game": "good"
}
game_over = False
current_loc = "dark room"
while game_over == False:
    prompt = input("").split(" ")
   
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
                number=random.randint(1,len(is_dictionary)+1)
                if number != len(is_dictionary)+1:
                    
                    match_add = random.randint(5,10)
                    print("You find a key as well as " + str(match_add) + " matches.")
                    if "match" in inventory.keys():
                        inventory["match"] += match_add
                    else:
                        inventory["match"] = match_add
                    if "key" in inventory.keys():
                        inventory["key"] += 1
                    else:
                        inventory["key"] = 1
                   
                else:
                  
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
        for i in list(inventory.keys()):
            if inventory[i] == 0:
                inventory.pop(i)
                
                
    elif prompt[0] == "look":
        possible_interaction = []
        for i in connect_entry.keys():
            if connect_entry[i] == current_loc:
                possible_interaction.append(goto[i])
        for i in connect_exit.keys():
            if connect_exit[i] == current_loc:
                possible_interaction.append(goto[i])
        message = "You see:"
        if len(possible_interaction) == 0:
            message = ""
        elif len(possible_interaction) < 2:
            for i in possible_interaction:
                message += "\n" 
                message += i
        else:
            num = len(possible_interaction)
            for i in range(num-1):
                pass

        print("You look around the " + current_loc + ". You se")


        
    elif prompt[0] == "go":
        interact = prompt[1]
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
                pass
                #should be a conditional statement for each possible interaction...
        else:
            print("Does not exist!")
