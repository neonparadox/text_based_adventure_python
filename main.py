import time
import random

print("Welcome to TIG text based adventure\nType \"help\" to get started!\n")
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
game_over = False;
current_loc = "dark room"
while game_over == False:
    prompt = input("Enter command: ").split(" ")
   
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
        if current_loc == "dark room":
            print("You see a dimly lit candle and an old wooden door. [Possible interactions: door, candle]")
        else:
            pass 