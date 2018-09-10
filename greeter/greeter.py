class Greeter:

    def __init__(self, message):
        self.message = message

    def greet(self):
        return 'Hello, {}'.format(self.message)
