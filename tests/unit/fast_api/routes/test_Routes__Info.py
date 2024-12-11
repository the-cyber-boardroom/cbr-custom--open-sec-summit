from unittest                                           import TestCase
from cbr_custom_open_sec_summit.fast_api.routes.Routes__Info import Routes__Info
from cbr_custom_open_sec_summit.utils.Version                import version__cbr_custom_open_sec_summit


class test_Routes__Info(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.routes_info = Routes__Info()

    def test_version(self):
        assert self.routes_info.version() == {'version': version__cbr_custom_open_sec_summit}

    def test_setup_routes(self):
        with self.routes_info as _:
            assert _.routes_paths() == []
            _.setup_routes()
            assert _.routes_paths() == ['/ping', '/version' ]