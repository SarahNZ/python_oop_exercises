# Given an instance of a Foo object, show two ways to print I am a Foo object 
# without hardcoding the word Foo.

class Foo:
    pass

foo = Foo()
print('I am a {foo.__class__.__name__} object')
print('I am a {type(foo).__name__} object')

