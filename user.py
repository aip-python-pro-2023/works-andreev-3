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
