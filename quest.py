import json


class Quest:
    count: int = 0
    __id: int
    __name: str
    __description: str
    __difficulty: int
    __steps: list

    def __init__(self, quest_id, name, description, difficulty, steps):
        Quest.count += 1
        self.__id = quest_id
        self.__name = name
        self.__description = description
        self.__difficulty = difficulty
        self.__steps = steps

    def get_name(self):
        return self.__name

    # Геттер
    def get_description(self):
        return self.__description  # .replace('<ToPlanet>', 'Марс').replace('<ToStar>', 'Солнце')

    # Сеттер
    def set_description(self, new_description):
        if isinstance(new_description, str) and new_description != '':
            self.__description = new_description
        else:
            print('Wrong description')

    @property
    def description(self):
        return self.__description  # .replace('<ToPlanet>', 'Марс').replace('<ToStar>', 'Солнце')

    @description.setter
    def description(self, value):
        if isinstance(value, str) and value != '':
            self.__description = value
        else:
            print('Wrong description')

    # Преобразование в строчку
    def __str__(self):
        return f'Quest(id={self.__id}, name={self.__name}, difficulty={self.__difficulty})'

    # Проверка на равенство
    def __eq__(self, other):
        return isinstance(other, Quest) and self.__id == other.__id

    def next_step(self, current_step: int, state: int) -> str:
        if state == 0:
            return 'DIED :('
        if state == 1:
            return 'SUCCESS'

    def mark_as_passed(self, user):
        user.passed_quests.append(self.__id)

    @staticmethod
    def create_from_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        return Quest(
            quest_id=data['filename'],
            name=data['filename'],
            description=data['taskText'],
            difficulty=data['hardness'],
            steps=data['jumps'],
        )


class User:
    def __init__(self, user_id):
        self.id = user_id
        self.__name = 'Test'
        self.passed_quests = []

    def get_name(self):
        return self.__name

    # def __contains__(self, item):
    #     if isinstance(item, Quest):
    #         return item.__id in self.passed_quests
    #     return False


iikebana = Quest(
    'Moi',
    'Мастер Иике-баны',
    'Длинное интересное описание',
    70,
    []
)

diehard = Quest(
    'Diehard',
    'Страшная смерть',
    'Длинное и очень интересное описание',
    10,
    []
)

print(iikebana)
print(diehard)
print(iikebana == diehard)

user = User('Nick')
print(iikebana == user)

# user.passed_quests.append(iikebana.__id)
# if iikebana in user:
#     print('Passed!')

print(Quest.count)
# diehard.count = diehard.count + 1

# result = iikebana.next_step([], randint(0, 1))
# print(result)

gobsaur = Quest.create_from_json('quests/gobsaur.json')
print(gobsaur)
print(gobsaur.get_description())

gobsaur.description += '\n\nДополнительное описание'
print(gobsaur.description)
# gobsaur.set_description(gobsaur.get_description() + '\n\nДополнительное описание')
# print(gobsaur.get_description())

for item in gobsaur, user:
    print(item.get_name())
