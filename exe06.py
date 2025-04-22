peso= float(input("digite seu peso: "))
altura= float(input("digite sua altura: "))

imc=peso/altura**2

if imc < 18.6:
    print("abaixo do peso")

elif imc >= 18.6 and imc <= 24.9:
    print("peso ideal (parabens!!}")

elif imc >= 25.0 and imc <= 29.0:
    print("levemente acima do peso ")
elif imc >= 30.0 and imc <= 34.9:
    print("obesidade grau 1")
elif imc >= 35.0 and imc <= 39.9:
    print("obesidade grau 2 (severa)")

else:
    print(f"{imc}obesidade grau 3 (quase morto)")