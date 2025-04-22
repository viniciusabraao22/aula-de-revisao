peso= float(input("digite seu peso: "))
altura= float(input("digite sua altura: "))

imc=peso/altura**2

if imc < 18.6:
    print("Abaixo do peso")

elif imc >= 18.6 and imc <= 24.9:
    print("Peso ideal (parabéns!!)")

elif imc >= 25.0 and imc <= 29.9:
    print("Levemente acima do peso")

elif imc >= 30.0 and imc <= 34.9:
    print("Obesidade grau 1")

elif imc >= 35.0 and imc <= 39.9:
    print("Obesidade grau 2 (severa)")

else:
    print(f"{imc} - Obesidade grau 3 (mórbida)")
