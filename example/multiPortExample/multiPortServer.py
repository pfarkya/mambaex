from mambaex import MambaexApps

server1 = MambaexApps.getOrCreateApp('Server1')
server2 = MambaexApps.getOrCreateApp('Server2')

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

def get_admins(req, res, next):
    print("sending users")
    res.status(200).send('{"ss":""}'.encode('UTF-8'))


server1.use("/", auth_middleware)
server1.use("/users", user_middleware)
server1.get("/users", get_users)
server1.listen(8080)

server2.use("/", auth_middleware)
server2.use("/admins", user_middleware)
server2.get("/admins", get_admins)
server2.listen(8081)


try:
    while True:
        pass
except KeyboardInterrupt:
    pass
