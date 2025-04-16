class Calculation:
    def __init__(self, calculationLine = ""):
        self.calculationLine = calculationLine

    def SetCalculationLine(self, modified_string):
        self.calculationLine = modified_string

    def SetLastSymbolCalculationLine(self, symbol):
        self.calculationLine += symbol

    def GetCalculationLine(self):
        return f"{self.calculationLine} - текущее значение свойства"

    def GetLastSymbol(self):
        print(f"{self.calculationLine[-1]} - последний символ")

    def DeleteLastSymbol(self):
        print(f"{self.calculationLine[:-1]} - без последнего удаленного символа")

calculation = Calculation()
calculation.SetCalculationLine("343 - 123 -*")
print(calculation.GetCalculationLine())
calculation.SetLastSymbolCalculationLine("=")
print(calculation.GetCalculationLine())
calculation.GetLastSymbol()
calculation.DeleteLastSymbol()
