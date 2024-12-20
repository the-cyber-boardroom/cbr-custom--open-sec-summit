from osbot_fast_api.api.Fast_API                                     import Fast_API
from cbr_custom_open_sec_summit.fast_api.routes.Routes__Info         import Routes__Info
from cbr_custom_open_sec_summit.markitdown.routes.Routes__Markitdown import Routes__Markitdown


class Open_Sec_Summit__Fast_API(Fast_API):
    base_path  : str  = '/'
    enable_cors: bool = True

    def setup_routes(self):
        self.add_routes(Routes__Info)
        self.add_routes(Routes__Markitdown)

