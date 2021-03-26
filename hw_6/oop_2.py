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

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
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

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict
from datetime import datetime, timedelta


class DeadlineError(Exception):
    """Exception for timeout homework deadline"""
    def __init__(self):
        super().__init__("You are late.")


class Person:
    """ A class to represent a person. """
    def __init__(self, first_name, last_name):
        """
        Create an instance of a person.

        Args:
            first_name: string, firs name of person
            last_name: string, last name of person
        """
        self.last_name = last_name
        self.first_name = first_name


class Homework:
    """
    A class to represent a homework and has method 'is_active',
    which check deadline of homework is passed or not.
    """
    def __init__(self, text, deadline):
        """
        Create an instance of a homework.

        Args:
            text: text for homework
            deadline: time to do homework
        """
        self.text = text
        self.deadline = timedelta(days=deadline)
        self.created = datetime.now()

    def is_active(self):
        """
        Check if homework still actual.

        Returns:
            bool: True if deadline hasn't come False otherwise

        """
        homework_deadline = self.created + self.deadline
        now = datetime.now()
        return now <= homework_deadline


class Student(Person):
    """
    A class to represent a student which has method 'do_homework'.
    'do_homework' takes class Homework object as argument
    and return an instance of HomeworkResult if deadline of homework is not passed
    or raise DeadlineError and return None otherwise.
    """
    def do_homework(self, homework, solution):
        """
        Return homework if deadline is available, raise exception otherwise.

        Args:
            homework: homework object
            solution: string

        Returns:
            cls: completed homeworks

        """
        if homework.is_active():
            return HomeworkResult(self, homework, solution)
        raise DeadlineError()


class HomeworkResult:
    """A class to represent successfully completed homeworks."""
    def __init__(self, student, homework, solution):
        """
        This method represents successfully completed homeworks.

        Args:
            student: Student object
            homework: Homework object
            solution: some text as a solution for homework
        """
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object.")
        self.homework = homework
        self.solution = solution
        self.author = student
        self.created = datetime.now()


class Teacher(Person):
    """
    A class to represent a teacher which has methods 'create_homework',
    'check_homework', 'reset_results'.
    """

    homework_done = defaultdict(list)

    def create_homework(self, text, deadline):
        """
        Returns the instance of class Homework with attributes 'text' and 'deadline'.

        Args:
            text: text of homework
            deadline: the amount of days for homework

        Returns: an instance of created homework

        """
        return Homework(text, deadline)

    def check_homework(self, hw_result):
        """
        Check if text of answer is longer than 5 symbols and doesn't duplicate someone else's.

        Args:
            hw_result: HomeworkResult object

        Returns:
            bool: False - if homework incorrect, True otherwise

        """
        if len(hw_result.solution) < 5:
            return False
        for _items in Teacher.homework_done[hw_result.homework]:
            if hw_result.solution in _items.solution:
                return False
        Teacher.homework_done[hw_result.homework].append(hw_result)

    def reset_results(homework = None):
        """
        If Homework is given - method delete all saved solutions in 'homework_done' for this Homework.
        If no argument is given, method reset all 'homework_done'

        Args:
            homework: object Homework as optional argument

        """
        if homework is None:
            Teacher.homework_done.clear()
        else:
            Teacher.homework_done.pop(homework)


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
