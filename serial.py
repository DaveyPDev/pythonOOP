"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__ (self, start = 0):
        """creating counter from start"""
        self.start = self.next = start

    def __repr__ (self):
        """ return iteration """
        return f" Serial Generator start = {self.start} next = {self.next} "

    def generate(self):
        """ return next serial number """
        self.next += 1
        return self.next - 1

    def reset(self):
        """ restarts counter """
        self.next = self.start
