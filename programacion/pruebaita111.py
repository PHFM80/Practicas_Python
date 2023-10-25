a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)
for numero, texto in zip(a, b):
 print("Número", numero, "Letra", texto)