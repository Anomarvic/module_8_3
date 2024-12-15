class IncorrectVinNumber(Exception):
    def __init__(self, input_text):
        self.message = input_text

class IncorrectCarNumbers(Exception):
    def __init__(self, input_text):
        self.message = input_text


class Car:
    def __init__(self, input_model, input_vin, input_numbers):
        self.model = input_model
        if self.__is_valid_vin(input_vin):
            self.__vin = input_vin
        if self.__is_valid_car_number(input_numbers):
            self.__numbers = input_numbers

    def __is_valid_vin(self, input_vin_number):
        if not isinstance(input_vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if isinstance(input_vin_number, int) and not (1000000 <= input_vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_car_number(self, input_car_number):
        if not isinstance(input_car_number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if isinstance(input_car_number, str) and len(input_car_number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

try:  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

    
