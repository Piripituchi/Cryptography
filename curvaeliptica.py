import random

def crear_primo(a,b):
    n=pow(a,2)+pow(b,2)
    m=1
    k=1
    while k>=1:
        m=(n-1)/(2**k)
        if m%2!=0:
            break
        k+=1
    a=random.randint(1,n-1)
    b=exponenciar(a,int(m),n)
    if b==1:
        return n
    for i in range(0,k):
        if b==-1%n:
            return n
        else:
            b=exponenciar(b,2,n)
    return crear_primo(a,b+2)

def es_primo(n):
    m=1
    k=1
    while k>=1:
        m=(n-1)/(2**k)
        if m%2!=0:
            break
        k+=1
    a=random.randint(1,n-1)
    b=exponenciar(a,int(m),n)
    if b==1:
        return True
    for i in range(0,k):
        if b==-1%n:
            return True
        else:
            b=exponenciar(b,2,n)
    return False

def exponenciar(x,a,n):
    z=1
    b=str(bin(a)).lstrip("0b")[::-1]
    #print("i\tbi\tz=z^2\tz=z*x")
    for i in range(len(b),0,-1):
        z=pow(z,2)%n
        if b[i-1]=='1':
            aux=z
            z=(z*x)%n
            #print(str(i-1)+"\t"+str(b[i-1])+"\t"+str(aux)+"\t"+str(z))
        #else:
            #print(str(i-1)+"\t"+str(b[i-1])+"\t"+str(z)+"\t \t")
    return z

def crear_k(Xo,Yo,p):
    aux=exponenciar(Xo,p-2,p)
    k=((pow(Xo,3)-pow(Yo,2))*aux)%p
    pot_4=exponenciar(k,int((p-1)/4),p)
    pot_2=exponenciar(k,int((p-1)/2),p)
    if (pot_4!=1 and pot_2==1):
        print("k= "+str(k))
        print("k^[(p-1)/4] mod p = "+str(pot_4))
        print("k^[(p-1)/2] mod p = "+str(pot_2))
    return k

def doblar(x,y,n,p,k):
    x_l=x
    y_l=y
    Xo=[]
    Yo=[]
    b=str(bin(n-1)).lstrip("0b")[::-1]
    for i in range(0,len(b)-1):
        aux=exponenciar(2*y_l,p-2,p)
        lmda=((3*pow(x_l,2)-k)*aux)%p
        aux=x_l
        x_l=(pow(lmda,2)-2*x_l)%p
        y_l=(lmda*(aux-x_l)-y_l)%p
        print(str(pow(2,i+1))+"a( "+str(x_l)+" , "+str(y_l)+" )")
        Xo.append(x_l)
        Yo.append(y_l)
    x_l=Xo[len(Xo)-1]
    y_l=Yo[len(Yo)-1]
    for i in range(len(b)-1,0,-1):
        if b[i-1]=='1':
            y_aux=Yo[i-1]
            x_aux=Xo[i-1]
            aux=exponenciar(x_aux-x_l,p-2,p)
            lmda=((y_l-y_aux)*aux)%p
            aux=x_l
            x_l=(pow(lmda,2)-aux-x_aux)%p
            y_l=(lmda*(aux-x_l)-y_l)%p
    return x_l,y_l





if __name__ == "__main__":
    try:
        while True: # Mientras el usuario no decida finalizar el programa
            a=int(input('Ingrese un impar a>3: '))
            b=int(input('Ingrese un par b>=2: '))
            p=crear_primo(a,b)
            print("p= "+str(p)+"a= "+str(a)+"b= "+str(b))
            q=(p+1+2*a)/4
            print("q= "+str(q))
            if es_primo(q)==False:
                continue
            print("Ingrese el elemento geneador")
            Xo=int(input('Ingrese Xo: '))
            Yo=int(input('Ingrese Yo: '))
            k=crear_k(Xo,Yo,p)
            Xi,Yi=doblar(Xo,Yo,int(q),p,k)
            print("Elliptic Curve")
            print("("+str(q)+"-1)("+str(Xo)+","+str(Yo)+" ) = ("+str(Xi)+","+str(Yi)+")")
            print("y^2=x^3-"+str(k)+"x mod "+str(p))
            print("Generator: ("+str(Xo)+","+str(Yo)+" ) ")
            print("Order = "+str(q))
            print("\n Presione ^C para terminar") #Instruccion para finalizar el programa "Ctrl + C" (Interrupcion)
    except: # Cuando ocurra la interrupcion indica que es el fin del programa
        print("\nFin del programa")
        exit()