def speed():
    d = float(input('Enter distance d (meters) : '))
    t = float(input('Enter time t (seconds) : '))
    print('Speed = {:.4f} m/s'.format(d/t))
def force():
    m = float(input('Enter mass m (kg) : '))
    a = float(input('Enter acceleration a (m/s^2) : '))
    print('force = {:.4f} N'.format(m*a))
def work_done():
    f = float(input('Enter force F(N)) : '))
    d = float(input('Enter distance d (m) : '))
    print('Work-Done = {:.4f} J'.format(f*d))
def density():
    m = float(input('Enter mass (kg) : '))
    v = float(input('Enter volume (m^3)'))
    print('Density = {:.4f} kg/m^3'.format(m/v))
def resistance():
    v = float(input('Enter voltage v (v) : '))
    I = float(input('Enter current I (A) : '))
    print('Resistance is = {:.4f} (ohm)'.format(v/I))
print('Welcome to your physic formula')
print('Pleace check which formula you want to use')
print('a is speed')
print('b is force')
print('c is Work Done')
print('d is density')
print('e is resistance')
ask = str(input('Enter your alphabet choice(a/b/c/d/e): ' ))
if ask == 'a':
    speed()
elif ask == 'b':
    force()
elif ask == 'c':
    work_done()
elif ask == 'd':
    density()
elif ask == 'e':
    resistance()
else:
    print("Invalid choice")