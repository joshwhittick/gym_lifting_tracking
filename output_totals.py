lifts = []
l = []

with open("lifting_log.txt") as f:
    for line in f:
        parts = line.split()
        exercise = parts[0]
        l.append(exercise)
        
        for i in l:
            if exercise not in lifts:
                lifts.append(exercise)
                
class Lift:
    def __init__(self, name, total_lifted):
        self.name = name
        self.total_lifted = total_lifted           
    
    def output_total(self):
        return f"Total lifted for {self.name} is {self.total_lifted:g}"

total = []

i = 0
n = 0
while i < len(lifts):
    with open("lifting_log.txt") as f:
        for line in f:
            parts = line.split()
            exercise = parts[0]
            if exercise == lifts[n]:
                load = float(parts[15])
                total.append(load)
    lifts[n] = Lift(lifts[n], sum(total))
    print(lifts[n].output_total())
    total.clear()
    n += 1
    i += 1
