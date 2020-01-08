"""
Написать свое property c кэшем и таймаутом
полностью повторяет поведение стандартной property за исключением:
    * хранит результат работы метода некоторое время, которое передается
      параметром в инициализацию проперти
    * пересчитывает значение, если таймер истек
"""

import time
import uuid


def timer_property(t):

    class Property(object):

        def __init__(self, fn_get=None, fn_set=None, fn_del=None, doc=None):

            self.fn_get = fn_get
            self.fn_set = fn_set
            self.fn_del = fn_del

            self.last_update = 0
            self.cached_data = None
            self.__doc__ = doc

        def __get__(self, obj, _type=None):
            if obj is None:
                return self
            current_time = time.time()
            if (current_time - self.last_update) > t:
                self.cached_data = self.fn_get(obj)
                self.last_update = current_time
            return self.cached_data

        def __set__(self, obj, value):
            self.last_update = time.time()
            self.cached_data = value

        def __delete__(self, obj):
            self.fn_del(obj)

        def getter(self, fn_get):
            return type(self)(fn_get, self.fn_set, self.fn_del, self.__doc__)

        def setter(self, fn_set):
            return type(self)(self.fn_get, fn_set, self.fn_del, self.__doc__)

        def deleter(self, fn_del):
            return type(self)(self.fn_get, self.fn_set, fn_del, self.__doc__)

    return Property


class Message:

    @timer_property(t=10)
    def msg(self):
        self._msg = self.get_message()
        return self._msg

    @msg.setter # reset timer also
    def msg(self, param):
        self._msg = param

    def get_message(self):
        """
        Return random string
        """
        return uuid.uuid4()


if __name__ == '__main__':
    m = Message()

    initial = m.msg
    print("initial", initial, m.msg)

    assert initial is m.msg
    print("assert initial is m.msg", m.msg)


    time.sleep(10)
    assert initial is not m.msg
    print("assert initial is not m.msg", m.msg)

    initial = m.msg
    print("new initial", initial)
    m.msg = uuid.uuid4()
    print(m.msg)
    assert initial is not m.msg
    print("assert new initial is not m.msg", m.msg)
