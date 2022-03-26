import random
import exponenciacion

def es_primo(n):
    m=1
    k=1
    while k>=1:
        m=(n-1)/(2**k)
        if m%2!=0:
            break
        k+=1
    a=random.randint(1,n-1)
    b=exponenciacion.exponenciar(a,int(m),n)
    print("n-1: "+str(n-1)+"\nm: "+str(m)+"\nk: "+str(k)+"\na: "+str(a))
    if b==1:
        print("b: "+str(b))
        return (str(n)+" Es primo")
    for i in range(0,k):
        if b==-1%n:
            print("b: "+str(b))
            return(str(n)+" Es primo")
        else:
            b=exponenciacion.exponenciar(b,2,n)
    print("b: "+str(b))
    return(str(n)+" Es compuesto")

if __name__ == "__main__":
    try:
        while True: # Mientras el usuario no decida finalizar el programa
            n=int(input('Ingrese n: '))
            s=es_primo(n) # 
            print("\n\tPor lo tanto: "+s)
            print("\n Presione ^C para terminar") #Instruccion para finalizar el programa "Ctrl + C" (Interrupcion)
    except: # Cuando ocurra la interrupcion indica que es el fin del programa
        print("\nFin del programa")
        exit()