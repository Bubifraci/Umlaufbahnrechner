from models import planet

class Bahn():
    def __init__(self, title, pl, e, rp, ra, a):
        if(e == None and rp == None and ra == None and a == None):
            localE = input(f"Gebe die Exzentrizität e deiner Bahn {title} an (/ falls unbekannt): ")
            if(localE.isnumeric()): 
                self.e = float(localE)

            if(self.e != 0.0):
                self.rp = pl.radius + 1000.0 * float(input(f"Gebe die Höhe vom Perigäum deiner Bahn {title} an (in km): "))
                self.ra = pl.radius + 1000.0 * float(input(f"Gebe die Höhe vom Apogäum deiner Bahn {title} an (in km): "))
            else:
                radius = pl.radius + 1000.0 * float((input(f"Gib die Höhe deiner Kreisbahn {title} an (in km): ")))
                self.rp = radius
                self.ra = radius
            self.a = 0.5*(self.rp+self.ra)
            if(localE == "/"):
                self.e = (float)((self.ra/self.a)-1)
        else:
            self.e = e
            self.rp = rp
            self.ra = ra
            if(a == None or a == "/"):
                self.a = (float)(0.5*(rp+ra))
            else:
                self.a = a
