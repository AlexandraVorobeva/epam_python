import pytest

from hw_6.oop_2 import DeadlineError, HomeworkResult, Student, Teacher


@pytest.fixture()
def opp_teacher():
    return Teacher("Daniil", "Shadrin")


@pytest.fixture()
def advanced_python_teacher():
    return Teacher("Aleksandr", "Smetanin")


@pytest.fixture()
def lazy_student():
    return Student("Roman", "Petrov")


@pytest.fixture()
def good_student():
    return Student("Lev", "Sokolov")


@pytest.fixture()
def expired_homework(opp_teacher):
    return opp_teacher.create_homework("Learn functions", 0)


@pytest.fixture()
def oop_hw(opp_teacher):
    return opp_teacher.create_homework("Learn OOP", 1)


@pytest.fixture()
def docs_hw(opp_teacher):
    return opp_teacher.create_homework("Read docs", 5)


def test_do_current_homework(good_student, docs_hw):
    homework = good_student.do_homework(docs_hw, "I have done this hw.")
    assert isinstance(homework, HomeworkResult)
    assert homework.author is good_student
    assert homework.solution == "I have done this hw."
    assert homework.homework is docs_hw


def test_do_homework_raising_deadline_error(lazy_student, expired_homework):
    with pytest.raises(DeadlineError, match="You are late"):
        lazy_student.do_homework(expired_homework, "Solution")


def test_homework_result_with_not_a_homework(good_student):
    with pytest.raises(TypeError):
        HomeworkResult(good_student, "fff", "Solution")


def test_check_homework(opp_teacher, good_student, oop_hw):
    result = good_student.do_homework(oop_hw, "I have done this hw")
    assert opp_teacher.check_homework(result) is True
    assert result.homework in opp_teacher.homework_done


def test_reset_result():
    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0


def test_reset_result_delete_all_from_homework_done():
    Teacher.reset_results()
    assert not bool(Teacher.homework_done)


def test_reset_result_delete_one_homework(oop_hw, opp_teacher, good_student):
    result = good_student.do_homework(oop_hw, "I have done this hw")
    opp_teacher.check_homework(result)
    assert len(Teacher.homework_done) == 1
    opp_teacher.reset_results()
    assert Teacher.homework_done == {}


def test_check_homework_unique_solution(good_student, oop_hw, opp_teacher):
    result = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(oop_hw, "I have done this hw")
    opp_teacher.check_homework(result)
    opp_teacher.check_homework(result_2)
    assert len(opp_teacher.homework_done) == 1
