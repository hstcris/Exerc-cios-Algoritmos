
angulo_graus = float(input("Digite o ângulo em graus: "))


angulo_radianos = angulo_graus * (3.14159265359 / 180.0)


seno = round(math.sin(angulo_radianos), 4)
cosseno = round(math.cos(angulo_radianos), 4)
tangente = round(math.tan(angulo_radianos), 4)


secante = round(1 / cosseno, 4)
cosecante = round(1 / seno, 4)
cotangente = round(1 / tangente, 4)


print(f"Seno do ângulo: {seno}")
print(f"Cosseno do ângulo: {cosseno}")
print(f"Tangente do ângulo: {tangente}")
print(f"Secante do ângulo: {secante}")
print(f"Cosecante do ângulo: {cosecante}")
print(f"Cotangente do ângulo: {cotangente}")
