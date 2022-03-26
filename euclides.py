def algoritmoEuclides(r0,r1):
    residuo=r0%r1
    r=[r0,r1]
    q=[]
    n=0
    print("\nCalculo de MCD("+str(r0)+","+str(r1)+"):\n")
    while residuo!=0:
        cosiente=r[n]//r[n+1]
        q.append(cosiente)
        residuo=r[n]%r[n+1]
        r.append(residuo)
        print(str(r[n])+"= "+str(cosiente)+"("+str(r[n+1])+")+"+str(residuo))
        n+=1

    print("\n\tMCD("+str(r0)+","+str(r1)+")="+str(r[-2]))

    if(r[-2]!=1):
        print("MCD("+str(r0)+","+str(r1)+")!=1, por lo tanto no existe inverso multiplicativo")
        return 0

    print("\nCalculo del inverso multiplicativo de "+str(r1)+" modulo "+str(r0)+"\n")

    t=[0,1]
    print("t0= 0\nt1= 1")
    for i in range(0,len(q)-1):
        t.append((t[i]-(q[i]*t[i+1]))%r0)
        print("t"+str(i+2)+"= ("+str(t[i])+"-"+str(q[i])+"("+str(t[i+1])+")) mod. "+str(r0)+" = "+str(t[i+2]))
    return t[-1]

if __name__ == "__main__":
    try:
        while True: # Mientras el usuario no decida finalizar el programa
            r0=int(input('Ingrese r0: '))
            r1=int(input('Ingrese r1: '))
            inv_mult=algoritmoEuclides(r0,r1) # Pasa la cadena del automata para su validacion
            if inv_mult!=0:
                print("\n Por lo tanto, ("+str(r1)+"*"+str(inv_mult)+") mod. "+str(r0)+"=1\n")
            print("\n Presione ^C para terminar") #Instruccion para finalizar el automata "Ctrl + C" (Interrupcion)
    except: # Cuando ocurra la interrupcion indica que es el fin del programa
        print("\nFin del programa")
        exit()