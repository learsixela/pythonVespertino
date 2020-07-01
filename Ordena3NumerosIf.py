x = int(input('Escriba el primer número: '))
y = int(input('Escriba el segundo número: '))
z = int(input('Escriba el tercer número: '))

if x>y and y>z:
    print(f"el orden es {x} {y} {z} x y z")
elif x>z and z>y:
    print(f"el orden es {x} {z} {y} x z y")
elif y>x and x>z:
    print(f"el orden es {y} {x} {z} y x z")
elif y>z and z>x:
    print(f"el orden es {y} {z} {x} y z x")
elif z>x and x>y:
    print(f"el orden es {z} {x} {y} z x y")
elif z>y and y>x:
    print(f"el orden es {z} {y} {x} z y x")