16.03.2018
"""
Выше мы рассмотрели, как создавать свойства. Но Python имеет также еще один - более элегантный способ определения свойств.
Этот способ предполагает использование аннотаций, которые предваряются символом @.

Для создания свойства-геттера над свойством ставится аннотация @property.

Для создания свойства-сеттера над свойством устанавливается аннотация имя_свойства_геттера.setter.

Перепишем класс Person с использованием аннотаций:


Во-первых, стоит обратить внимание, что свойство-сеттер определяется после свойства-геттера.

Во-вторых, и сеттер, и геттер называются одинаково - age. И поскольку геттер называется age,
 то над сеттером устанавливается аннотация @age.setter.
"""
class Person:
    def __init__(self, name, age):
        self.__name = name # устанавливаем имя
        self.__age = age # устанавливаем возраст

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1,100):
            self.__age = age
        else:
            print ('Недопустимый возраст')

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print ("Имя : ",self.__name,"\t возраст : ",self.__age)


tom = Person("Tom", 25)

tom.display_info()          # Имя: Tom  Возраст: 25


tom.age = -1346             # Недопустимый возраст
print(tom.age)

tom.age = 30
tom.display_info()          # Имя: Tom  Возраст: 25



    










