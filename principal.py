import funciones
import json

# Cargar los datos del archivo JSON en una variable
with open('Elden_Ring.json', 'r') as file:
    data = json.load(file)

def mostrar_menu():
    print("\n=== Elden Ring ====")
    print("1. Listar Aliados")
    print("2. Contar Armas por Tipo")
    print("3. Buscar Arma por Nombre")
    print("4. Buscar Hechizos por Tipo")
    print("5. Buscar Aliado y Recomendar Armas")
    print("6. Salir")

def mostrar_separador():
    print("=================================================\n")

def menu():
    while True:
        mostrar_menu()
        
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == '1':
            aliados = funciones.listar_aliados(data)
            mostrar_separador()
            print("Aliados disponibles:")
            for aliado in aliados:
                print(aliado)
        elif opcion == '2':
            conteo = funciones.contar_armas_por_tipo(data)
            mostrar_separador()
            print("Total de armas por tipo:")
            for tipo, total in conteo.items():
                print(f"{tipo.capitalize()}: {total}")
        elif opcion == '3':
            nombre_arma = input("Ingrese el nombre del arma: ")
            arma = funciones.buscar_arma_por_nombre(data, nombre_arma)
            mostrar_separador()
            if isinstance(arma, dict):
                print(f"Nombre: {arma['nombre']}")
                print(f"Ataque: {arma['ataque']}")
                print(f"Descripción: {arma['descripcion']}")
            else:
                print(arma)
        elif opcion == '4':
            tipo_hechizo = input("Ingrese el tipo de hechizo: ")
            hechizos = funciones.buscar_hechizos_por_tipo(data, tipo_hechizo)
            mostrar_separador()
            if hechizos:
                print(f"Hechizos de tipo {tipo_hechizo.capitalize()}:")
                for hechizo in hechizos:
                    print(f"Nombre: {hechizo['nombre']}")
                    print(f"Descripción: {hechizo['descripcion']}\n")
            else:
                print("No se encontraron hechizos de ese tipo.")
        elif opcion == '5':
            nombre_aliado = input("Ingrese el nombre del aliado: ")
            resultado = funciones.buscar_aliado_y_recomendar_armas(data, nombre_aliado)
            mostrar_separador()
            if isinstance(resultado, dict):
                aliado = resultado['Aliado']
                print(f"Nombre: {aliado['nombre']}")
                print(f"Tipo: {aliado['tipo']}")
                print(f"Descripción: {aliado['descripcion']}")
                print("Recomendaciones de Armas:")
                for arma in resultado['Recomendaciones de Armas']:
                    print(arma)
            else:
                print(resultado)
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
