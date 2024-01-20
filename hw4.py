class GeeksPeople:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Имя -{self.name},Введите почту -{self.email},Номер -{self.phone}"
    

class Student(GeeksPeople):
    def __init__(self, name, email, phone,student_id , group_where_study):
        GeeksPeople.__init__(self,name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study

    def study(self):
        print(f"Студента - {self.name} учится в {self.group_where_study} группе")

    def __str__(self):
        return super().__str__() + f"Id студента {self.student_id}, Группа студента {self.group_where_study}"
    

class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach ):
        GeeksPeople.__init__(self,name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def teach (self):
        print(f"Учитель - {self.name} преподает {self.group_where_teach} группе")

    def __str__(self):
        return super().__str__() + f"Id учителя {self.teacher_id}, Группа учителя {self.group_where_teach}, "
    
class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id):
        GeeksPeople.__init__(self,name, email, phone)
        self.admin_id = admin_id

    def create_group (self,cours_name):
        print(f"Админ -{self.name}, Создал {cours_name} группу")

    def __str__(self):
        return super().__str__() + f"Id Админа {self.admin_id} "
    
class Mentor(Student,Teacher):
    def __init__(self, name, email, phone, student_id, group_where_study, teacher_id, group_where_teach):
        super().__init__(name, email, phone, student_id, group_where_study)
        Teacher.__init__(self, name, email, phone, teacher_id, group_where_teach)


student = Student("Musulmankul", "musu@gmail.com", "0505617171", 7777, "14-2B")
print(student)
student.study()

teacher= Teacher("Сыймык", "syimyk@gmail.com", "0700000007", 5050, "14-2B")
print(teacher)
teacher.teach()

admin = Admin("Улан", "ulan@gmail.com", "0505050505", 5356)
print(admin)
admin.create_group("14-2B")

mentor = Mentor("Кудбухон", "kud@gmail.com", "0777770077", 1234567, "10-1B", 9876543, "15-2B")
print(mentor)
mentor.study()
mentor.teach()
