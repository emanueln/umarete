# Name list (40 of each)
from random import seed
from random import randint
seed(1)

boy_names = ["Noah","Liam","William","Mason","James","Benjamin","Jacob","Michael","Elijah","Ethan","Alexander","Oliver","Daniel","Lucas","Matthew","Aiden","Jackson","Logan","David","Joseph","Samuel","Henry","Owen","Sebastian","Gabriel","Carter","Jayden","John","Luke","Anthony","Isaac","Dylan","Wyatt","Andrew","Joshua","Christopher","Grayson","Jack","Julian","Ryan"]
girl_names = ["Emma","Olivia","Ava","Sophia","Isabella","Mia","Charlotte","Abigail","Emily","Harper","Amelia","Evelyn","Elizabeth","Sofia","Madison","Avery","Ella","Scarlett","Grace","Chloe","Victoria","Riley","Aria","Lily","Aubrey","Zoey","Penelope","Lillian","Addison","Layla","Natalie","Camila","Hannah","Brooklyn","Zoe","Nora","Leah","Savannah","Audrey","Claire"]

last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter"]

def random_boy_name():
    index = randint(0, 39)
    return boy_names[index]

def random_girl_name():
    index = randint(0, 39)
    return girl_names[index]


def random_last_name():
    index = randint(0, 39)
    return last_names[index]