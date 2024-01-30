class Student():
    def __init__(self, name, age) -> None:
        self.name = name
        self.__age = age

    def study(self, course_name):
        print(f"{self.name}正在学习{course_name},{self.__age}岁。")

    def __siyou(self):
        print(self.__age)


def main():
    student1 = Student("lizhen", 18)
    student1.study("数学")
    student1._Student__siyou()
    # print(f"{student1.name}, {student1.__age}")


if __name__ == '__main__':
    main()
