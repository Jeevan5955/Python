class Cylinder:
    
    def __init__(self,height=1,radius=1):
        
        self.height = height
        self.radius = radius
        
    def volume(self):
        
        # V=πr^2h
        
        return 3.14 * (self.radius**2) * self.height
    
    def surface_area(self):
        
        # A=2πrh+2πr^2
        
        return (2 * 3.14 * self.radius * self.height) + (2 * 3.14 * (self.radius ** 2) )
