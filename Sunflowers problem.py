num = int(input())
plants = ""

for i in range(num):
    plant = input()
    plants += plant + " "
plants = plants.split(" ")
plants.sort()
plants.remove("")
length = int(len(plants)/num)

correct_plants = []


for i in range(0,len(plants),length):
    temp = []
    for j in range(length):
        temp.append(plants[j+i])
        correct_plants.append(temp)


for i in range(0,len(correct_plants),length):
    print(" ".join(correct_plants[i]))






    