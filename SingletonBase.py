class SingletonBase:
    _instances = {}  # برای هر کلاس فرزند، یک نمونه جداگانه

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # اولین بار از این کلاس (یا زیرکلاس) نمونه ساخته می‌شود
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]


class Logger(SingletonBase):
    def __init__(self):
        # مراقب باشید: __init__ در هر فراخوانی صدا زده می‌شود
        # پس باید idempotent باشد یا با فلگ کنترل شود
        self.messages = getattr(self, "messages", [])

    def log(self, msg):
        self.messages.append(msg)


class Config(SingletonBase):
    def __init__(self):
        self.values = getattr(self, "values", {})


# تست
l1 = Logger()
l2 = Logger()
c1 = Config()
c2 = Config()

print(l1 is l2)  # True
print(c1 is c2)  # True
print(l1 is c1)  # False
