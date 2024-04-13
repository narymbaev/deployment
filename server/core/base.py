import traceback
import ujson
from sanic import response
from sanic.request import Request
from sanic.views import HTTPMethodView

from core import errors, outputs
from modules import timber
from settings import settings
from utils.object import encoder
from utils.result import Result


class BaseAPI(HTTPMethodView):
    decorators = []

    @classmethod
    def is_http_response(cls, value):
        return isinstance(value, response.HTTPResponse)

    @classmethod
    async def options(cls, *args, **kwargs):
        return response.text('')

    def adapt(self, result):
        if result:
            if isinstance(result, Result.Success):
                if result.data:
                    return self.success(data=result.data)
                else:
                    return self.success()
            elif isinstance(result, Result.Error):
                return self.error(result.error)
        return self.error()

    @classmethod
    def success(cls, output=None, format_type='json', show_static_host_name=True, **kwargs):
        static_host_name = settings.get('static_host_name', settings.get('hostname', ''))
        kwargs['_success'] = True
        if show_static_host_name:
            kwargs['static_host_name'] = static_host_name

        if output:
            if isinstance(output, str):
                if hasattr(outputs, output):
                    output = getattr(outputs, output)()

            if isinstance(output, outputs.Output):
                kwargs.update({'message': output.message})

        return response.json(kwargs, status=200, dumps=encoder.encode) if format_type == 'json' else kwargs

    @classmethod
    def fail(cls, **kwargs):
        kwargs['_success'] = False
        return response.json(kwargs, dumps=encoder.encode, status=200)

    @classmethod
    def error(cls, error=None, status=200, format_type='json', **kwargs):
        static_host_name = settings.get('static_host_name', settings.get('hostname', ''))
        data = {'_success': False, 'static_host_name': static_host_name}

        if kwargs.get('data'):
            data['data'] = kwargs.pop('data')

        if error:
            if isinstance(error, str):
                if hasattr(errors, error):
                    error = getattr(errors, error)(**kwargs)

        if not error or not isinstance(error, errors.Error):
            error = errors.Unknown(**kwargs)

        data['error'] = error

        return response.json(data, status=status, dumps=encoder.encode) if format_type == 'json' else data

    @classmethod
    def raw(cls, body, status=200, headers=None, content_type='application/octet-stream'):
        return response.raw(body, status, headers, content_type)

    @staticmethod
    def as_list(request: Request, parameter: str, distinct=False) -> list:
        if request.args:
            value = request.args.get(parameter, None)
        elif request.json:
            value = request.json.get(parameter, None)
        else:
            value = None
        if value is None:
            return []
        output_list = ujson.loads(value)
        if distinct and isinstance(output_list, list):
            try:
                output_list = list(set(output_list))
            except Exception as e:
                traceback.print_exc()
                timber.w(f'BaseAPI#as_list() -> '
                         f'[Unable to parse list] request: {request}, parameter: {parameter}, e: {e}')
        return output_list
