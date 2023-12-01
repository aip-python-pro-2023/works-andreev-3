from random import randint


class Quest:
    def __init__(self, quest_id, name, description, difficulty, steps):
        self.id = quest_id
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.steps = steps

    def next_step(self, current_step, state):
        if state == 0:
            return 'DIED :('
        if state == 1:
            return 'SUCCESS'

    def mark_as_passed(self, user):
        user.passed.append(self.id)


class User:
    pass


iikebana = Quest(
    'Moi',
    'Мастер Иике-баны',
    'Длинное интересное описание',
    70,
    []
)

print(iikebana.name)
print(iikebana.description)
result = iikebana.next_step([], randint(0, 1))
print(result)
