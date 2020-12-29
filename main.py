from threading import Lock, Thread

class SingletonMeta(type):
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances: # First creation
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance

        return cls._instances[cls] # Return the only object


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        print("A method")

class MySingleton(metaclass=SingletonMeta):
    def my_method(self):
        print("My method")

class MultithreadSingleton(metaclass=SingletonMeta):
    def __init__(self, value: str):
        self.value = value


s1 = Singleton()
s2 = Singleton()
s3 = MySingleton()
s4 = MySingleton()

print(id(s1), id(s2), id(s3), id(s4))

if id(s1) == id(s2):
    print("Singleton works, both variables contain the same instance.")
else:
    print("Singleton failed, variables contain different instances.")

## MULTITHREAD
def test_multithread_singleton(value):
    singleton = MultithreadSingleton(value)
    print(singleton.value)

process1 = Thread(target=test_multithread_singleton, args=("FOO",))
process2 = Thread(target=test_multithread_singleton, args=("BAR",))
process1.start()
process2.start()