from sanic import Blueprint

from .pull import PullBranch
from .restart import RestartService
from .check_status import CheckServiceStatus

api = Blueprint('api')

api_bp = Blueprint('api', url_prefix='/api')

api_bp.add_route(RestartService.as_view(), '/restart')
api_bp.add_route(PullBranch.as_view(), '/pull')
api_bp.add_route(CheckServiceStatus.as_view(), '/check_status')

