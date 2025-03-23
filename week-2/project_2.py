import math

def solve_cubic(a, b, c, d):
  '''Find the roots of a cubic function'''
  b /= a
  c /= a
  d /= a

  p = (3 * c - b ** 2) / 3
  q = (2*b**3 - 9*b*c + 27*d) / 27
  delta = (q**2 / 4) + (p**3 / 27)

  if delta > 0:
    u = (-q/2 + math.sqrt(delta))**(1/3)
    v = (-q/2 - math.sqrt(delta))**(1/3)
    y1 = u + v
  else:
    r = math.sqrt(-p**3 / 27)
    theta = math.acos(-q / (2*r))
    y1 = 2 * (-p / 3)**0.5 * math.cos(theta / 3)

  x1 = y1 - b / 3
  return x1


def solve_quadratic(a, b, c):
  '''Find the roots of a quadratic function'''
  d = (b ** 2) - 4 * a * c
  if d < 0:
    print("Equation has no real roots")
    return
  sqrt_d = math.sqrt(d)
  root1 = (-b + sqrt_d) / (2 * a)
  root2 = (-b - sqrt_d) / (2 * a)
  return root1, root2



def solve_quartic(a, b, c, d, e):
  '''Find the roots of a quartic function'''
  b /= a
  c /= a
  d /= a
  e /= a

  p = c - (3 * b**2) / 8
  q = d - (b * c) / 2 + (b**3) / 8
  r = e - (b * d) / 4 + (b**2 * c) / 16 - (3 * b**4) / 256

  # Solve the resolvent cubic: y^3 + 2py^2 + (p^2 - 4r)y - q^2 = 0
  y = solve_cubic(1, 2*p, p**2 - 4*r, -q**2)

  R = math.sqrt(p + 2*y)
  D1 = math.sqrt(y**2 - 4*r)
  D2 = math.sqrt(2*y - p - (2*q / R))

  x1 = (-R + D1) / 2
  x2 = (-R - D1) / 2
  x3 = (R + D2) / 2
  x4 = (R - D2) / 2

  shift = b / 4
  return x1 - shift, x2 - shift, x3 - shift, x4 - shift


option = int(input('''
1. Cubic Equation
2. Quartic Equation
3. Quadratic Equation
'''))

if option == 1:
  print("Find the roots of cubic equation in the form ax^3 + bx^2 + cx + d = 0")
  a = float(input("Enter a: "))
  b = float(input("Enter b: "))
  c = float(input("Enter c: "))
  d = float(input("Enter d: "))
  roots = solve_cubic(a, b, c, d)
  print(f"The roots of the equation {a}x^3 + {b}x^2 + {c}x + {d} = 0 are", roots)
elif option == 2:
  print("Find the roots of cubic equation in the form ax^4 + bx^3 + cx^2 + dx + e = 0")
  a = float(input("Enter a: "))
  b = float(input("Enter b: "))
  c = float(input("Enter c: "))
  d = float(input("Enter d: "))
  e = float(input("Enter e: "))
  roots = solve_quartic(a, b, c, d, e)
  print(f"The roots of the equation {a}x^4 + {b}x^3 + {c}x^2 + {d}x + {e} = 0 are", roots)
elif option == 3:
  print("Find the roots of cubic equation in the form ax^2 + bx + c = 0")
  a = float(input("Enter a: "))
  b = float(input("Enter b: "))
  c = float(input("Enter c: "))
  roots = solve_quadratic(a, b, c)
  print(f"The roots of the equation {a}x^2 + {b}x + {c} = 0 are", roots)