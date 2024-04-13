from core.base import BaseAPI


class CheckServiceStatus(BaseAPI):
    async def get(self, request):
        return self.success()