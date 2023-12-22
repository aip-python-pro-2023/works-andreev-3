from random import choice


class QuestLocation:
    def __init__(self, description, jumps):
        self._description = description
        self._jumps = jumps

    def jump(self):
        return choice(self._jumps)

    def __str__(self):
        return f'QuestLocation(description={self._description}, jumps={self._jumps})'


class WinQuestLocation(QuestLocation):
    def __init__(self, description, payment):
        super().__init__(description, ['Вы победили!'])
        self.__payment = payment

    def __str__(self):
        return f'WinQuestLocation(description={self._description}, payment={self.__payment})'


class LoseQuestLocation(QuestLocation):
    def __init__(self, description):
        super().__init__(description, ['Вы проиграли...'])

    def __str__(self):
        return f'LoseQuestLocation(description={self._description})'


location = QuestLocation("Вы в сосновой чаще. Что будете делать?",
                         ['Бежать куда глаза глядят', 'Осмотреться'])

winLocation = WinQuestLocation("Вы осмотрелись, нашли хижину лесника со спутниковым телефоном и вызвали спасателей. Осталось немного, и Вы спасены!", 100_000)
loseLocation = LoseQuestLocation("Вы побежали куда глаза глядят и не заметили, что наступила ночь. Всё решили без Вас, и миссия провалена.")

print(location)
print(location.jump())
print(winLocation)
print(winLocation.jump())
print(loseLocation)
print(loseLocation.jump())
