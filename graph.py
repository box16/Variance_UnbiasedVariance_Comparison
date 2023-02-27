import matplotlib.pyplot as pyplot


class BoxPlot:
    def __init__(self, title) -> None:
        self.__title = title
        self.__data = []
        self.__labels = []

    def add_plot(self, plot, label):
        if not plot:
            raise ValueError("plot is empty")
        if not label:
            raise ValueError("label is empty")
        self.__data.append(plot)
        self.__labels.append(label)

    def draw(self):
        if not self.__data:
            raise ValueError("data is empty")
        if not self.__labels:
            raise ValueError("labels is empty")
        if len(self.__data) != len(self.__labels):
            raise ValueError("Not match length")

        pyplot.title(self.__title)
        pyplot.boxplot(self.__data, labels=self.__labels)
        pyplot.show()
