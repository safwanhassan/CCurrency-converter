 from forex_python.converter import CurrencyRates

c = CurrencyRates()

from_currency = input("أدخل رمز العملة المراد التحويل منها (مثال: USD): ").upper()
to_currency = input("أدخل رمز العملة المراد التحويل إليها (مثال: EUR): ").upper()
amount = float(input("أدخل المبلغ: "))


converted_amount = c.convert(from_currency, to_currency, amount)
print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
