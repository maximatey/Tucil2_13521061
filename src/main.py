import random
import math
import time

def distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 + (point1[2]-point2[2])**2)

def exhaustive(points):
    n = len(points)
    count = 0
    if n <= 1:
        return None
    elif n == 2:
        return [points,count]
    else:
        mind = distance(points[0], points[1])
        count+=1
        closest = [points[0], points[1]]
        for i in range(n):
            for j in range(i+1, n):
                dist = distance(points[i],points[j])
                count +=1
                if dist < mind:
                    mind = dist
                    closest = [points[i],points[j]]
        return [closest,count]

def main_alg(points):
    n = len(points)
    count = 0
    if n <= 3:
        return exhaustive(points)
    else:
        mid = n//2
        sortedps=sorted(points, key=lambda p: p[0])
        left_points=sortedps[:mid]
        right_points=sortedps[mid:]
        [left, c1]=main_alg(left_points)
        count+=c1
        [right,c2]=main_alg(right_points)
        count+=c2
        if distance(left[0],left[1])<distance(right[0],right[1]):
            closest=left
            mind=distance(left[0], left[1])
        else:
            closest=right
            mind=distance(right[0], right[1])
        count +=2
        mid_points=[]
        for point in sortedps:
            if abs(point[0]-sortedps[mid][0])<mind:
                mid_points.append(point)
        for i in range(len(mid_points)):
            j=i+1
            while j<len(mid_points) and mid_points[j][1]-mid_points[i][1]<mind:
                dist=distance(mid_points[i],mid_points[j])
                count+=1
                if dist<mind:
                    mind=dist
                    closest=[mid_points[i],mid_points[j]]
                j+=1
        return [closest,count]
    


n = int(input("Input n: "))

print(n, "points")
print("")

points = [(random.randrange(0,150), random.randrange(0,150), random.randrange(0,150)) for i in range(n)]
print("Random points:", points)

start_time = time.time()
[closestbf,count] = exhaustive(points)
ttime= time.time()-start_time

print("")
print("Brute Force")
print("The closest pair:", closestbf, "with distance", "{:.2f}".format(distance(closestbf[0], closestbf[1])))
print("Number of Euclidian Distance Formula called:", count)
print("Total time of execution:", "{:.5f}".format(ttime * 1000), " ms")

start_time = time.time()
[closestdnc,count] = main_alg(points)
ttime= time.time()-start_time

print("")
print("Divide and conquer")
print("The closest pair:", closestdnc, "with distance", "{:.2f}".format(distance(closestdnc[0], closestdnc[1])))
print("Number of Euclidian Distance Formula called:", count)
print("Total time of execution:", "{:.5f}".format(ttime * 1000), " ms")
