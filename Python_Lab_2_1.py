
h_0 = 276 #по варианту
v_0 = 76 #по варианту
g = 1.62
M = 2150
v_gas = 3660
a_max = 29.63
m_0 = 200
v_max = 3

def letim(m, mu, t, h, v, alpha=0):
    dt = 0.001
    delta_t = 0
    if m <= 0:
        mu = 0
    while delta_t <= t:
        dv = (v_gas + v) / (M + m) * mu *dt - g * dt 
        v += dv
        h += v * dt
        delta_t += dt
        m = m - mu * dt
    return v, h, m, dv/dt


t_all = 0
v = -v_0 # тормозим в начальной точке на обратном пути
m = m_0
h = h_0
alpha = 0
mu = 7.8019 #расход топлива
a = 0
t = 0.2
while h > 0:
    t_all += t
    print(round(v, 2), 'm/s\t', round(h, 2), 'm\t', alpha, '\t', mu, 'kg/s\t', t, 's')
    v, h, m, a = letim(m, mu, t, h, v)
    if h <= 0 and v <= -3:
        print('AAAAAAA you are dead!')
        break
    if abs(a) > a_max:
        print('You are dead again')
        break

print(round(v, 2), 'm/s\t', round(h, 2), 'm\t') 
print('Время: ', round(t_all + 2*abs(v_0)/g, 2), 's')
print('Осталось топлива:', round(m, 2), 'kg')