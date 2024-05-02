class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        total = "🍪" * self.size
        return total

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError

        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        try:
            self._capacity = int(capacity)
            if self.capacity < 0:
                raise ValueError
        except ValueError:
            raise ValueError

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError
        self._size = size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(1)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)

if __name__ == "__main__":
    main()