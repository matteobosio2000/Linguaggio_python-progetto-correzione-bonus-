import os

def il_menu():
    print("\nMenu della lista della spesa")
    print("1 - Aggiungere un elemento alla lista")
    print("2 - Rimuovere un elemento dalla lista")
    print("3 - Visualizzare tutti gli elementi ordinati alfabeticamente")
    print("4 - Salvare la lista su file")
    print("5 - Caricare una lista da file")
    print("6 - Uscire dal programma")

def aggiungi_elemento(lista):
    elemento = input("Inserisci l'elemento da aggiungere: ").strip()
    if elemento:
        lista.append(elemento)
        print(f"'{elemento}' è stato aggiunto alla lista.")
    else:
        print("Elemento non valido.")

def rimuovi_elemento(lista):
    elemento = input("Inserisci l'elemento da rimuovere: ").strip()
    if elemento in lista:
        lista.remove(elemento)
        print(f"'{elemento}' è stato rimosso dalla lista.")
    else:
        print(f"'{elemento}' non è presente nella lista.")

def visualizza_lista(lista):
    if lista:
        print("\nLista della Spesa (in ordine alfabetico):")
        for elemento in sorted(lista):
            print(f"- {elemento}")
    else:
        print("La lista è vuota.")

def salva_su_file(lista, nome_file="lista_spesa.txt"):
    try:
        with open(nome_file, "w") as file:
            for elemento in lista:
                file.write(elemento + "\n")
        print(f"Lista salvata su '{nome_file}'.")
    except Exception as e:
        print(f"Errore durante il salvataggio: {e}")

def carica_da_file(nome_file="lista_spesa.txt"):
    try:
        if not os.path.exists(nome_file):
            print(f"Il file '{nome_file}' non esiste.")
            return []
        with open(nome_file, "r") as file:
            lista = [linea.strip() for linea in file]
        print(f"Lista caricata da '{nome_file}'.")
        return lista
    except Exception as e:
        print(f"Errore durante il caricamento: {e}")
        return []

def main():
    lista_spesa = []
    while True:
        il_menu()
        scelta = input("\nScegli un'opzione (1-6): ").strip()
        if scelta == "1":
            aggiungi_elemento(lista_spesa)
        elif scelta == "2":
            rimuovi_elemento(lista_spesa)
        elif scelta == "3":
            visualizza_lista(lista_spesa)
        elif scelta == "4":
            salva_su_file(lista_spesa)
        elif scelta == "5":
            lista_spesa = carica_da_file()
        elif scelta == "6":
            print("Uscita dal programma. Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()

