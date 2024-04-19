class Grandparent:
    def gdisplay(self):
        print("grand parent")

class Parent(Grandparent):
    def pdisplay(self):
        print("parent")

class Child(Parent):
    def cdisplay(self):
        print("child")



c1 = Child()
c1.gdisplay()
c1.pdisplay()
c1.cdisplay()
