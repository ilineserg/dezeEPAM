"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как у словаря, сюда попадают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго, проверку делаю автотестами и просмотром кода.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict


class Human:

    def __init__(self, last_name, first_name):
        self.first_name = first_name
        self.last_name = last_name


class Student(Human):

    def do_homework(self, homework, solution):
        if homework.is_active is True:
            return HomeworkResult(homework, solution, author=self)
        else:
            raise DeadlineError('You are late')


class Teacher(Human):

    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

    @staticmethod
    def check_homework(homework_result):
        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework].append(homework_result)
            return True
        else:
            return False

    @staticmethod
    def reset_results(homework=None):
        if homework is None:
            Teacher.homework_done.clear()
        else:
            Teacher.homework_done[homework].clear()


class Homework:

    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    @property
    def is_active(self):
        return datetime.datetime.now() < self.created + self.deadline


class HomeworkResult:

    def __init__(self, homework, solution, author):
        if not isinstance(homework, Homework):
            raise ValueError
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = homework.created


class DeadlineError(Exception):
    """Error for situation if deadline of Homework has passed"""


if __name__ == '__main__':
    opp_teacher = Teacher('Daniil', 'Shadrin')
    advanced_python_teacher = Teacher('Aleksandr', 'Smetanin')

    lazy_student = Student('Roman', 'Petrov')
    good_student = Student('Lev', 'Sokolov')

    oop_hw = opp_teacher.create_homework('Learn OOP', 1)
    docs_hw = opp_teacher.create_homework('Read docs', 5)

    result_1 = good_student.do_homework(oop_hw, 'I have done this hw')
    result_2 = good_student.do_homework(docs_hw, 'I have done this hw too')
    result_3 = lazy_student.do_homework(docs_hw, 'done')
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print('There was an exception here')
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
