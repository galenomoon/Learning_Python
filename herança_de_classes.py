class Person:
    def __init__(self):
        self.cpf = None
        self.name = None
        self.address = None


class Clerk(Person):
    def __init__(self):
        self.registration = None
        self.name = None
        self.salary = None

    def login_as_admin(self):
        # code
        pass

class Client(Person):
    def __init__(self):
        self.id = None
        self.registerDate = None

    def login_as_client(self):
        # code
        pass

clerk_1 = Clerk()
clerk_1.name = "Guilherme Galeno"
print(clerk_1.name) #herança

client_1 = Client()
client_1.cpf = "529.304.768-00"
print(client_1.cpf) #herança