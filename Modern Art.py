M = int(input())
N = int(input())
K = int(input())

canvas = []

for j in range(M):
    canvas.append(["B"]*N)


counter = 0
for j in range(K):
    painted = input()
    painted = painted.split(" ")
    num = int(painted[1])-1
    if (painted[0] == "R"):
        for i in range(N):
            if (canvas[num][i] == "G"):
                canvas[num][i] = "B"
                counter-=1
            elif (canvas[num][i] == "B"):
                canvas[num][i] = "G"
                counter+=1
    elif(painted[0]=="C"):
        for a in range(M):
            if(canvas[a][num] == "G"):
                canvas[a][num] = "B"
                counter-=1
            elif(canvas[a][num] == "B"):
                canvas[a][num] = "G"
                counter+=1
print(counter)




