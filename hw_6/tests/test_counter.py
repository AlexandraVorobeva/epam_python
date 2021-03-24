from hw_6.counter import instances_counter


def test_get_created_instances():
    @instances_counter
    class User:
        pass

    assert User.get_created_instances() == 0
    user_1 = User()
    assert user_1.get_created_instances() == 1
    user_2 = User()
    assert user_2.get_created_instances() == 2


def test_reset_instances_counter_return_count_of_instances():
    @instances_counter
    class User:
        pass

    user_1, user_2 = User(), User()
    assert user_1.get_created_instances() == 2
    assert user_1.reset_instances_counter() == 2


def test_reset_instances_counter_reset():
    @instances_counter
    class User:
        pass

    user_1, user_2 = User(), User()
    assert user_1.get_created_instances() == 2
    user_1.reset_instances_counter()
    assert user_1.get_created_instances() == 0
