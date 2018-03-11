import Pyro4

@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {0} YOU ARE LIT".format(name)

daemon = Pyro4.Daemon()
uri = daemon.register(GreetingMaker)

print("Ready. Object uri =", uri)
daemon.requestLoop()
