import pytest
from dog_pack.dogs import Puggle, Boxer, Dog, DogPack


# @pytest.mark.skip('todo')
def test_boxer_create():
    assert Boxer()


# @pytest.mark.skip('todo')
def test_boxer_no_name():
    pooch = Boxer()
    actual = pooch.name
    expected = "unknown"
    assert actual == expected


# @pytest.mark.skip('todo')
def test_boxer_name():
    marv = Boxer("Marv")
    actual = marv.name
    expected = "Marv"
    assert actual == expected


# @pytest.mark.skip('todo')
def test_boxer_str():
    marv = Boxer("Marv")
    actual = marv.__str__()
    expected = "Marv"
    assert actual == expected


# @pytest.mark.skip('todo')
def test_boxer_repr():
    marv = Boxer("Marv")
    actual = marv.__repr__()
    expected = "Boxer('Marv')"
    assert actual == expected


# @pytest.mark.skip('todo')
def test_boxer_is_a_dog():
    marv = Boxer("Marv")
    actual = isinstance(marv, Dog)
    expected = True
    assert actual == expected


# @pytest.mark.skip('todo')
def test_boxer_greet(marv):
    actual = marv.greet()
    expected = "The name's Marv. Pleasure."
    assert actual == expected


# @pytest.mark.skip('todo')
def test_boxer_sleep(marv):
    actual = marv.sleep()
    expected = "zzz"
    assert actual == expected


# @pytest.mark.skip('todo')
def test_puggle_create():
    assert Puggle()


# @pytest.mark.skip('todo')
def test_puggle_no_name():
    pooch = Puggle()
    actual = pooch.name
    expected = "unknown"
    assert actual == expected


# @pytest.mark.skip('todo')
def test_puggle_name(lela):
    actual = lela.name
    expected = "Lela"
    assert actual == expected


# @pytest.mark.skip('todo')
def test_puggle_is_a_dog():
    lela = Puggle("Lela")
    actual = isinstance(lela, Dog)
    expected = True
    assert actual == expected


# @pytest.mark.skip('todo')
def test_puggle_greet(lela):
    actual = lela.greet()
    expected = "I am Lela. I am SO HAPPY to meet you!"
    assert actual == expected


# @pytest.mark.skip('todo')
def test_puggle_sleep(lela):
    actual = lela.sleep()
    expected = "zzz"
    assert actual == expected


# @pytest.mark.skip('todo')
def test_puggle_class_characteristics():
    actual = Puggle.get_characteristics()
    expected = "Like a mini boxer"
    assert actual == expected


# @pytest.mark.skip('todo')
def test_boxer_class_characteristics():
    actual = Boxer.get_characteristics()
    expected = "Boxers are lovers, not fighters."
    assert actual == expected


# @pytest.mark.skip('todo')
def test_puggle_count():
    actual = Puggle.get_breed_count()
    expected = 0
    assert actual == expected

    Puggle("Lela")

    actual = Puggle.get_breed_count()
    expected = 1
    assert actual == expected


# @pytest.mark.skip('todo')
def test_dog_count():
    Puggle("Lela")
    Boxer("Marv")

    assert Puggle.get_breed_count() == 1
    assert Boxer.get_breed_count() == 1
    assert Dog.get_all_dog_count() == 2


# @pytest.mark.skip('todo')
def test_dog_is_abstract():
    with pytest.raises(TypeError):
        Dog("Impossible")


# @pytest.mark.skip('todo')
def test_dogpack_create():
    assert DogPack()


# @pytest.mark.skip('todo')
def test_empty_dogpack():
    pack = DogPack()
    actual = pack.dogs
    expected = []
    assert actual == expected


# @pytest.mark.skip('todo')
def test_two_in_dogpack():
    dogs = [Boxer("Marv"), Puggle("Lela")]
    pack = DogPack(dogs)
    actual = len(pack.dogs)
    expected = 2
    assert actual == expected


# @pytest.mark.skip('todo')
def test_dogpack_str():
    dogs = [Boxer("Marv"), Puggle("Lela")]
    pack = DogPack(dogs)
    actual = pack.__str__()
    expected = "Marv Lela"
    assert actual == expected


# @pytest.mark.skip('todo')
def test_dogpack_repr():
    dogs = [Boxer("Marv"), Puggle("Lela")]
    pack = DogPack(dogs)
    actual = pack.__repr__()
    expected = "DogPack([Boxer('Marv'), Puggle('Lela')])"
    assert actual == expected


# @pytest.mark.skip('todo')
def test_dogpack_callout():
    dogs = [Boxer("Marv"), Puggle("Lela")]
    pack = DogPack(dogs)
    actual = pack.callout()
    expected = ["The name's Marv. Pleasure.", "I am Lela. I am SO HAPPY to meet you!"]
    assert actual == expected


# @pytest.mark.skip('todo')
def test_dogpack_instances():
    actual = len(DogPack.instances)
    expected = 0
    assert actual == expected
    DogPack()
    actual = len(DogPack.instances)
    expected = 1
    assert actual == expected


def test_describe_dogpack():
    actual = DogPack.describe()
    expected = 'A DogPack is "composed" of Dog instances.'
    assert actual == expected


# ### FIXTURES ###


@pytest.fixture(autouse=True)
def prep():
    """
    Reset the Class counts so it's fresh each test run
    """
    Puggle.count = 0
    Boxer.count = 0
    Dog.count = 0
    DogPack.instances = []


@pytest.fixture
def marv():
    return Boxer("Marv")


@pytest.fixture
def lela():
    return Puggle("Lela")
