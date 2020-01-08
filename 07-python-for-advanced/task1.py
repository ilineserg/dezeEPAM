"""
Реализовать такой метакласс, что экземпляры класса созданного с помощью него
будут удовлетворять следующим требованиям:
* объекты созданные с одинаковыми аттрибутами будут одним и тем же объектом
* объекты созданные с разными аттрибутами будут разными объектами
* у любого объекта есть мозможность получить доступ к другим объектам
    того же класса
>>> unit1 = SiamObj('1', '2', a=1)
>>> unit2 = SiamObj('1', '2', a=1)
>>> unit1 is unit2
True
>>> unit3 = SiamObj('2', '2', a=1)
>>> unit3.connect('1', '2', 1).a = 2
>>> unit2.a == 2
True
>>> pool = unit3.pool
>>> print(len(pool))
2
>>> del unit3
>>> print(len(pool))
1
"""

import sys
from weakref import WeakValueDictionary, WeakKeyDictionary


class SiamMeta(type):
    _pool = WeakValueDictionary()

    def __call__(cls, *args, **kwargs):

        def get_key(*args_, **kwargs_):
            return str(args_ + tuple(kwargs_.values()))

        def _delete(obj_):
            _key = get_key(*obj_.args, **obj_.kwargs)
            if _key in cls._pool:
                del cls._pool[_key]

        def _connect(*args_):
            _key = get_key(*args_)
            return cls._pool[_key]

        key = get_key(*args, **kwargs)

        if key not in cls._pool:
            obj = super(SiamMeta, cls).__call__(*args, **kwargs)
            obj.connect = _connect
            obj.pool = cls._pool
            cls._pool[key] = obj
            cls.__del__ = _delete

        return cls._pool[key]


class SiamObj(metaclass=SiamMeta):

    def __init__(self, *args, **kwargs):
        self.__dict__ = dict(kwargs)
        self.args = args
        self.kwargs = kwargs


if __name__ == "__main__":
    unit1 = SiamObj('1', '2', a=1)
    unit2 = SiamObj('1', '2', a=1)

    print(unit1 is unit2)

    unit3 = SiamObj('2', '2', a=1)

    unit3.connect('1', '2', 1).a = 2
    print(unit2.a == 2)

    pool = unit3.pool
    print(len(pool))

    del unit3
    print(len(pool))