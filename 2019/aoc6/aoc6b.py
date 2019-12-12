class orbitingObject:
    
    def __init__(self, name):
        self.orbits = None
        self.satellites = []
        self.name = name
        
    def addSatellite(self, satellite):
        self.satellites.append(satellite)
        satellite.orbits = self

    def getOrbitCount(self):
        if self.orbits is None:
            if self.name != "COM":
                print(f"Object {self.name} does not orbit anything")
            return 0
        else:
            return self.orbits.getOrbitCount() + 1

    def getOrbitPath(self):
        path = []
        if self.orbits is not None:
            self.orbits.searchOrbitPath(path)
        return path

    def searchOrbitPath(self, path):
        path.append(self)
        if self.orbits is not None:
            self.orbits.searchOrbitPath(path)
        return path


def main():
    orbitObjects = {}
    
    with open("2019/aoc6/input.txt") as input_file:
        lines = input_file.readlines()

    for line in lines:
        orbitDef = line.split(")")            # Get the object pair
        c = orbitDef[0].strip()
        s = orbitDef[1].strip()

        if c in orbitObjects:
            # Already exists
            centerObject = orbitObjects[c]
        else:
            # Create and Use
            centerObject = orbitingObject(c)
            orbitObjects[c] = centerObject

        if s in orbitObjects:
            # Already Exists
            satellite = orbitObjects[s]
        else:
            # Create and Use
            satellite = orbitingObject(s)
            orbitObjects[s] = satellite

        if satellite.orbits is None:
            # Set up the orbit
            satellite.orbits = centerObject
            centerObject.addSatellite(satellite)
        else:
            print(f"Warning - satellite {satellite.name} already orbits {satellite.orbits.name}, cannot change to {centerObject.name}")
            

    print(f"Found {len(orbitObjects)} Orbital Objects")

    orbitCount = 0
    for orbitObject in orbitObjects.values():
        orbitCount += orbitObject.getOrbitCount()

    print(f"Orbit Count Checksum: {orbitCount}")

    YOU = orbitObjects["YOU"]
    pathYOU = YOU.getOrbitPath()
    print(f"YOU are {len(pathYOU)} objects from COM")

    SAN = orbitObjects["SAN"]
    pathSAN = SAN.getOrbitPath()
    print(f"SAN is {len(pathYOU)} objects from COM")
    
    transfers = -100    # Obvious error value

    for orbitObject in pathYOU:
        if orbitObject in pathSAN:
            # Found a common object
            transfers = pathYOU.index(orbitObject) + pathSAN.index(orbitObject)
            break

    print(f"You need {transfers} orbital transfers to get to Santa.")


# Execute the program
if __name__ == "__main__":
    main()