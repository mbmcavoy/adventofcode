class point:

    refDistance = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceManhattan(self, otherPoint):
        return abs(self.x - otherPoint.x) + abs(self.y - otherPoint.y)

class WireSegment:
    

    
    
    def __init__(self, startPoint, startDistance, vector):

        self.startPoint = startPoint
        self.startDistance = startDistance

        self.direction = vector[0]
        self.distance = int(vector[1:])
        
        self.endDistance = self.startDistance + self.distance

        self.xMin = startPoint.x
        self.xMax = startPoint.x
        self.yMin = startPoint.y
        self.yMax = startPoint.y

        if self.direction == "U":
            self.vertical = True
            self.yMax = startPoint.y + self.distance
            self.endPoint = point(startPoint.x, self.yMax)
        elif self.direction == "D":
            self.vertical = True
            self.yMin = startPoint.y - self.distance
            self.endPoint = point(startPoint.x, self.yMin)
        elif self.direction == "L":
            self.vertical = False
            self.xMin = startPoint.x - self.distance
            self.endPoint = point(self.xMin, startPoint.y)
        elif self.direction == "R":
            self.vertical = False
            self.xMax = startPoint.x + self.distance
            self.endPoint = point(self.xMax, startPoint.y)
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
                intersection = point(self.xMin, otherWire.yMin)
                intersection.refDistance = self.startDistance + intersection.distanceManhattan(self.startPoint) + \
                    otherWire.startDistance + intersection.distanceManhattan(otherWire.startPoint)
                return intersection
            else:
                # No intersection
                return None

        else:
            #this wire is horizontal, compare against vertical wire
            if (self.xMin <= otherWire.xMin <= self.xMax) and (otherWire.yMin <= self.yMin <= otherWire.yMax):
                # Intersects!
                intersection = point(otherWire.xMin, self.yMin)
                intersection.refDistance = self.startDistance + intersection.distanceManhattan(self.startPoint) + \
                    otherWire.startDistance + intersection.distanceManhattan(otherWire.startPoint)
                return intersection

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
    distance = 0

    for vector in vectorList1:
        segment = WireSegment(startPoint, distance, vector)
        wire1.append(segment)
        startPoint = segment.endPoint
        distance = segment.endDistance

    # Build Wire 2
    wire2 = []
    vectorList2 = input_file.readline().split(",")
    startPoint = centralPort
    distance = 0

    for vector in vectorList2:
        segment = WireSegment(startPoint, distance, vector)
        wire2.append(segment)
        startPoint = segment.endPoint
        distance = segment.endDistance

    #Find intersections
    intersections = []
    for wire1Segment in wire1:
        for wire2Segment in wire2:
            intersection = wire1Segment.intersection(wire2Segment)

            if not (intersection is None):
                intersections.append(intersection)

    print(f"Found {len(intersections)} intersections")

    # Sort intersections
    intersections.sort( key=lambda p: p.refDistance)

    print(f"Reference Distance = {intersections[0].refDistance}")

# Execute the program
if __name__ == "__main__":
    main()