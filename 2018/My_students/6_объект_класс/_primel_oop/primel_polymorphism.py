
"""
Полиморфизм является еще одним базовым аспектом объектно-ориентированного программирования 
и предполагает способность к изменению функционала, унаследованного от базового класса.
Например, пусть у нас будет следующая иерархия классов:
"""

class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст
 
    @property
    def name(self):
        return self.__name
 
    @property
    def age(self):
        return self.__age
 
    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")
 
    def display_info(self):
        print("Имя:", self.__name, "\tВозраст:", self.__age)
 
 
class Employee(Person):
    # определение конструктора
    def __init__(self, name, age, company):
        Person.__init__(self, name, age)
        self.company = company
 
    # переопределение метода display_info
    def display_info(self):
        Person.display_info(self)
        print("Компания:", self.company)
 
 
class Student(Person):
    # определение конструктора
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university
 
    # переопределение метода display_info
    def display_info(self):
        print("Студент", self.name, "учится в университете", self.university)


if __name__ == "__main__":

	people = [Person("Tom", 23), Student("Bob", 19, "Harvard"), Employee("Sam", 35, "Google")]
	 
	for person in people:
		person.display_info()
		print()
	'''
	Проверка типа объекта

	При работе с объектами бывает необходимо в зависимости от их типа выполнить те или иные операции.
	И с помощью встроенной функции isinstance() мы можем проверить тип объекта. 
	Эта функция принимает два параметра:

	isinstance(objict, type)
	'''
	print ("-----------------")
	print ("-----------------")

	for person in people:
		if isinstance(person, Student):
			print(person.university)

		elif isinstance(person, Employee):
			print (person.company)

		else:
			print(person.name)

		print()



















