'''
Questo programma prende un numero in ingresso, chiede la base di partenza e lo converte in una base di arrivo.
Come prima cosa converte il numero come intermezzo decimale, poi lo converte nella base di destinazione.
'''

Numero1 = str(input("Inserisci il numero INTERO che vuoi convertire: "))
Numero1lista = []
Numero1Decimale = 0
Numero2 = " "
Numero2lista = []

B1 = int(input("Inserisci la base di partenza: "))
B2 = int(input("Inserisci la base di arrivo: "))
Finale = " "
VOID = None

#inizio la divisione del PRENumero1 nel Numero (LISTA)
tempy = 0
for i in range(len(Numero1)):
    Numero1lista.append(Numero1[tempy])
    tempy += 1
tempy = 1
Numero1 == int(Numero1)
#Verifica della leicità dell'operazione
if any(int(num) > B1 - 1 for num in Numero1lista):
    VOID = True
else:
    VOID = False

if VOID == True:
    print("Attenzione! Il numero inserito o la base di partenza sono errate!")
    quit()

#inizio del programma vero e proprio
if B1 == B2:
    print("La base di partenza è la stessa della base di arrivo... Che cosa vuoi convertire?")
    quit()


if B1 != 10:
    Numero1lista = Numero1lista[len(Numero1lista)::-1]
    for i in Numero1lista:
        Numero1Decimale += int(i) * (B1) ** Numero1lista.index(i)

while Numero1Decimale % B2 != 0 and Numero1Decimale // B2 != 0:
    Numero2 += str(Numero1Decimale % B2)
    Numero1Decimale = Numero1Decimale // B2
print(Numero2)



