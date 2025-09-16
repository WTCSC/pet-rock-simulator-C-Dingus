import os

def read_save():
    stats = {}
    with open("save.rock", "r") as file:
        lines = file.read().split('\n');
        for line in lines:
            match line.split(':')[0]:
                case "name":
                    stats["name"] = line.split(':')[1]
                case "food":
                    stats["food"] = int(line.split(':')[1])
                case "happiness":
                    stats["happy"] = int(line.split(':')[1])
                case "diet":
                    buf = line.split('[')[1].split(']')[0].split(',')
                    stats["diet"] = [int(buf[0]), int(buf[1]), int(buf[2])]
                case "mind":
                    buf = line.split('[')[1].split(']')[0].split(',')
                    stats["mind"] = [int(buf[0]), int(buf[1])]
    return stats


def run():
    save = read_save()
    while True:
        start_msg = f"{save['name']} is\n"
        if save['food'] <= 3:
            start_msg += "Hungry\n"
        if save['happy'] <= 3:
            start_msg += "Bored\n"
        if 'mind' in save:
            calm = save['mind'][0]
            joy = save['mind'][1]
            
            if calm > 0:
                if joy > 5 and calm > 5:
                    start_msg += "Euphoric\n"
                elif joy > 0:
                    start_msg += "Happy\n"
                elif joy > -5:
                    start_msg += "Sad\n"
                else:
                    start_msg += "Depressed\n"
            else:
                if joy < -5 and calm < -5:
                    start_msg += "Psychopathic\n"
                elif joy < 0:
                    start_msg += "Apathetic\n"
                else:
                    if calm < -5:
                        start_msg += "Furious\n"
                    else:
                        start_msg += "Angry\n"
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
            elif ballance > 5:
                start_msg += "Queasy\n"
            else:
                start_msg += "Healthy\n"

        input(start_msg)
        




def start(challanges, name):
    with open("save.rock", "w") as file:
        contents = f"name:{name}\nfood:5\nhappiness:5\n"
        if "diet" in challanges:
            contents += "diet:[5, 5, 5]\n"
        if "mind" in challanges:
            contents += "mind:[5, 5]\n"
        file.write(contents)

    run();




if os.path.exists("save.rock"):
    while True:
        i = input("start/(cont)inue/quit\n>>")
        if i == "start":
            challanges = []
            i = input("add challanges?(y/n)\n>>")
            if i == "y":
                while True:
                    challange = input("challange name or (exit)\n>>")
                    if challange == "exit":
                        break
                    challanges.append(challange)
            name = input("Name of your new pet rock:\n>>")
            start(challanges, name)
            break
        elif i == "cont":
            run()
            break
        elif i == "quit":
            break
        else:
            print("invalid input")
else:
    i = input("start/quit\n>>")
    while True:
        if i == "start":
            challanges = []
            i = input("add challanges?(y/n)\n>>")
            if i == "y":
                while True:
                    challange = input("challange name or (exit)\n>>")
                    if challange == "exit":
                        break
                challanges.append(challange)
            name = input("Name of your new pet rock:\n>>")
            start(challanges, name)
        elif i == "quit":
            break
        else:
            print("invalid input")

