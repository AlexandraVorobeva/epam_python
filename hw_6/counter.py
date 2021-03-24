"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """
    Decorator for counting instances of a class.
    It has 2 methods (get_created_instances, reset_instances_counter)
    and 1 attribute.

    Args:
        cls: any class

    Returns: same class

    """
    cls.counter = 0

    def __new__(Cls):
        """
        Creates __new__ method and assign it to existing class.

        Args:
            Cls: any class

        Returns: instance of class

        """
        cls.counter += 1
        instance = super(cls, Cls).__new__(Cls)
        return instance

    cls.__new__ = __new__

    def get_created_instances(*arg):
        """
        This method returns count of instances of the class created.

        Args:
            *arg: any class

        Returns: count of instances

        """
        return cls.counter

    def reset_instances_counter(*arg):
        """
        This method resets counter and returns previous value.

        Args:
            *arg: any class

        Returns: creation count

        """
        cls.counter, count_last = 0, cls.counter
        return count_last

    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
