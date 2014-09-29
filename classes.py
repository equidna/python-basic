#! c:/Python33/python.exe

class Bird:
    def __init__(self, kind, call):
        self.kind = kind
        self.call = call
    
    def do_call(self):
        print("a %s goes %s" % (self.kind, self.call))

class Parrot(Bird):
    def __init__(self):
        Bird.__init__(self, "Parrot", "Kah!")

class Cuckoo(Bird):
    def __init__(self):
        Bird.__init__(self, "Cuckoo", "Cuckoo!")


if __name__ == "__main__":
    parrot = Parrot()
    cuckoo = Cuckoo()
    
    parrot.do_call()
    
    cuckoo.do_call()