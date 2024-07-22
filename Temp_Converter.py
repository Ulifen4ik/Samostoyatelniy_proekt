class Converter:
    @staticmethod
    def Celsius_to_Farenheit(Celsius):
        return (Celsius * 9 / 5) + 32
    @staticmethod
    def Farenheit_to_Celsius(Farenheit):
        return (Farenheit - 32) * 5/9


if __name__ == "__main__":
    print(Converter.Celsius_to_Farenheit(-40))
    print(Converter.Farenheit_to_Celsius(-40))
    