class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceManhattan(self, otherPoint):
        return abs(self.x - otherPoint.x) + abs(self.y - otherPoint.y)

class WireSegment:
    

    
    
    def __init__(self, startPoint, vector):

        self.direction = vector[0]
        self.distance = int(vector[1:])

        if self.direction == "U":
            self.vertical = True
            self.xMin = startPoint.x
            self.xMax = startPoint.x
            self.yMin = startPoint.y
            self.yMax = startPoint.y + self.distance
            self.endPoint = point(startPoint.x, startPoint.y + self.distance)
        elif self.direction == "D":
            self.vertical = True
            self.xMin = startPoint.x
            self.xMax = startPoint.x
            self.yMin = startPoint.y - self.distance
            self.yMax = startPoint.y
            self.endPoint = point(startPoint.x, startPoint.y - self.distance)
        elif self.direction == "L":
            self.vertical = False
            self.xMin = startPoint.x - self.distance
            self.xMax = startPoint.x
            self.yMin = startPoint.y
            self.yMax = startPoint.y
            self.endPoint = point(startPoint.x - self.distance, startPoint.y)
        elif self.direction == "R":
            self.vertical = False
            self.xMin = startPoint.x
            self.xMax = startPoint.x + self.distance
            self.yMin = startPoint.y
            self.yMax = startPoint.y
            self.endPoint = point(startPoint.x + self.distance, startPoint.y)
        else:
            print(f"Error: Vector {vector}")

        # print (f"Segment: {self.direction} {self.distance} to {self.endPoint.x}, {self.endPoint.y}")

    def intersection(self, otherWire):
        if self.vertical == otherWire.vertical:
            # Same orientation, ignore
            return None

        elif self.vertical:
            #This wire is vertical, compare againt horizontal wire
            if (otherWire.xMin <= self.xMin <= otherWire.xMax) and (self.yMin <= otherWire.yMin <= self.yMax):
                # Intersects!
                return point(self.xMin, otherWire.yMin)
            else:
                # No intersection
                return None

        else:
            #this wire is horizontal, compare against vertical wire
            if (self.xMin <= otherWire.xMin <= self.xMax) and (otherWire.yMin <= self.yMin <= otherWire.yMax):
                # Intersects!
                return point(otherWire.xMin, self.yMin)
            else:
                # No intersection
                return None

        


def main():
    centralPort = point(0,0)

    input_file = open("2019/aoc3/input.txt")

    # Build Wire 1
    wire1 = []
    vectorList1 = input_file.readline().split(",")
    startPoint = centralPort
    for vector in vectorList1:
        segment = WireSegment(startPoint, vector)
        wire1.append(segment)
        startPoint = segment.endPoint

    # Build Wire 2
    wire2 = []
    vectorList2 = input_file.readline().split(",")
    
    startPoint = centralPort
    for vector in vectorList2:
        segment = WireSegment(startPoint, vector)
        wire2.append(segment)
        startPoint = segment.endPoint
    
    #Find intersections
    intersections = []
    for wire1Segment in wire1:
        for wire2Segment in wire2:
            intersection = wire1Segment.intersection(wire2Segment)

            if not (intersection is None):
                intersections.append(intersection)

    print(f"Found {len(intersections)} intersections")

    # Sort intersections
    intersections.sort( key=lambda p: p.distanceManhattan(centralPort))

    #print intersection list
    # for intersection in intersections:
        # print(f"x={intersection.x}, y={intersection.y}")

    print(f"Manhattan Distance = {intersections[0].distanceManhattan(centralPort)}")

# Execute the program
if __name__ == "__main__":
    main()