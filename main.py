import copy

class Protoype:
    def __init__(self):
        self._objects = {}
    
    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]
    
    def clone(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)

        return obj

class Car:
    def __init__(self, name, color, options):
        self.name = name
        self.color = color
        self.options = options
    
    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)


c = Car('Mazda 3', 'Red', 'MX')
prototype = Protoype()
prototype.register_object('c', c)

cloned = prototype.clone('c')
cloned.color = 'Blue'

print(cloned, 'vs', c)