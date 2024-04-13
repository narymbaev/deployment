import locale

from sanic import Sanic, response

from modules import db


class App(Sanic):

    def __init__(self):
        super().__init__(name='qbox-deployment')

    def set_config(self, **kwargs):
        for attr, value in kwargs.items():
            self.config.__setattr__(attr, value)


app = App()

app.blueprint([
    api_bp
])


@app.route('/', methods=['GET', 'HEAD'], name='root_index')
# @D.render_to_template('index.html')
async def index(request):
    return response.html('<html>Welcome</html>', status=200)


@app.before_server_start
async def before_server_start(_app, _loop):
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
    await db.initialize(_loop)
    # mongo.initialize(_loop)
    # await cache.initialize(_loop)


@app.before_server_stop
async def before_server_stop(_app, _loop):
    app.purge_tasks()
