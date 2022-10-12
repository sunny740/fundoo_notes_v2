import logging
from user import urls
import user
from user.models import UserLog

logging.basicConfig(filename="view.log", level=logging.INFO, filemode="w", force=True)

class UserMiddleware:
    """
    create a new middleware class
    """
    def __init__(self, get_response):
        # One-time configuration and initialization.

        self.get_response = get_response
        

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        self.updtelogtable(request)
        response = self.get_response(request)
        return response       
        

    # middleware hook
    def updtelogtable(self, request):
        user_data = UserLog.objects.filter(method=request.method, url=request.get_full_path())
        if not user_data.exists():
            UserLog.objects.create(method=request.method, url=request.get_full_path())
        else:
            data = user_data.first()
            data.count += 1
            data.save()

