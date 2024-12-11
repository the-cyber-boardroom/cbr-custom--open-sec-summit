from osbot_fast_api.api.Fast_API_Routes  import Fast_API_Routes
from cbr_custom_open_sec_summit.utils.Version import version__cbr_custom_open_sec_summit

ROUTES_PATHS__INFO = ['/info/version',  '/info/ping']

class Routes__Info(Fast_API_Routes):
    tag :str = 'info'

    def ping(self):
        return 'pong'
    
    def version(self):
        return {'version': version__cbr_custom_open_sec_summit}

    
    def setup_routes(self):
        self.add_route_get(self.ping)
        self.add_route_get(self.version)

