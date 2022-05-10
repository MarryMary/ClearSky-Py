import re
def http404(env, start_response):
    start_response('404 Not Found', [('Content-type', 'text/plain; charset=utf-8')])
    return [b'404 Not Found']


def http405(env, start_response):
    start_response('405 Method Not Allowed', [('Content-type', 'text/plain; charset=utf-8')])
    return [b'405 Method Not Allowed']

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
            if not matched:
                continue

            error_callback = http405
            url_vars = matched.groupdict()
            if method == r['method']:
                return r['callback'], url_vars
        return error_callback, {}