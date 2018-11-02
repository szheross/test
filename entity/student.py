class Student():
    def __init__(self,id,name,age,score):
        self.name = name
        self.id = id
        self.age = age
        self.acore = score
        self.cls = 'Student'


class Teacher():
    def __init__(self,id,name,gonghao):
        self.name = name
        self.id = id
        self.gonghao = gonghao
        self.cls = 'teacher'

teacher = Teacher('666', 45)
print(teacher.__dict__)
