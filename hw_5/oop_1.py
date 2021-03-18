"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истело ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
from datetime import datetime, timedelta


class Homework:
    """
    A class to represent a homework and has method 'is_active',
    which check deadline of homework is passed or not.
    """

    def __init__(self, text: str, deadline: int):
        """
        Create an instance of a homework.

        Args:
            text: text for homework
            deadline: time to do homework
        """
        self.text = text
        self.deadline = timedelta(deadline)
        self.created = datetime.now()

    def is_active(self) -> bool:
        """
        Check if homework still actual.

        Returns:
            bool: True if deadline hasn't come False otherwise

        """
        homework_deadline = self.created + self.deadline
        now = datetime.now()
        return now <= homework_deadline


class Student:
    """
    A class to represent a student which has method 'do_homework'.
    'do_homework' takes class Homework object as argument
    and return this object if deadline of homework is not passed
    or print 'You are late' and return None otherwise.
    """

    def __init__(self, last_name, first_name):
        """
        Create an instance of a student.

        Args:
            last_name: string, firs name of student
            first_name: string, last name of student
        """
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework):
        """
        Do homework if it's actual. Print "You are late" otherwise.

        Args:
            homework: homework object

        Returns: homework if deadline is available, None otherwise

        """
        if homework.is_active():
            return homework
        print("You are late")
        return None


class Teacher:
    """
    A class to represent a teacher which has method 'create_homework'.
    'create_homework' returns the instance of class Homework
    with attributes 'text' and 'days'.

    """
    def __init__(self, last_name, first_name):
        """
        Create an instance of a teacher.

        Args:
            last_name: string, firs name of teacher
            first_name: string, last name of teacher
        """
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text, days):
        """
        Returns the instance of class Homework with attributes 'text' and 'days'.

        Args:
            text: text of homework
            days: the amount of days for homework

        Returns: an instance of created homework

        """
        return Homework(text, days)


if __name__ == '__main__':
    teacher = Teacher('Daniil', 'Shadrin')
    student = Student('Roman', 'Petrov')
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
