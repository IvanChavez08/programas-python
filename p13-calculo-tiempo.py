#Dada una cantidad de horas, calcula el equivalente en días, minutos y segundos


horas = float(input("Introduce la cantidad de horas: "))


días = horas // 24


horas_restantes = horas % 24


minutos = horas_restantes * 60


segundos = minutos * 60


print(f"{horas} horas equivalen a:")
print(f"{días} días")
print(f"{int(minutos)} minutos")
print(f"{int(segundos)} segundos")
