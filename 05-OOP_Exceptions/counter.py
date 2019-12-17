import functools


def instances_counter(cls):
    cls.instance = 0

    @staticmethod
    def get_created_instances():
        return cls.instance

    def reset_instances_counter(cls):
        cls.instance = 0
        return cls.instance

    get_created_instances = get_created_instances

    return cls



@instances_counter
class User:
    pass


if __name__ == '__main__':

    one = User()
    print(type(one))
    print(one.instance)
    two = User()
    print(two.instance)

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
