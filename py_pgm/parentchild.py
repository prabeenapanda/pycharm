
class Parent(object):
    def public(self):
        print("good")
    def _protected(self):
        print("hi")
    def __private(self):
        print("hello")

class Child(Parent):
    def pub(self):
        self.public()
    def foo(self):
        self._protected()
    def bar(self):
        self.__private()

c = Child()
c.pub()
c.foo()
c.bar()
