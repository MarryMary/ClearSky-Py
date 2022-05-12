from Core.Elena.TemplateEngines.Crystal.Core.Analyzer import Analyzer
class CrystalGate:

    # CallAnalyzer is full parsing template.
    def CallAnalyzer(self, template: str, params: dict, mode: str):
        if(mode == "pythonista"):
            mode = "pythonista"
        elif(mode == "phper"):
            mode = "phper"
        else:
            mode = "phper"
        analyzer_instance = Analyzer()
        return analyzer_instance.Main(template, params, False, mode)

    # OnlyFunctionEval is parsing only function in template.
    def OnlyFunctionEval(self, template: str, params: dict):
        analyzer_instance = Analyzer()
        return analyzer_instance.Main(template)

    # OnlyParamsEval is parsing only params in template
    def OnlyParamsEval(self, template: str, params: dict):
        analyzer_instance = Analyzer()
        return analyzer_instance.Main(template, params, True)