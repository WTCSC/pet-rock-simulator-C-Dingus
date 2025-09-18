#used to check file system
import os

#quit the program
import sys

#i stole this idea from dexter
import time

def spell(string):
    for i in string:
        print(i, end = "", flush = True)
        time.sleep(0.02)

def rock(emotion):
    with open("face.rock") as file:
        print(file.read().lstrip().split("%" + emotion + "%")[1])
    return None


#read the save
def read_save():
    #set base dict to be filled
    stats = {}

    #open save
    with open("save.rock", "r") as file:
        #split it into lines
        lines = file.read().split('\n');

        for line in lines:
            #crunch the lines into the dict
            match line.split(':')[0]:
                case "name":
                    stats["name"] = line.split(':')[1]
                case "food":
                    stats["food"] = int(line.split(':')[1])
                case "happy":
                    stats["happy"] = int(line.split(':')[1])
                case "diet":
                    buf = line.split('[')[1].split(']')[0].split(',')
                    stats["diet"] = [int(buf[0]), int(buf[1]), int(buf[2])]
                case "mind":
                    buf = line.split('[')[1].split(']')[0].split(',')
                    stats["mind"] = [int(buf[0]), int(buf[1])]
                case "egg":
                    stats["egg"] = "egg"

    #return the dict
    return stats

#push the rock stats dict into a file that read_save can read
def save_game(data):
    save = ""

    for key, val in data.items():
        #formating
        save += str(key)
        save += ":"
        save += str(val)
        save += "\n"

    #write the file
    with open("save.rock", "w") as file:
        file.write(save)

#run the game
def run():
    #read the save data
    save = read_save()

    #start of the game loop
    while True:
        #calculate health every round if it goes bellow 1 then the game is over
        health = 5

        #set the start message that tells the user how their pet rock is
        start_msg = f"{save['name']} is\n"

        #crunch all the data for the start message
        if save['food'] <= 3:
            start_msg += "Hungry\n"

            if 'mind' in save:
                save['mind'][1] -= 3
                save['mind'][0] -= 4

        if save['food'] <= 0:
            health = 0

        if save['happy'] <= 3:
            start_msg += "Bored\n"
            if 'mind' in save:
                save['mind'][1] -= 4

        if save['happy'] <= 0:
            if 'mind' in save:
                save['mind'][1] -= 10
            else:
                health = 0

        if 'mind' in save:
            calm = save['mind'][0]
            joy = save['mind'][1]
            
            if calm > 0:
                if joy > 5 and calm > 5:
                    rock("euphoric")
                elif joy > 0:
                    rock("happy")
                elif joy > -5:
                    rock("sad")
                else:
                    rock("depressed")
            else:
                if joy < -5 and calm < -5:
                    rock("psychopathic")
                elif joy < 0:
                    rock("apathetic")
                else:
                    if calm < -5:
                        rock("furious")
                    else:
                        rock("angry")

        if 'diet' in save:
            mean = int((save['diet'][0] + save['diet'][1] + save['diet'][2])/3)
            ballance = 0;

            for i in save['diet']:
                if i > mean:
                    ballance += (i - mean)
                else:
                    ballance += (mean - i)

            if ballance > 5:
                start_msg += "Sick\n"
                if 'mind' in save:
                    save['mind'][1] -= 10
            elif ballance > 2:
                start_msg += "Queasy\n"
                if 'mind' in save:
                    save['mind'][1] -= 5
            else:
                start_msg += "Healthy\n"

        #end the game
        if health <= 0:
            spell("Dead")
            break

        #tell the player the information they can get about their rock
        spell(start_msg)

        #get what the player wants to do
        while True:
            spell(f"\nWhat do you do?\n-(Feed) {save['name']}\n-(Play) with {save['name']}\n-Save and (Quit)\n>>")
            choice = input()

            if choice.lower() == "play":
                spell(f"How would you like to play with {save['name']}\n-(Throw) him at pedestrians\n-(Pet) him\n-Bring him on a (run) \n>>")
                choice = input()

                match choice.lower():
                    case "throw":
                        spell(f"you throw {save['name']} at a few pedestrians")
                        save['happy'] += 4
                        if 'mind' in save:
                            save['mind'][0] -= 3
                            save['mind'][1] -= 3
                    case "pet":
                        spell(f"you pet {save['name']} ")
                        save['happy'] += 2
                        if 'mind' in save:
                            save['mind'][0] += 2
                            save['mind'][1] += 1

                    case "run":
                        spell(f"you take {save['name']} on a run for some reason")
                        save['happy'] += 1
                        if 'mind' in save:
                            save['mind'][0] += 4
                            save['mind'][1] -= 1

                    case "chuck":
                        spell(f"You found a seceret :D, anyways you chuck {save['name']} at oncoming traffic")
                        save['happy'] += 24
                        if 'mind' in save:
                            save['mind'][0] -= 20
                            save['mind'][1] -= 20
                
            elif choice.lower() == "feed":
                
                #if the player has the diet challange enables
                if 'diet' in save:
                    spell(f"\n what do you wish to feed {save['name']} \n-S(s), \n-.*.(dots), \n-//(bars) \n>>")
                    food = input()
                    match food.lower():
                        case "s":
                            spell(f"you feed {save['name']} some protein rich food (S)")
                            save['diet'][0] += 1
                            save['food'] += 1

                            #if the rock has emotions
                            if 'mind' in save:
                                save['mind'][0] + 2
                        case "dots":
                            spell(f"you feed {save['name']} some carbohydrate rich food (.*.)")
                            save['diet'][1] += 1
                            save['food'] += 2

                            if 'mind' in save:
                                save['mind'][0] -= 2
                                save['mind'][1] += 3
                        case "bars":
                            spell(f"you feed {save['name']} some fatty food (//)")
                            save['diet'][2] += 1
                            save['food'] += 3

                            if 'mind' in save:
                                save['mind'][0] -= 1
                                save['mind'][1] -= 2
                        case _:
                            spell(f"you did not feed {save['name']}")
                            if 'mind' in save:
                                save['mind'][0] -= 2
                                save['mind'][1] -= 3
                else:
                    spell(f"you feed {save['name']}")
                    save['food'] += 2

                break

            elif choice.lower() == "quit":
                #save and quit the game
                with open("test.rock", "w") as file:
                    save_game(save)
                    sys.exit(0)
            else:
                spell("unrecognized input")

        #end of round
        save['happy'] -= 2
        save['food'] -= 2

        if 'diet' in save:
            save['diet'] -= [2, 2, 2]

        if 'mind' in save:
            save['mind'] += [1, 1]

        if 'egg' in save:
            save['egg'] += "egg"


#used to initiate a new save 
def start(challanges, name):
    #make save file
    with open("save.rock", "w") as file:
        contents = f"name:{name}\nfood:5\nhappy:5\n"
        #read the input challanges
        if "diet" in challanges:
            contents += "diet:[5, 5, 5]\n"
        if "mind" in challanges:
            contents += "mind:[5, 5]\n"
        if "egg" in challanges:
            spell("you found an egg")
            contents += "egg:egg\n"
        file.write(contents)
    #start the game loop
    run();



#if a save exists
if os.path.exists("save.rock"):
    #get user input to start new or continue or quit
    while True:
        spell("(Start)/(Cont)inue/Quit\n")
        i = input(">>")
        if i == "start":
            #ask if the player would like to play some of the challanges
            challanges = []
            spell("add challenges?(y/n)\n>>")
            i = input()
            if i == "y":
                while True:
                    #read challanges
                    spell("challenge name or (exit)\n>>")
                    challange = input()
                    if challange == "exit":
                        break
                    challanges.append(challange)
            name = spell("Name of your new pet rock:\n>>")
            name = input()
            #start
            start(challanges, name)
            break
        elif i == "cont":
            #continue from save
            run()
            break
        elif i == "quit":
            #leave
            break
        else:
            spell("invalid input")
else:
    spell("start/quit\n>>")
    i = input()
    while True:
        #start
        if i == "start":
            challanges = []
            #impliment challanges
            spell("add challenges?(y/n)\n>>")
            i = input()
            if i == "y":
                while True:
                    spell("challenge name or (exit)\n>>")
                    challange = input()
                    if challange == "exit":
                        break
                challanges.append(challange)
            spell("Name of your new pet rock:\n>>")
            name = input()
            start(challanges, name)
        elif i == "quit":
            #leave
            break
        else:
            spell("invalid input")

