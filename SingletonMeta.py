class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # این متد وقتی صدا زده می‌شود که می‌نویسیم: MyClass()
        if cls not in cls._instances:
            # اولین بار: نمونه‌ی جدید بساز
            cls._instances[cls] = super().__call__(*args, **kwargs)
        # دفعات بعد: همان نمونه قبلی را برگردان
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    """کلاس پایه‌ی Singleton که بقیه می‌توانند از آن ارث‌بری کنند."""
    pass

class Logger(Singleton):
    def __init__(self):
        self.messages = getattr(self, "messages", [])

    def log(self, msg):
        self.messages.append(msg)


class Config(Singleton):
    def __init__(self):
        self.values = getattr(self, "values", {})


l1 = Logger()
l2 = Logger()
c1 = Config()
c2 = Config()

print(l1 is l2)  # True  → Logger سینگلتون است
print(c1 is c2)  # True  → Config هم سینگلتون است
print(l1 is c1)  # False → هر کلاس instance خودش را دارد

l1.log("hello")
print(l2.messages)  # ['hello']  چون هر دو یکی هستند

