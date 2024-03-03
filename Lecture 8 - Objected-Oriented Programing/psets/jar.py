class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        self.size += n
        return self.size

    def withdraw(self, n):
        self.size -= n
        return self.size


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("capacity must be at least 1")
        self._capacity = capacity


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Overload of capacity")
        elif size < 0:
            raise ValueError("There aren't enough cookies")
        self._size = size

    # Funtion to sum different instaciated jar objects
    def __add__(self, other):
        # I Coul've done some condition to enlarge the capacity if it overloads, but I decided to keep it simple
        size = self.size + other.size
        other_jar = Jar()
        other_jar.deposit(size)
        return other_jar


def main():
    jar = Jar()
    jar.deposit(5)
    print(jar)
    jar.deposit(5)
    print(jar)
    # jar.deposit(8)
    # print(jar)
    jar.withdraw(9)
    print(jar)
    # jar.withdraw(2)
    # print(jar)

if __name__ == '__main__':
    main()
