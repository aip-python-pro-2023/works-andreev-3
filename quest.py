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

    def __repr__(self):
        return f'Quest(id="{self.__id}", name="{self.__name}")'

    @property
    def quest_id(self):
        return self.__id

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


class QuestRepository:
    quests: list[Quest] = None

    def __init__(self):
        self.quests = [
            Quest(
                'Moi',
                'Мастер Иике-баны',
                'Длинное интересное описание',
                70,
                []
            ),
            Quest(
                'Diehard',
                'Страшная смерть',
                'Длинное и очень интересное описание',
                10,
                []
            )
        ]

    def add(self, new_quest: Quest):
        self.quests.append(new_quest)

    def get_all(self):
        return self.quests.copy()

    def get_by_id(self, quest_id):
        return [quest for quest in self.quests if quest.quest_id == quest_id][0]
