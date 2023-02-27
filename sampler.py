import abc
import numpy


class Sampler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self):
        raise NotImplementedError()


class NormalSampler(Sampler):
    def __init__(self, mean, std, sample_size) -> None:
        if std < 0:
            raise ValueError("std is negative")
        if sample_size <= 0:
            raise ValueError("sample size is negative")

        self.__mean = mean
        self.__std = std
        self.__sample_size = sample_size

    def get(self) -> numpy.ndarray:
        return numpy.random.normal(loc=self.__mean,
                                   scale=self.__std,
                                   size=self.__sample_size)
