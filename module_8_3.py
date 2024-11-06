class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers


    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) == False:
            raise IncorrectVinNumber("Неверный тип vin номера")
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber("Неверный диапозон для vin номера")
        return True


    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) == False:
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        return True



try:
 first = Car("Toyota", 1002289, "x740ex")
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{first.model} успешно создан")

try:
    second = Car("Honda", 279, "t032cp")
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{second.model} успешно создан")

try:
    third = Car("Mazda", 5015015, "нет номера")
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f"{third.model} успешно создан")