class OrthiaBlockCodeEngine:
    def Entrance(self, template: str, params: dict, mode: str = "phper", isHTMLSC: bool = True):
        self.__template = template
        self.__params = params
        self.__parsemode = mode
        self.__isHTMLSC = isHTMLSC
        self.MainAnalyzer()
        return self.__template

    def MainAnalyzer(self):
        pass