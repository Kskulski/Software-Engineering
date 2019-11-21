class Math:
    def is_prime(self, num):
        if num < 0:
            raise(ValueError)

        if num <= 1:
            return True

        for divisor in range(2, num):
            if num % divisor == 0:
                return False

        return True

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        return a/b

    def multiply(self, a, b):
        return a * b

    def sub_and_print(self, a, b):
        print('result is : {}'.format(a-b))
