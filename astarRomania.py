#
#   Created by PyCharm.
#   User: Rizky Andre Wibisono
#   Date: 17/03/2019
#   Time: 20:59
#

import heapq

class ctNode:
    def __init__(self, city, distance):
        self.city = str(city)
        self.distance = str(distance)

class priorityQueue:
    def __init__(self):
        self.cities=[]

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))

    def pop(self):
        return  heapq.heappop(self.cities)[1]

    def isEmpty(self):
        if(self.cities == []):
            return True
        else:
            return False

romania = {}

def makedict():
    file = open("romania.txt", 'r')
    for string in file:
        line = string.split(',')
        ct1 = line[0]
        ct2 = line[1]
        dist = int(line[2])
        romania.setdefault(ct1, []).append(ctNode(ct2, dist))
        romania.setdefault(ct2, []).append(ctNode(ct1, dist))

def makehuristikdict():
    h = {}
    with open("romania_sld.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h

def heuristic(node, values):
    return values[node]

def astar(start, end, visited, path, distance):
    q = priorityQueue()
    q.push(start, 0)
    distance[start] = 0
    expandedList = []
    path[start]= None
    h = makehuristikdict()

    while(q.isEmpty() == False):
        current = q.pop()
        expandedList.append(current)

        if(current == end):
            break

        for new in romania[current]:
            updatedDistance = distance[current] + int(new.distance)

            if(new.city not in distance or updatedDistance < distance[new.city]):
                distance[new.city] = updatedDistance
                priority = updatedDistance + heuristic(new.city, h)
                q.push(new.city, priority)
                path[new.city] = current

    printoutput(start, end, path, distance, expandedList)


def printoutput(start, end, path, distance, expandedlist):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()
    print("Kota yg mungkin dijelajah: " + str(expandedlist))
    print("Jumlah kemungkinan kota: " + str(len(expandedlist)))
    print("Daftar final kota yang dilewati: " + str(finalpath))
    print("Jumlah kota: " + str(len(finalpath)))
    print("Total jarak: " + str(distance[end]))


def main():
    src = "Arad"
    dst = "Bucharest"

    makedict()
    visited = []
    path = {}
    distance = {}
    astar(src, dst, visited, path, distance)


if __name__ == "__main__":
    main()


