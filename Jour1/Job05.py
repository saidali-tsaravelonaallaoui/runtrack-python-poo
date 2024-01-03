class Point:
    def __init__(self,x=10,y=5):
        self.x = x
        self.y = y
    def afficherLesPoints (self):
        print(f"Coordonnée du point :({self.x}, {self.y})")
    def afficherX (self):
        print(f"La coordonnée x est : {self.x}")
    def afficherY (self):
        print(f"La coordonnée y est : {self.y}")
    def changerX (self,newx):
        self.x = newx
    def changerY (self,newy):
        self.y = newy