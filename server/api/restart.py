from core.base import BaseAPI


class RestartService(BaseAPI):
    async def post(self, request):
        return self.success()
