import re
from Core.Elena.Executer.Provide import Provide
from Core.Elena.Router.GateWay import GateWay

def http404(env, start_response):
    return Provide.echo(start_response, Provide.Viewer("NotFound", True), 404)


def http405(env, start_response):
    return Provide.echo(start_response, Provide.Viewer("NotAllowed", True), 405)

def DebuggingFunction(env, start_response, message: str = "URI Pattern was not matched."):
    return Provide.echo(start_response, message, 200)

class StarNavigator:
    routes = []

    @classmethod
    def Get(cls, route: str, function):
        cls.routes.append({
            'method': 'GET',
            'route': route,
            'route_compiled': re.compile(route),
            'function': function
        })

    @classmethod
    def Post(cls, route: str, function):
        cls.routes.append({
            'method': 'POST',
            'route': route,
            'route_compiled': re.compile(route),
            'function': function
        })

    @classmethod
    def Put(cls, route: str, function):
        cls.routes.append({
            'method': 'PUT',
            'route': route,
            'route_compiled': re.compile(route),
            'function': function
        })

    @classmethod
    def Patch(cls, route: str, function):
        cls.routes.append({
            'method': 'PATCH',
            'route': route,
            'route_compiled': re.compile(route),
            'function': function
        })

    @classmethod
    def Delete(cls, route: str, function):
        cls.routes.append({
            'method': 'DELETE',
            'route': route,
            'route_compiled': re.compile(route),
            'function': function
        })

    @classmethod
    def All(cls, route: str, function):
        cls.routes.append({
            'method': '*',
            'route': route,
            'route_compiled': re.compile(route),
            'function': function
        })

    @classmethod
    def match(cls, method, route):
        callback = DebuggingFunction
        for r in cls.routes:
            if GateWay.RoutingJudgement(r['route'], route):
                callback = http405
                if method == r['method']:
                    callback = r['callback']
                elif r['method'] == '*':
                    callback = r['callback']
            else:
                callback = http404
        return callback

    @classmethod
    def __call__(cls, env, start_response):
        method = env['REQUEST_METHOD'].upper()
        route = env['PATH_INFO'] or '/'
        import Web.Settings.RoutingSettings
        callback = cls.match(method, route)
        return callback(env, start_response)