from data import values

class Planet():

    def __init__(self, name = None):
        if(name == None):
            self.title = input("Wie lautet der Name deines Planeten: ")
        else:
            self.title = name
        
        checkTitle = self.title.lower()
        vals = values.Values()
        planetVals = []
        match checkTitle:
            case 'erde':
                planetVals = [vals.massErde, vals.rErde]
            case 'venus':
                planetVals = [vals.massVenus, vals.rVenus]
            case 'saturn':
                planetVals = [vals.massSaturn, vals.rSaturn]
            case 'mars':
                planetVals = [vals.massMars, vals.rMars]
            case 'jupiter':
                planetVals = [vals.massJupiter, vals.rJupiter]
            case 'mond':
                planetVals = [vals.massMond, vals.rMond]

        if(planetVals == []):
            self.mass = (float)(input(f"Gebe die Masse des Planeten {self.title} an (in kg): "))
            self.radius = 1000.0 * (float)(input(f"Gebe den Radius des Planeten {self.title} an (in km): "))
        else:
            self.mass = planetVals[0]
            self.radius = planetVals[1] * 1000.0
