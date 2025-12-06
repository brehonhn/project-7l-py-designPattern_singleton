# Singleton Design Pattern in Python
این پروژه پیاده‌سازی الگوی طراحی **Singleton** را با دو روش مختلف نشان می‌دهد:

1. Singleton با استفاده از متد `__new__`  
2. Singleton با استفاده از **MetaClass** (وراثت‌پذیر و استاندارد)

---

## 📌 Singleton چیست؟
Singleton یک الگوی طراحی از نوع **Creational** است که تضمین می‌کند:

- یک کلاس فقط **یک نمونه (instance)** در کل برنامه داشته باشد  
- دسترسی به آن نمونه از یک نقطهٔ مشخص انجام شود  
- جلوگیری از ساخت نمونه‌های غیرضروری یا ناخواسته  

این الگو معمولاً برای Logger، Config، Connection Pool، Database و … استفاده می‌شود.

---

# 1️⃣ روش اول: Singleton ساده با `__new__`

در این روش یک کلاس پایه تعریف می‌کنیم که فقط اجازه می‌دهد از هر کلاس فرزند آن، **یک نمونه** ساخته شود.

### 📦 فایل: `SingletonBase.py`

```python
class SingletonBase:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]
