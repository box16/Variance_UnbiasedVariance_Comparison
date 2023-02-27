import numpy


class Variance:
    def __init__(self, data, ddof) -> None:
        if data is None:
            raise ValueError("data is None")
        if ddof < 0:
            raise ValueError("ddof is negative")
        if ddof >= len(data):
            raise ValueError("ddof is larger than data")

        self.__variance = numpy.var(data, ddof=ddof)

    def get(self):
        return self.__variance


class VarianceCollection():
    def __init__(self, ddof) -> None:
        if ddof < 0:
            raise ValueError("ddof is negative")
        self.__members = []
        self.__ddof = ddof

    def append(self, data):
        variance = Variance(data, self.__ddof).get()
        self.__members.append(variance)

    def get(self):
        if not self.__members:
            raise ValueError("members is nothing")
        return self.__members


def CreateVarianceCollection():
    return VarianceCollection(0)


def CreateUnbiasedVarianceCollection():
    return VarianceCollection(1)
