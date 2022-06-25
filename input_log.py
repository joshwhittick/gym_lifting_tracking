lifts = []

lift_values = {
"a" : "", #lift
"b" : "", #date
"c" : 0, #load
"d" : 0, #sets
"e" : 0, #reps
"f" : 0, #sets * reps
"g" : 0 #set * reps * load
}

def write_to_log(lift, date, lift_load, lift_sets, lift_reps, total_reps, total_load):
    
    line = f"{lift} on {date} with {lift_load} kgs sets: {lift_sets} reps: {lift_reps} total reps: {total_reps} total load: {total_load:g}"
    
    with open('lifting_log.txt', 'a') as f:
        f.write('\n')
        f.writelines(''.join(line))
        
while True: 
    print("Do you want to enter a new days lifting?")
    n = input("y/n:")

    if n == "y":
        lift_values["b"] = input("Enter date: ")    
        lifts.append(input("Enter exercise: "))

        while input("Do you want to enter a new exercise? (y/n):") == "y":
            inpt = input("Enter another exercise:")
            lifts.append(inpt) 

        for lift in lifts:
            lift_values["a"] = lift
            lift_values["c"] = float(input(f"Enter load for {lift_values['a']}:"))
            lift_values["d"] = int(input(f"Enter sets for {lift_values['a']}:"))
            lift_values["e"] = int(input(f"Enter reps for {lift_values['a']}:"))
            lift_values['f'] = int(lift_values['d'] * lift_values['e'])
            lift_values['g'] = int(lift_values['f'] * lift_values['c'])

            write_to_log(lift_values["a"], lift_values["b"], lift_values["c"], lift_values["d"], lift_values["e"], lift_values["f"], lift_values["g"])

    elif n == "n":
        quit()
