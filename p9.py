from abc import ABCMeta, abstractmethod


class Person(object, metaClass = ABCMeta):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def lizhen(cls):
        return cls("lizhen", 100)

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @staticmethod
    def is_lizhen(name):
        return name == 'lizhen'

    @abstractmethod
    def like(self):
        pass

    def print_self(self):
        print(f"{self._name} , {self._age}")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    def study(self):
        print(f"{self._name}, {self._age}岁,正在学习{self._grade}")

    def like(self):
        super().like()
        print("喜欢玩")


class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    def teach(self, course_name):
        print(f"{self._name}, {self._title}, {self._age}岁,正在讲{course_name}")

    def like(self):
        super().like()
        print("喜欢计算机")


def main():
    # person = Person("lizhen", 18)
    # person.age = 19
    # person._name = "lizhen1"
    # print(person._name)
    # print(Person.is_lizhen('lizhen'))
    # person.print_self()
    # Person.print_self(person)

    # lizhen = Person.lizhen()
    # lizhen.print_self()

    student = Student("yiyi", 6, "一年级")
    teacher = Teacher("天天", 25, "语文老师")
    student.study()
    student.like()
    teacher.teach("第一课")
    teacher.like()


if __name__ == '__main__':
    main()
