lift = input("Enter exercise to see:")
with open("lifting_log.txt") as f:
    for line in f:
        parts = line.split()
        exercise = parts[0]
        if exercise == lift:
            print(line)