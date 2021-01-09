class Response:
    """Response object will carry information and methods with response to the request

    :ivar: body
    :ivar: headers
    """
    def __init__(self,handler):
        self.wfile = handler.wfile
        self.send_response = handler.send_response
        self.send_header = handler.send_header
        self.send_response = handler.send_response
        self.end_headers = handler.end_headers
        self.headers = {}
    def status(self, code):
        """Setting status to response to send
        :params: code - intiger
        :returns: response
        """
        self.status_code = code
        return self
    def send(self, data=None):
        """send the data to client
        :params: data - buffer
        :returns: response
        """
        self.send_response(self.status_code)
        self.end_headers()
        if data is not None:
            self.wfile.write(data)
    def header(self, key, value=None):
        """Setting the header to be send
        """
        pass
