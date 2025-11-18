from models import planet
from models import bahn
from math import sqrt
import os

G = 6.67259*pow(10, -11)

def hohmann_transfer(initialBahn = None, endBahn = None, setPlanet = None):
    if(initialBahn == None or endBahn == None or setPlanet == None):
        pl = initPlanet(True)
        baI = initBahn(False, "Initial", pl)
        baE = initBahn(False, "Ziel", pl)
    else:
        pl = setPlanet
        baI = initialBahn
        baE = endBahn


    baT = bahn.Bahn("Transfer", pl, None, baI.rp, baE.ra, "/")
    vp = vis_viva_equation(pl, baI.rp, baT.a)
    vi = vis_viva_equation(pl, baI.rp, baI.a)
    va = vis_viva_equation(pl, baT.ra, baT.a)
    vf = vis_viva_equation(pl, baE.ra, baE.a)
    dv = abs(vp-vi) + abs(vf-va)
    return dv

def initBahn(printOut, title, pl):
    ba = bahn.Bahn(title, pl, None, None, None, None)
    if(printOut):
        print(f"Deine Bahn hat die Exzentrizität {ba.e}, den Apogäumsradius {ba.ra}, den Perigäumsradius {ba.rp} und die große Halbachse {ba.a}")
    return ba

def initPlanet(printOut):
    pl = planet.Planet()
    if(printOut):
        print(f"Dein Planet ist {pl.title} mit der Masse {pl.mass}kg und dem Radius {pl.radius}km")
    return pl

def vis_viva_equation(pl, point, a):
    return sqrt(G*pl.mass*(2/point-1/a))

def test_21a(startHeight, endHeight):
    planetNames = ['Venus', 'Erde', 'Mars', 'Jupiter', 'Saturn', 'Mond']
    planetObjs = []
    results = []
    for name in planetNames:
        planetObjs.append(planet.Planet(name=name))

    for pl in planetObjs:
        startRadius = startHeight * 1000 + pl.radius
        endRadius = endHeight * 1000 + pl.radius
        initialBahn = bahn.Bahn("Initial", pl, 0, startRadius, startRadius, startRadius)
        endBahn = bahn.Bahn("End", pl, 0, endRadius, endRadius, endRadius)
        results.append(hohmann_transfer(initialBahn=initialBahn, endBahn=endBahn, setPlanet=pl))

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "hohmann_ergebnisse.txt")

    with open(file_path, "w", encoding="utf-8") as f:
            
            header = f"Ergebnisse Hohmann-Transfer ({startHeight}km -> {endHeight}km)\n"
            header += "-" * 40 + "\n"
            
            f.write(header)
            print(header, end="")

            i = 0
            for res in results:
                line = f"{planetNames[i]:<10}: {res:.5f} m/s\n"
                
                f.write(line)      
                print(line, end="")
                i += 1
                
    print(f"\nDaten wurden erfolgreich gespeichert in:\n{file_path}")

test_21a(350, 900)