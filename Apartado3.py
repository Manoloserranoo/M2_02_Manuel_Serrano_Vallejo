username=input("Introduzca su nombre de usuario:")
password=input("Introduzca su contraseña:")

if username:
  A = 3 <= len(username) < 10
else:
  A = False
if password:
  B = password == "Tokio" or password == "Python"
else:
  B = False
print(f"{A}")
print(f"{B}")