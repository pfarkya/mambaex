from mambaex import MambaexApps

server = MambaexApps.getOrCreateApp('Server1')

def auth_middleware(req, res, next):
    print("we are in auth middle ware")
    if req.headers["Authorization"] != None:
        next()
    else:
        res.status(401).send()

def user_middleware(req, res, next):
    print("we are in user middleware")
    next()

def get_users(req, res, next):
    print("sending users")
    res.status(200).send('{"ss":""}'.encode('UTF-8'))


server.use("/", auth_middleware)
server.use("/users", user_middleware)
server.get("/users", get_users)
server.listen(8080)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
