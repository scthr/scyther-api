from functools import wraps
from typing import List, Union

from django.http import HttpResponse


def restrict_methods(methods: Union[List[str], str]):
    """
    Restricts a route to only allow certain HTTP methods.

    :examples:

    To allow only ``POST`` requests:

    >>> @restrict_methods("POST")
    >>> def some_route(request):
    >>>     pass

    To allow ``POST`` and ``GET``:

    >>> @restrict_methods(["POST", "GET"])
    >>> def some_route(request):
    >>>     pass

    """
    if isinstance(methods, str):
        methods = [methods]

    def _route_restrictor(route):
        @wraps(route)
        def _restricted_route(request):
            if request.method not in methods:
                return HttpResponse(status_code=405)
            return route(request)

        return _restricted_route

    return _route_restrictor
