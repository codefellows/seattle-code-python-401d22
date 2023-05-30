from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod


class DogPack:
    """
    A class that represents a collection of dogs.
    Each instance of DogPack is passed a list of dog instances
    representing the dogs of the pack. The class variable
    instances represents all of the DogPack instances created.
    """

    instances = []

    def __init__(self, dogs=None):
        # Python Gotcha Warning: do NOT use mutable data type as default
        self.dogs = dogs or []
        DogPack.instances.append(self)

    # returns a string that represents the object. used in print() and str()
    def __str__(self):
        dog_strings = [str(dog) for dog in self.dogs]
        return " ".join(dog_strings)

    # returns a string that can be used to reconstruct the object
    def __repr__(self):
        return f"DogPack({self.dogs})"

    def callout(self):
        return [dog.greet() for dog in self.dogs]

    @classmethod
    def list_packs(cls):
        return cls.instances

    @staticmethod
    def describe():
        return 'A DogPack is "composed" of Dog instances.'


class Dog(ABC):
    """
    Base class for different dogs, each dog has their own breed, eg boxer or puggle.
    """

    count = 0

    def __init__(self, name="unknown"):
        self.name = name
        self.__class__.increase_count()

    def __str__(self):
        return self.name

    # write this once Boxer and Puggle have been refactored
    # def __repr__(self):
    #     print(dir(self)) # show how "dir" will display attributes
    #     return f"{self.__class__.__name__}('{self.name}')"

    def sleep(self):
        return "zzz"

    @abstractclassmethod
    def increase_count(cls):
        """
        subclass must implement this class method
        """
        Dog.count += 1

    @abstractmethod
    def greet(self):
        """
        subclass must implement this instance method
        """
        pass

    @abstractstaticmethod
    def get_characteristics():
        """
        subclass must implement this static method
        """
        pass

    @classmethod
    def get_all_dog_count(cls):
        return cls.count


class Boxer(Dog):
    """
    A super cool dog
    """

    count = 0

    def __repr__(self):
        # refactor to use self.__class__.__name__
        # later will do same with Puggle
        return f"Boxer('{self.name}')"

    @classmethod
    def increase_count(cls):
        cls.count += 1
        return super().increase_count()

    def greet(self):
        return f"The name's {self.name}. Pleasure."

    @staticmethod
    def get_characteristics():
        return "Boxers are lovers, not fighters."

    @classmethod
    def get_breed_count(cls):
        return cls.count


class Puggle(Dog):
    """
    adorably spunky
    """

    count = 0

    # refactor to use self.__class__.__name__
    # then notice duplication with Boxer
    # then "pull up" to super class
    def __repr__(self):
        return f"Puggle('{self.name}')"

    def greet(self):
        return f"I am {self.name}. I am SO HAPPY to meet you!"

    @classmethod
    def increase_count(cls):
        cls.count += 1
        return super().increase_count()

    @staticmethod
    def get_characteristics():
        return "Like a mini boxer"

    @classmethod
    def get_breed_count(cls):
        return cls.count
