class SingletonSimple:
    _instance = None   # تنها نمونه‌ی این کلاس

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# تست:
s1 = SingletonSimple()
s2 = SingletonSimple()

print(s1 is s2)  # True
