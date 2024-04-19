class Student:
    pass


student1 = Student()
student2 = Student()

student1.fn = 'meghana'
student1.major = 'ec'

student2.fn = 'deepika'
student2.major = 'is'


print(student1.fn)
print(student2.major)


class Record:
    def __init__(self, fn, major):
        self.fn = fn
        self.major = major

    def name_with_major(self):
        return f'{self.fn} has {self.major} as major'

student1 = Record("meghana","ec")
student2 = Record("deepika","is")


print(student1.name_with_major())
print(Record.name_with_major(student2))
print(student2.major)

