from enum import Enum


class Title(Enum):
    Mr = "Mr"
    Mrs = "Mrs"
    Ms = "Ms"
    Mx = "Mx"
    Dr = "Dr"
    Sir = "Sir"
    Captain = "Captain"
    Prof = "Professor"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class Gender(Enum):
    M = "Male"
    F = "Female"
    T = "Transgender"
    GQ = "Genderqueer"
    A = "Agender"
    G = "Genderless"
    N = "Non-binary"
    TM = "Trans Man"
    TF = "Trans Woman"
    TG = "Third Gender"
    TS = "Two-Spirit"
    BG = "Bigender"
    GF = "Genderfluid"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class BodyType(Enum):
    Avg = "Average"
    Ath = "Athletic / Toned"
    Sl = "Slender"
    EP = "A Few Extra Pounds"
    C = "Curvy"
    H = "Heavy Set / Stocky"
    F = "Full Figured / Big Beautiful"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
