from wsgiref.simple_server import make_server
from Core.Elena.Router.StarNavigator import StarNavigator

class index:
    @staticmethod
    def SystemStartTrigger(port: int = 8000):
        System = StarNavigator()
        httpd = make_server('', port, System)
        print("StartUp ClearSky Server Listen->Port:"+str(port)+" DocumentRoot:Exposure/")
        httpd.serve_forever()