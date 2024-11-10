from Index import Documento

while True:

    try:
        print()
        scelta = int(input("Scegli una voce dal menù:\n 1)Crea Documento\n 2)Visualizza Documenti Creati\n 3)Esci\n"))
        print()
        if scelta == 1:
            try:
                print('Inizia a creare il tuo documento:')
                codice = input('Inserisci il codice:\n')
                descrizione = input('Inserisci la descrizione:\n')
                articolo = Documento(codice, descrizione)
                print(articolo)
            except ValueError:
                print("Riprova")
                
        elif scelta == 2:
            print(Documento.registro())

        elif scelta == 3:
            print("Arrivederci!")
            break
        else:
            print("Inserisci un numero da 1 a 3!!")
    except ValueError:
        print("Deve essere un INT")
        
