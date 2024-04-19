class Parent:
    def pdisplay(self):
        print("parent")

class Child(Parent):
    def cdisplay(self):
        print("child")



c1 = Child()
c1.pdisplay()
c1.cdisplay()
