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
    
    def netForce(self):
        x1 = 0
        y1 = 0
        t = 99999999
        for f in self.forces():
            if (f.t < t) and (f.t != -1):
                t = f.t
            x1+= f.mag * math.sin(f.dir)
            y1+= f.mag * math.cos(f.dir)
        netF = Force(math.sqrt(x1^2+y1^2),math.atan(y1/x1),t)
        return(netF)
    
    def checkForces(self):
        for f in self.forces():
            if f.t>-1 and f.t <=0:
                self.forces.remove(f)
    
class Surface:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y

def applyForce(obj,force):
    obj.forces.append(force)

def updatePosition(obj):
    if obj.netForce().mag > 0 and obj.netForce().t > 0:
        obj.accel.dir = obj.netForce().dir
        obj.accel.mag = obj.netForce().mag
        
        ti = obj.netForce().t
        for f in obj.forces:
            if f.t == ti:
                f.t -= .02
    
        

    

        