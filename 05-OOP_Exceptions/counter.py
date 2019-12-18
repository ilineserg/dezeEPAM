"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


import functools


def instances_counter(cls):
    setattr(cls, 'instance_count', 0)

    def init_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cls.instance_count += 1
            return func(*args, **kwargs)
        return wrapper


    @staticmethod
    def get_created_instances():
        return cls.instance_count

    @staticmethod
    def reset_instances_counter():
        temp = cls.instance_count
        cls.instance_count = 0
        return temp

    setattr(cls, '__init__', init_wrapper(cls.__init__))
    setattr(cls, 'get_created_instances', get_created_instances)
    setattr(cls, 'reset_instances_counter', reset_instances_counter)

    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3

