import re
from Core.Elena.Executer.Provide import Provide

def http404(env, start_response):
    return Provide.echo(start_response, Provide.Viewer("NotFound", True), 404)


def http405(env, start_response):
    return Provide.echo(start_response, Provide.Viewer("NotAllowed", True), 405)

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
        error_callback = http404
        for r in cls.routes:
            matched = r['route_compiled'].match(route)
            print(matched)

            if not matched:
                continue

            error_callback = http405
            url_vars = matched.groupdict()
            if method == r['method']:
                return r['callback'], url_vars
            elif r['method'] == '*':
                return r['callback'], url_vars
        return error_callback, {}

    @classmethod
    def __call__(cls, env, start_response):
        method = env['REQUEST_METHOD'].upper()
        route = env['PATH_INFO'] or '/'
        callback, kwargs = cls.match(method, route)
        return callback(env, start_response, **kwargs)