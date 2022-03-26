import math

class Punto:
    def __init__(self, x, y, pend):
        self.x = x
        self.y = y
        self.pend = pend

def power(x, y, p):
    # Initialize result
    res = 1;
     
    # Update x if it is more than or
    # equal to p
    x = x % p;
    while (y > 0):
         
        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p;
 
        # y must be even now
        y = y>>1; # y = y/2
        x = (x * x) % p;
    return res;

def find_mod_inv(a,m):
    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            return x
    raise Exception('El inverso modular no existe.')

# Function to check
# Log base 2
def Log2(x):
    return (math.log10(x) /
            math.log10(2));
 
# Function to check
# if x is power of 2
def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)));

def calc_pend(x1,y1,x2,y2,p,k):
    if x1 != x2:
        return ((y2 - y1) * find_mod_inv(x2 - x1, p)) % p
    else:
        return ((3 * x1 ** 2 - k) * find_mod_inv(2 * y1, p)) % p

# x_3=λ^2-(x_1+x_2) mod. p si x_1≠x_2
def calc_xn(pend, x1, x2, p): # x1 != x2
    if x1 != x2:
        return (pend ** 2 - (x1 + x2)) % p
    else:
        return (pend ** 2 - (2 * x1)) % p

# y_3=λ(x_1-x_3 )-y_1  mod.p
def calc_yn(pend, x1, xn, y1, p):
    return (pend * (x1 - xn) - y1) % p

def calc_sum_punto(x1,y1,x2,y2,p,k):
    pend = calc_pend(x1,y1,x2,y2,p,k)
    xn = calc_xn(pend, x1, x2, p)
    yn = calc_yn(pend, x1, xn, y1, p)
    #print("pend=" + str(pend) + " xn=" + str(xn) + " yn=" + str(yn))
    return Punto(xn,yn,pend)

def generarPuntos(x1,y1,x2,y2,p,k, lim):
    lista = []
    lista_potencias2 = []

    i = 1
    # print("\n>>Lista de puntos X0 potencia de 2:")
    # Punto inicial X0
    p0 = Punto(x1, y1, calc_pend(x1,y1,x2,y2,p,k))
    lista.append(p0)
    lista_potencias2.append(p0)
    print(str(i) + "a(" + str(p0.x) + ",  " + str(p0.y) + ")")

    # Punto 2X0 o x1
    i += 1
    p1 = calc_sum_punto(lista[-1].x, lista[-1].y, lista[-1].x, lista[-1].y, p, k)
    lista.append(p1)
    lista_potencias2.append(p1)
    print(str(i) + "a(" + str(p1.x) + ",  " + str(p1.y) + ")")
    
    i += 1
    for x in range(lim-2):
        p_aux = calc_sum_punto(lista[-1].x, lista[-1].y, lista[0].x, lista[0].y, p , k)
        lista.append(p_aux)
        #print(str(i) + "a: {x: " + str(p_aux.x) + ", y: " + str(p_aux.y) + "}")
        print(str(i) + "a= (" + str(p_aux.x) + ", " + str(p_aux.y) + ")")
        lista_potencias2.append(p_aux)
        i += 1
    return lista_potencias2

def doblar(q):
    bin_q = format(q-1, 'b')
    posiciones = []
    rev = bin_q[::-1]
    for i in range(len(rev)):
        if rev[i] == '1':
            posiciones.append(i)
    # for pos in posiciones:
    #     print(pos)
    return posiciones


def sumarPuntosDoblados(listPosi, listPuntos, p, k):
    listPosi_inv = listPosi[::-1]
    # Res ultimo punto de la lista original 
    res = listPuntos[listPosi_inv[0]]
    acum = 0

    print("\nSe suman los puntos :")
    for i in range(len(listPosi_inv)-1):
        acum = acum + 2 ** listPosi_inv[i]
        print("(q-1)(α) = " + str(acum) + "α + " + str(2 ** (listPosi_inv[i+1]))+"α")
        res = calc_sum_punto(res.x, res.y, listPuntos[listPosi_inv[i+1]].x, listPuntos[listPosi_inv[i+1]].y, p, k)
        

    print("\nültimo punto generado (" + str(res.x) + ", " + str(res.y) + ")")
    aux = (-listPuntos[0].y) % p
    if aux == res.y:
        print("El punto es generador")
    else:
        print("El punto NO es generador")
    return res


def run():
    a = 651
    b = 170
    alpha = [55211, 443096]

    # Ejemplo del libro
    # a = 17
    # b = 8
    # alpha = [231, 217]

    # y^2≡x^3-kx mod.p
    alpha = [int(input('Ingrese Xo= ')), int(input('Ingrese Yo= '))]
    a = int(input('Ingrese a= '))
    b = int(input('Ingrese b= '))
    lim = int(input('Clave Privada Beta= '))
    

    p = a ** 2 + b ** 2 # p impar y b par
    # Encontrar un factor primo del número p+2a+1 = q
    q = int((p + 2*a + 1)/4)
    k = ((alpha[0] ** 3 - alpha[1] ** 2) * find_mod_inv(alpha[0], p)) % p

    #print("\np = " + str(p))
    #print("q = " + str(q))
    #print("k = " + str(k))

    # Procedimiento de doblar
    bin_q = format(q-1, 'b')
    posiciones = doblar(q)
    #print("\nConversión a binario: "+bin_q)
    print("El bit " + str(posiciones[-1])+" es el mas significativo\n")

    #print("\nDebemos calcular hasta el punto " + str(2**posiciones[-1]) + "_X0")
    puntos = generarPuntos(alpha[0], alpha[1],alpha[0], alpha[1], p, k, lim)
    #punto_final = sumarPuntosDoblados(posiciones, puntos, p, k)


if __name__ == '__main__':
    run()