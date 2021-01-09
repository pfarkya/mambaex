from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from socketserver import ThreadingMixIn
from .helper.callername import callername
from .handlerClass import HandlerMambaServer, ThreadedServerWithAppStack
from threading import Thread
import re

class MambaexApp ():
    """
    A class for handling server instance
    """

    def __init__(self, name):
        caller = callername(1)
        if caller != 'mambaex.mambaexApps.MambaexApps.getOrCreateApp':
            raise Exception("Can't be create an object directly accessing this class")
        self.name = name
        self.appstack = []
    def __convertpathtoregexpath(self, path, isUse=False):
        result = re.sub(r"(:.+?)\/", "?P<\\1>(.*?)/", path, 0)
        lastI = result.rfind("/")
        length = len(result)
        if lastI < length -1 and result[lastI + 1] == ":":
            name = result[(lastI + 1):]
            replacer = "?P<" + name + ">(.*?)"
            result = result.replace(":" + name, replacer)
        if isUse != True:
            result = "^" + result + "$"
        return re.compile(result)


    def get(self, path, callback):
        """
        Add the callback function defination to the stack of the GET method of given path

        :param string path: A path string/regex string to match
        :param function callback: A function to callback
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        self.appstack.append({'callback':callback, 'method': 'GET', 'path': path, 'regexpath': self.__convertpathtoregexpath(path)})
        return self
    def use(self, path, callback):
        """
        Add the callback function defination to the stack of the ALL method of given path

        :param string path: A path string/regex string to match
        :param function callback: A function to callback
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        # Check for static add
        self.appstack.append({'callback':callback, 'method': '*', 'path': path , 'regexpath': self.__convertpathtoregexpath(path, True)})
        return self
    def post(self, path, callback):
        """
        Add the callback function defination to the stack of the POST method of given path

        :param string path: A path string/regex string to match
        :param function callback: A function to callback
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        self.appstack.append({'callback':callback, 'method': 'POST', 'path': path, 'regexpath': self.__convertpathtoregexpath(path)})
        return self
    def put(self, path, callback):
        """
        Add the callback function defination to the stack of the PUT method of given path
        :param string path: A path string/regex string to match
        :param function callback: A function to callback
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        self.appstack.append({'callback':callback, 'method': 'PUT', 'path': path, 'regexpath': self.__convertpathtoregexpath(path)})
        return self
    def patch(self, path, callback):
        """
        Add the callback function defination to the stack of the PATCH method of given path

        :param string path: A path string/regex string to match
        :param function callback: A function to callback
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        self.appstack.append({'callback':callback, 'method': 'PATCH', 'path': path, 'regexpath': self.__convertpathtoregexpath(path)})
        return self
    def delete(self, path, callback):
        """
        Add the callback function defination to the stack of the DELETE method of given path

        :param string path: A path string/regex string to match
        :param function callback: A function to callback
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        self.appstack.append({'callback':callback, 'method': 'DELETE', 'path': path, 'regexpath': self.__convertpathtoregexpath(path)})
        return self
    def listen(self, port):
        """
        Start listening to port

        :param int port: A port at which it starts listening
        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        print("Listening on port " + str(port))
        self.server = ThreadedServerWithAppStack(self.appstack,('', port), HandlerMambaServer)
        self._server_thread = Thread(target=self.server.serve_forever)
        self._server_thread.daemon = True
        self._server_thread.start()
        return self
    def stop(self):
        """
        Use to stop listening

        :return: app itself for chaining avability
        :rtype: MambaexApp_
        """
        if self._server_thread is not None:
            self._server_thread.stop()
        else:
            raise Exception("Server not configured")
        return self
