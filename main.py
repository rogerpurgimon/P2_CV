from tasks import Tasks

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("1. Exercici 1"
          "\n2.Exercici 2"
          "\n3. Exercici 3"
          "\n4.Exercici 4"
          "\n5.Finalitzar el programa")

    ex = 0
    task = Tasks()
    while(ex != 5):

        ex = int(input("Escriu la tasca que vols executar (1,2,3,4): "))

        if ex == 1:
            task.parse_info()
        elif ex == 2:
            task.new_container()
        elif ex == 3:
            task.resize()
        elif ex == 4:
            task.checl_track()
        elif ex == 5:
            print('------Programa finalitzat------')
            break