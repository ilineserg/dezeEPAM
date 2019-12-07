import datetime


class Student:

    def __init__(self, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def do_homework(homework):
        return homework if homework.is_active else 'You are late'


class Teacher:

    def __init__(self, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)


class Homework:

    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    @property
    def is_active(self):
        if datetime.datetime.now() > self.created + self.deadline:
            return False
        else:
            return True


if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    print(teacher.last_name, teacher.first_name)  # Daniil
    print(student.first_name, student.last_name)  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762
    print(expired_homework.deadline)  # 0:00:00
    print(expired_homework.text)  # 'Learn functions'
    print(expired_homework.is_active)

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    print(oop_homework.deadline)  # 5 days, 0:00:00
    print(oop_homework.text)
    print(oop_homework.is_active)

    print(student.do_homework(oop_homework))
    print(student.do_homework(expired_homework))  # You are late
