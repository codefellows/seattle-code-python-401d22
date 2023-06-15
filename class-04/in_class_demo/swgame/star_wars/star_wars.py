class ForceUser:

    count = 0

    def attacking(self):
        return f"{self.name} is Force attacking!"

    def getting_hit(self):
        return f'{self.name} is being attacked!'

    def __str__(self):
        return f"{self.name} is in the House!"

    def __repr__(self):
        return f"JediMaster('{self.name}')"


    @classmethod
    def get_count(cls):
        return JediMaster.count + SithLord.count


class JediMaster(ForceUser):

    count = 0

    def __init__(self, name='Random Master', age=21):
        self.name = name
        self.age = age
        JediMaster.count += 1


    @staticmethod
    def get_code():
        return 'There is no emotion, there is PEACE.'

    @classmethod
    def get_count(cls):
        return cls.count


class SithLord(ForceUser):

    count = 0

    def __init__(self, name='Random Sith', age=21):
        self.name = name
        self.age = age
        SithLord.count += 1

    @staticmethod
    def get_code():
        return 'Peace is a lie, there is only PASSION.'

    @classmethod
    def get_count(cls):
        return cls.count


if __name__ == '__main__':
    jedi1 = JediMaster("Yoda")
    print(jedi1)
    # print(jedi1.attacking())
