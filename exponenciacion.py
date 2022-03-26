def exponenciar(x,a,n):
    z=1
    b=str(bin(a)).lstrip("0b")[::-1]
    print("i\tbi\tz=z^2\tz=z*x")
    for i in range(len(b),0,-1):
        z=pow(z,2)%n
        if b[i-1]=='1':
            aux=z
            z=(z*x)%n
            print(str(i-1)+"\t"+str(b[i-1])+"\t"+str(aux)+"\t"+str(z))
        else:
            print(str(i-1)+"\t"+str(b[i-1])+"\t"+str(z)+"\t \t")
    return z

if __name__ == "__main__":
    try:
        while True: # Mientras el usuario no decida finalizar el programa
            x=int(input('Ingrese x: '))
            a=int(input('Ingrese a: '))
            n=int(input('Ingrese n: '))
            z=exponenciar(x,a,n) # 
            print("\n\tPor lo tanto: ("+str(x)+"^"+str(a)+") mod "+str(n)+" = "+str(z))
            print("\n Presione ^C para terminar") #Instruccion para finalizar el automata "Ctrl + C" (Interrupcion)
    except: # Cuando ocurra la interrupcion indica que es el fin del programa
        print("\nFin del programa")
        exit()