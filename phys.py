import math



twopi = 2 * math.pi

class Acceleration:
    def __init__(self,mag,dir):
        self.mag = mag
        self.dir = dir

class Velocity:
    def __init__(self,mag,dir):
        self.mag = mag
        self.dir = dir

class Force:
    def __init__(self,mag,dir,time):
        self.mag = mag
        self.dir = dir
        self.time = time
    
class Object:
    def __init__(self,name,mass):
        self.name = name
        self.mass = mass
        self.x = 0
        self.y = 0
        self.acc = 0
        self.vel = 0
        self.forces=[]
    
    def netForce(self,forces):
        x1 = 0
        y1 = 0
        t = 99999999
        for f in forces:
            if (f.time < t) and (f.time != -1):
                t = f.time
            x1+= f.mag * math.sin(f.dir)
            y1+= f.mag * math.cos(f.dir)
        
        if x1 == 0:
            angle = twopi / 4
        else:
            angle = math.atan(y1/x1)

        netF = Force(math.sqrt((x1**2)+(y1**2)),angle,t)
        return(netF)
    
    def checkForces(self):
        for f in self.forces():
            if f.time>-1 and f.time <=0:
                self.forces.remove(f)
    
class Surface:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y

def applyForce(obj,force):
    obj.forces.append(force)

def updateAccel(obj,frate):
    nf = obj.netForce(obj.forces)

    if nf.mag > 0 and nf.time > 0:
        obj.acc = Acceleration((nf.mag) * obj.mass,nf.dir)
        obj.vel = Velocity((frate/1000) *obj.acc.mag, obj.acc.dir)
        ti = nf.time
        for f in obj.forces:
            if f.time == ti:
                f.time -= (frate/1000)

def newCoords(obj,frate,xinit,yinit):

    xnew = xinit + obj.vel.mag * (frate/1000) * math.cos(obj.vel.dir) + 1/2 * obj.acc.mag *math.cos(obj.acc.dir) * (frate/1000)**2
    ynew = yinit + obj.vel.mag * (frate/1000) * math.sin(obj.vel.dir) + 1/2 * obj.acc.mag *math.sin(obj.acc.dir)* (frate/1000)**2

    return(xnew,ynew)



                
    
    
        

    

        