import json
from random import randint


class Quest:
    count = 0

    def __init__(self, quest_id, name, description, difficulty, steps):
        Quest.count += 1
        self.id = quest_id
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.steps = steps

    # Преобразование в строчку
    def __str__(self):
        return f'Quest(id={self.id}, name={self.name}, difficulty={self.difficulty})'

    # Проверка на равенство
    def __eq__(self, other):
        return isinstance(other, Quest) and self.id == other.id

    def next_step(self, current_step, state):
        if state == 0:
            return 'DIED :('
        if state == 1:
            return 'SUCCESS'

    def mark_as_passed(self, user):
        user.passed_quests.append(self.id)

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
        self.passed_quests = []

    def __contains__(self, item):
        if isinstance(item, Quest):
            return item.id in self.passed_quests
        return False


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

user = User('Moi')
print(iikebana == user)

user.passed_quests.append(iikebana.id)
if iikebana in user:
    print('Passed!')

print(Quest.count)
# diehard.count = diehard.count + 1

# result = iikebana.next_step([], randint(0, 1))
# print(result)

gobsaur = Quest.create_from_json('quests/gobsaur.json')
print(gobsaur)
print(gobsaur.description)
