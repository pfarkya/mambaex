import re
from .response import Response

class Request:
    """Request object carries the information about request comes to the server handler

    :ivar: body
    :ivar: params
    :ivar: query
    :ivar: headers
    :ivar: path
    """
    nobodymethods = ["GET", "HEAD", "DELETE"] # Head not supported for now
    bodymethods = ["POST", "PUT","PATCH"]
    def __init__(self,handler):
        self.handler = handler
        self.headers = self.handler.headers
        self.rfile = self.handler.rfile
        self.res = Response(self.handler)
        self.extract_path_and_query(self.handler)
        self._exactmatch = False
        self.get_calling_stack(self.handler)
        if handler.command in self.nobodymethods:
            """No need of Parsing check if anything is there"""
            pass
        elif handler.command in self.bodymethods:
            """Need of Parsing check if anything is there"""
            if 'Content-Length' in self.headers:
                content_len = int(self.headers.get('Content-Length'))
                if content_len > 0:
                    post_body = self.rfile.read(content_len)
                    if header_content_type == HttpConstants.CONTENT_TYPE_JSON:
                        body_params = json.loads(post_body.decode("utf-8"))
                    elif header_content_type == HttpConstants.CONTENT_TYPE_WWW_FORM:
                        body_params = {}
                        arr = post_body.decode("utf-8").split("&")
                        for param in arr:
                            param_arr = param.split("=", 1)
                            key = param_arr[0]
                            value = param_arr[1]
                            body_params[key] = value
                    else:
                        raise Exception(
                            "Content-Type must be " + HttpConstants.CONTENT_TYPE_JSON
                            + " or " + HttpConstants.CONTENT_TYPE_WWW_FORM
                        )
        if self._exactmatch != True:
            self.res.status(404).send()
        else:
            self.currentcallback = 0
            self.nextcallback = 0
            self.length_of_callbacks = len(self.calling_stack)
            self.next()
    def get_calling_stack(self, handler):
        """
        get the calling stack to be called if any matching routes are avaialble
        """
        self.calling_stack = []
        for eachstack in handler.server.appstack:
            print(eachstack)
            if eachstack["method"] == "*":
                # non exact match crete path param
                match = eachstack["regexpath"].match(self.path)
                if  match != None:
                    self.calling_stack.append(eachstack["callback"])
            elif  eachstack["method"] == handler.command:
                # exact match create & overrride path peram if non exact match before
                match = eachstack["regexpath"].match(self.path)
                if  match != None:
                    self._exactmatch = True
                    self.pathparams = match.groups()
                    self.calling_stack.append(eachstack["callback"])
        return self.calling_stack
    def extract_path_and_query(self, handler):
        path_query = handler.path.split('?')
        self.path = path_query[0]
        if len(path_query) > 1:
            self.querystring = path_query[1]
        else:
            self.querystring = None
        self.query_params = {}
        if self.querystring is not None:
            query_array = self.querystring.split('&')
            for query_elem in query_array:
                q = query_elem.split('=')
                if len(q) == 2:
                    self.query_params[q[0]] = q[1]
    def next(self):
        """
        Logic to make pass itself in method call
        """
        self.currentcallback = self.nextcallback
        self.nextcallback = self.nextcallback + 1
        if self.currentcallback < self.length_of_callbacks:
            self.calling_stack[self.currentcallback](self,self.res,self.next)
