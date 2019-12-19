from operator import attrgetter

def main():
    with open("2019/2019-10/input.txt") as input_file:
        lines = input_file.readlines()

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
    
    mostVisibility = max(sites, key=attrgetter('visibleCount'))
    print(f"The best site is at {mostVisibility.x}, {mostVisibility.y} and can see {mostVisibility.visibleCount} asteroids.")


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
                asteroidUp = (scanX, scanY, None)
                break

        if asteroidUp is not None:
            self.visibleAsteroids.append(asteroidUp)

        # Scan Down, stop at first found
        asteroidDown = None
        scanX = self.x
        for scanY in range(self.y + 1, field.lenY):
            if field.hasAsteroid(scanX, scanY):
                # Found one!
                asteroidDown = (scanX, scanY, None)
                break

        if asteroidDown is not None:
            self.visibleAsteroids.append(asteroidDown)

        # Scan Left, check for blocks
        asteroidsLeft = []
        for scanX in range(self.x - 1, -1, -1):
            for scanY in range(0, field.lenY):
                if field.hasAsteroid(scanX, scanY):
                    # Found one, check if already blocked (has same slope)
                    slope = (scanY - self.y)/(scanX - self.x)
                    blockers = [blocker for blocker in asteroidsLeft if blocker[2] == slope]
                    if len(blockers) == 0:
                        # No blockers found!
                        asteroidsLeft.append((scanX, scanY, slope))

        self.visibleAsteroids += asteroidsLeft

        # Scan Right, check for blocks
        asteroidsRight = []
        for scanX in range(self.x + 1, field.lenX):
            for scanY in range(0, field.lenY):
                if field.hasAsteroid(scanX, scanY):
                    # Found one, check if already blocked (has same slope)
                    slope = (scanY - self.y)/(scanX - self.x)
                    blockers = [blocker for blocker in asteroidsRight if blocker[2] == slope]
                    if len(blockers) == 0:
                        # No blockers found!
                        asteroidsRight.append((scanX, scanY, slope))
        
        self.visibleAsteroids += asteroidsRight
        self.visibleCount = len (self.visibleAsteroids)

# Execute the program
if __name__ == "__main__":
    main()