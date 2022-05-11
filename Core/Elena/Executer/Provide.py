import json
from Web.Programs.Controllers import *
class Provide:
    @staticmethod
    def Viewer(path: str, IsIrregular: bool = False):
        if(IsIrregular):
            clsk_docroot = "Web/Templates/IrregularCase/" + path.strip() + ".html"
        else:
            clsk_docroot = "Web/Templates/Normal/" + path.strip() + ".html"
        template = ""
        with open(clsk_docroot, "r", encoding="utf-8") as file:
            template = file.read()
        return template

    @staticmethod
    def Reader():
        pass

    @staticmethod
    def echo(start_response, string: str, status: int = 200, header: list = [('Content-type', 'text/html; charset=utf-8')]):
        Me = Executer()
        status_code = Me.StatusCodeJudgement(status)
        start_response(status_code, header)
        return [string.encode()]

    @staticmethod
    def Controller(controller_name: str, function_name: str):
        pass

    @staticmethod
    def WebAPI(start_response, data: dict, status: int = 200):
        pass

    @staticmethod
    def JumpTo(to: str = "/"):
        pass

    def StatusCodeJudgement(self, status: int):
        with open("Core/Elena/Executer/HTMLStatusCode.json", "r", encoding="utf-8") as f:
            codes = json.load(f)
        for match_code, status_str in codes.items():
            if(str(status).strip() == match_code):
                return str(status_str)
        return "200 OK"