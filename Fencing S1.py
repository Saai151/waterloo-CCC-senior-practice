num = int(input())
heights = input()
heights = heights.split(" ")
widths = input()
widths = widths.split(" ")

area_finder = []
area = 0

for i in range(len(heights)-1):
    temp = int(heights[i]) + int(heights[i+1])
    area_finder.append(temp)
    area += (int(widths[i])*area_finder[i])/2
    

print(area)