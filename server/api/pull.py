from core.base import BaseAPI


class PullBranch(BaseAPI):
    async def post(self, request):
        return self.success()