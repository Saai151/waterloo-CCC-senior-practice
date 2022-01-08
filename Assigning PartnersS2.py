num = int(input())

names1 = input()
names2 = input()

list_names = [names1.split(" "),names2.split(" ")]
counter = 0
for i in range(num):

    index = list_names[1].index(list_names[0][i])
    index2 = list_names[0].index(list_names[1][i])
    if(index == index2 and list_names[0][i] != list_names[1][i]):
        counter +=1 
    else:
        counter-=1

if(counter == num): print("good")
else: print("bad")
