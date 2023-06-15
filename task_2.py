# Задача 2. Необходимо создать класс Animal, который имеет атрибуты Name (тип животного), Color (его расцветку)
# и Voice (издаваемый звук). Написать функцию, которая возвращает строку вида «It says <Voice>.», где <Voice>
# является уникальным атрибутом класса Animal. Задать три экземпляра класса Cow, Cat, Dog с уникальными атрибутами
# для каждого. Для каждого экземпляра вывести строку вида «<Name> is <Color>. It says <Voice>.»

class Animal:
    # уникальные атрибуты класса Animal
    def __init__(self, name, color, voice):
        self.name = name
        self.color = color
        self.voice = voice

    # метод класса, который возвращает «It says <Voice>.»
    def produce_sounds(self):
        return f'It says {self.voice}.'


cow = Animal(name='Burenka', color='black-white', voice='muuuu')
print(f'{cow.name} is {cow.color}. {cow.produce_sounds()}')

cat = Animal(name='Murlyka', color='ginger', voice='meow')
print(f'{cat.name} is {cat.color}. {cat.produce_sounds()}')

dog = Animal(name='Sharik', color='black', voice='gav')
print(f'{dog.name} is {dog.color}. {dog.produce_sounds()}')