class Multiplication():
    def __init__(self, number):
        self.number = number

    def get_multiply_numbers_from_1to10(self):
        i = 1
        while(i <= 10):
            result = i*self.number
            print("{}*{}: {}".format(self.number, i,  result))
            i += 1
try:
#     number = int(input("Enter a number here to see table: "))
    mul = Multiplication(8)
    mul.get_multiply_numbers_from_1to10()
except EOFError as e:
    print(end="")
