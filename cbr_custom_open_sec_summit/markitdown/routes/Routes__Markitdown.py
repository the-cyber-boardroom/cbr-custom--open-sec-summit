from fastapi                                                    import UploadFile, File
from osbot_fast_api.api.Fast_API_Routes                         import Fast_API_Routes
from starlette.responses import PlainTextResponse

from cbr_custom_open_sec_summit.markitdown.Markitdown_Service   import Markitdown_Service

ROUTES_PATHS__MARKITDOWN = ['/markitdown/markitdown-pdf',  '/markitdown/markitdown-xslx', '/markitdown/markitdown-upload']

class Routes__Markitdown(Fast_API_Routes):
    tag     : str = 'markitdown'
    service : Markitdown_Service

    def markitdown_upload(self, file: UploadFile = File(...)) -> str:

        markdown = self.service.process_file(file)
        return PlainTextResponse(markdown)

    def markitdown_pdf(self) -> str:
        """Process a sample PDF file."""
        file_path = 'markitdown/sample_files/sample.pdf'
        markdown  = self.service.process_local_file(file_path)
        return PlainTextResponse(markdown)

    def markitdown_xslx(self) -> str:
        file_path = 'markitdown/sample_files/test.xlsx'
        markdown = self.service.process_local_file(file_path)
        return markdown

    def setup_routes(self):
        self.add_route_get (self.markitdown_xslx)
        self.add_route_get (self.markitdown_pdf)
        self.add_route_post(self.markitdown_upload)