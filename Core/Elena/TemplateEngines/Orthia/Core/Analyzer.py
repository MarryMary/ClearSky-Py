import re
from Core.Elena.TemplateEngines.Orthia.Core.OrthiaBlockCodeEngine import OrthiaBlockCodeEngine
from Core.Elena.TemplateEngines.Orthia.Core.OrthiaBuildInFunctions import OrthiaBuildInFunctions

class Analyzer:
    def __init__(self):
        self.__param = ""
        self.__template = ""
        self.__parsemode = ""

    def Main(self, template: str, param: dict = dict(), mode: bool = False, writer: str = "phper", isHTMLSC: bool = False):
        if(writer.strip() != ""):
            if(len(param) != 0 and not mode):
                self.__template = template
                self.isHTMLSC = isHTMLSC
                self.__param = param
                self.__parsemode = writer
                analyzer = OrthiaBlockCodeEngine()
                self.__template = analyzer.Entrance(self.__template, self.param, self.__parsemode, self.isHTMLSC)
                self.VariableInserter()
                return self.__template
            elif(len(param) == 0):
                self.__template = template
                self.isHTMLSC = isHTMLSC
                self.__param = param
                self.__parsemode = writer
                analyzer = OrthiaBlockCodeEngine()
                self.__template = analyzer.Entrance(self.__template, self.param, self.__parsemode, self.isHTMLSC)
                return self.__template
            else:
                self.__template = template
                self.isHTMLSC = isHTMLSC
                self.__param = param
                self.__parsemode = writer
                self.VariableInserter()
                return self.__template
        else:
            pass

    def VariableInserter(self):
        for ORTHIASYSKEY, ORTHIASYSVAL in self.__param:
            exec("{} = {}".format(ORTHIASYSKEY, ORTHIASYSVAL))
        ORTHIASYSNS = locals()
        prepared = ""
        ORTHIASYSTEMPLATE = self.__template.split("\n")
        self.__template = ""
        for ORTHIASYSLINE in ORTHIASYSTEMPLATE:
            ORTHIASYSPATTERN = r'/\{{.+?\}}/'
            ORTHIASYSVALIABLE = re.match(PRTHOASYSPATTERN, ORTHIASYSLINE)
            for ORTHIASYSVALS in ORTHIASYSVALIABLE:
                for ORTHIASYSV in ORTHIASYSVALS:
                    if(self.__parsemode == "phper"):
                        ORTHIAVAL_TRIMED = ORTHIASYSV.strip().lstrip("{{").rstrip("}}").strip().lstrip("$")
                        ORTHIAVAL_UNTRIMED = ORTHIAVAL_TRIMED
                        ORTHIAVAL_TRIMED = val_trimed.split("->")
                    elif(self.__parsemode == "pythonista"):
                        ORTHIAVAL_TRIMED = ORTHIASYSV.strip().lstrip("{{").rstrip("}}").strip()
                        ORTHIAVAL_UNTRIMED = ORTHIAVAL_TRIMED
                        ORTHIAVAL_TRIMED = ORTHIAVAL_TRIMED.split(".")

                    if(ORTHIASYSNS[ORTHIAVAL_TRIMED[0]] and ORTHIASYSV in ORTHIASYSLINE):
                        if(len(ORTHIAVAL_TRIMED) != 1):
                            ORTHIAFUNCTIONINSTANCE = OrthiaBuildInFunctions()
                            ORTHIASYSLINE = ORTHIASYSLINE.replace(ORTHIASYSV, ORTHIAFUNCTIONINSTANCE.ArrayAnalyzer(exec("{}".format(ORTHIAVAL_TRIMED[0], ORTHIAVAL_UNTRIMED))))

                        else:
                            if(type(ORTHIASYSNS[ORTHIAVAL_TRIMED[0]]) == "list" or type(ORTHIASYSNS[ORTHIAVAL_TRIMED[0]]) == "dict"):
                                ORTHIAVARDUMPMANAGEMENT = type(ORTHIASYSNS[ORTHIAVAL_TRIMED[0]])+"("+len(ORTHIASYSNS[ORTHIAVAL_TRIMED[0]])+")"
                                if(type(ORTHIASYSNS[ORTHIAVAL_TRIMED[0]]) == "list"):
                                    for(ORTHIASYSTEMLISTORDICTK, ORTHIASYSTEMLISTORDICTV in enumerate(ORTHIASYSNS[ORTHIAVAL_TRIMED[0]])):
                                        ORTHIAVARDUMPMANAGEMENT = ORTHIAVARDUMPMANAGEMENT+"<br>"+ORTHIASYSTEMLISTORDICTK+" => "+ORTHIASYSTEMLISTORDICTV
                                    ORTHIASYSLINE = ORTHIAVARDUMPMANAGEMENT
                                else:
                                    for (ORTHIASYSTEMLISTORDICTK, ORTHIASYSTEMLISTORDICTV in ORTHIASYSNS[ORTHIAVAL_TRIMED[0]].items()):
                                        ORTHIAVARDUMPMANAGEMENT = ORTHIAVARDUMPMANAGEMENT + "<br>" + ORTHIASYSTEMLISTORDICTK + " => " + ORTHIASYSTEMLISTORDICTV
                                    ORTHIASYSLINE = ORTHIAVARDUMPMANAGEMENT
                            else:
                                if(self.isHTMLSC):
                                    ORTHIASYSLINE = ORTHIASYSLINE.replace(ORTHIASYSV, ORTHIASYSNS[ORTHIAVAL_TRIMED[0]])
                                else:
                                    ORTHIASYSLINE = ORTHIASYSLINE.replace(ORTHIASYSV, ORTHIASYSNS[ORTHIAVAL_TRIMED[0]])
                    else:
                        ORTHIASYSLINE = ""
            self.__template = self.__template+str(ORTHIASYSLINE)+"\n"
        return True