David = 100
Antonia = 100

num_rounds = int(input("Please enter the number of rounds to be played: \n"))

for i in range(num_rounds):
    temp = input("What did you role: ")
    temp2 = temp.split( )
    David_role = int(temp2[0])
    Antonia_role = int(temp2[1])
    if (David_role>Antonia_role):
        Antonia = Antonia - David_role
    elif (Antonia_role > David_role):
        David = David - Antonia_role

print(David)
print(Antonia)
