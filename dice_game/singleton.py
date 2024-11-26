class ClassicSingleton:

    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)

        return cls


class SimpleSingleton:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)

        return  cls

# Setting rules to create another classes - "Factory of classes" - Lazy instantiation
# class SingletonMeta(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             instance = super().__call__()
#             cls._instances[cls] = instance
#         return cls._instances[cls]
#
# class Singleton(metaclass=SingletonMeta):
#     def business_logic(self):
#         pass

# Eager instantiation
class SingletonMeta(type):

    _instances = {}

    def __init__(cls, name):
        super().__init__(name)
        cls._instances[cls] = super().__call__()

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __inti__(self):
        pass


singleton = Singleton()