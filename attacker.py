def run_attacker():
    do_continue = True
    no_processes = 0
    processes = list()

    while do_continue:
        # Ask how many inputs do you want.
        print(f"Actualmente hay {no_processes} procesos.")
        print("Ingrese el número de procesos de ataque que desea que existan:")
        new_no_processes = int(input())
        if new_no_processes == no_processes:
            print("Ya hay ese número de procesos activos.")
        elif new_no_processes < 0 or new_no_processes > 50:
            print("Sólo se permiten de 0 a 50 procesos activos.")
        else:
            dif_no_processes = abs(new_no_processes - no_processes)
            if new_no_processes > no_processes:
                print(f"Iniciando {dif_no_processes} procesos de ataque.")
                for _ in range(dif_no_processes):
                    print("Starting attack process")
                print(f"Se iniciaron {dif_no_processes} procesos de ataque satisfactoriamente.")
            else:
                print(f"Deteniendo {dif_no_processes} procesos de ataque.")
                for _ in range(dif_no_processes):
                    print("Stopping attack process")
                print(f"Se detuvieron {dif_no_processes} procesos de ataque satisfactoriamente.")
            no_processes = new_no_processes


if __name__ == "__main__":
    run_attacker()