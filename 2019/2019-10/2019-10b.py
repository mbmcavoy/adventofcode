from operator import attrgetter
from math import pi
from math import atan2

def main():
    with open("2019/2019-10/input.txt") as input_file:
        lines = [line.rstrip('\n') for line in input_file]

    field = asteroidField(lines)
    sites = []

    for y in range(field.lenY):
        for x in range(field.lenY):
            if field.hasAsteroid(x, y):
                # Found an asteroid - possible station site
                newSite = site(x, y)
                newSite.checkView(field)
                sites.append(newSite)

    print(f"Surveyed {len(sites)} asteroids for possible Monitoring Base sites.")
    
    base = max(sites, key=attrgetter('visibleCount'))
    sites = None # done - go away!
    print(f"The best site is at {base.x}, {base.y} and can see {base.visibleCount} asteroids. Installing...")
    field.changeLocation(base.x, base.y, "X")
    field.printField()

    print(f"Proceeding to obliterate asteroids!")
    destroyedAsteroids = base.destroyAsteroids(field)

    print(f"Destroyed {len(destroyedAsteroids)} asteroids.")
    field.printField()

    if len(destroyedAsteroids) >= 200:
        winner = destroyedAsteroids[199]
        print(f"The 200th asteroid destoyed was at location {winner[0]}, {winner[1]}.")


class asteroidField:
    def __init__(self, fieldDef):
        self.field = fieldDef
        self.lenY = len(fieldDef)
        self.lenX = len(fieldDef[0])

    def hasAsteroid(self, x, y):
        if (self.field[y][x] == "#"):
            return True

        else:
            return False

    def changeLocation(self, x, y, newChar):
        if len(newChar) != 1:
            raise ValueError("Incorrect length for newChar")
        else:
            line = self.field[y]
            newLine = line[0:x] + newChar + line[x + 1:self.lenX]
            self.field[y] = newLine

    def printField(self):
        for line in self.field:
            print(line)

        

class site:

    def __init__ (self, x, y):
        self.x = x
        self.y = y

        self.visibleAsteroids = []
        self.visibleCount = 0


    def checkView(self, field):
        
        # Reset View
        self.visibleAsteroids = []

        # Scan up, stop at first found
        asteroidUp = None
        scanX = self.x
        for scanY in range(self.y - 1, -1, -1):
            if field.hasAsteroid(scanX, scanY):
                # Found one!
                asteroidUp = (scanX, scanY, pi/2)
                break

        if asteroidUp is not None:
            self.visibleAsteroids.append(asteroidUp)

        # Scan Down, stop at first found
        asteroidDown = None
        scanX = self.x
        for scanY in range(self.y + 1, field.lenY):
            if field.hasAsteroid(scanX, scanY):
                # Found one!
                asteroidDown = (scanX, scanY, -pi/2)
                break

        if asteroidDown is not None:
            self.visibleAsteroids.append(asteroidDown)

        # Scan Left, check for blocks
        asteroidsLeft = []
        for scanX in range(self.x - 1, -1, -1):
            for scanY in range(0, field.lenY):
                if field.hasAsteroid(scanX, scanY):
                    # Found one, check if already blocked (has same angle)
                    angle = atan2(self.y - scanY, scanX - self.x)
                    blockers = [blocker for blocker in asteroidsLeft if blocker[2] == angle]
                    if len(blockers) == 0:
                        # No blockers found!
                        asteroidsLeft.append((scanX, scanY, angle))

        self.visibleAsteroids += asteroidsLeft

        # Scan Right, check for blocks
        asteroidsRight = []
        for scanX in range(self.x + 1, field.lenX):
            for scanY in range(0, field.lenY):
                if field.hasAsteroid(scanX, scanY):
                    # Found one, check if already blocked (has same angle)
                    angle = atan2(self.y - scanY, scanX - self.x)
                    blockers = [blocker for blocker in asteroidsRight if blocker[2] == angle]
                    if len(blockers) == 0:
                        # No blockers found!
                        asteroidsRight.append((scanX, scanY, angle))
        
        self.visibleAsteroids += asteroidsRight
        self.visibleCount = len (self.visibleAsteroids)

    def destroyAsteroids(self, field):
        # Initialize Laser
        destroyedAsteroids = []
        self.laserAngle = pi/2

        while True:
                      
            # Find next asteroid (Might be none if asteroids were hidden behind last destroyed)
            nextAsteroid = self.seekLaser()

            # New scan
            self.checkView(field)

            # Got 'em - nothing left to destroy!
            if len(self.visibleAsteroids) == 0:
                break

            # Fire Laser?
            if nextAsteroid is not None:
                self.visibleAsteroids.remove(nextAsteroid)
                destroyedAsteroids.append(nextAsteroid)
                field.changeLocation(nextAsteroid[0], nextAsteroid[1], "*")

        return destroyedAsteroids

    def seekLaser(self):
        nextAsteroid = None
        
        if len(self.visibleAsteroids) > 0:
            # Put in angle order (clockwise is descending angle)
            sortedAsteroids = sorted(self.visibleAsteroids, key=lambda a: a[2], reverse=True)

            # Look for an asteroid at or below the current angle
            for asteroid in sortedAsteroids:
                if asteroid[2] <= self.laserAngle:
                    nextAsteroid = asteroid
                    break

            # If none beyond, wrap to the start of the list
            if nextAsteroid is None:
                nextAsteroid = sortedAsteroids[0]

            # point the laser
            self.laserAngle = nextAsteroid[2]
        
        return nextAsteroid


# Execute the program
if __name__ == "__main__":
    main()