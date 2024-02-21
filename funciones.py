def listar_aliados(data):
    # Lista los nombres de todos los aliados disponibles en el juego.
    aliados = [aliado['nombre'] for aliado in data['elden_ring']['historia']['alianzas']]
    return aliados

def contar_armas_por_tipo(data):
    # Cuenta el total de armas disponibles categorizadas por su tipo.
    conteo = {}
    for categoria in ['espadas', 'arcos', 'lanzas']:
        conteo[categoria] = len(data['elden_ring']['armamento'][categoria])
    return conteo

def buscar_arma_por_nombre(data, nombre_arma):
    # Busca armas por su nombre y muestra su descripción y ataque.
    for categoria in data['elden_ring']['armamento']:
        for arma in data['elden_ring']['armamento'][categoria]:
            if arma['nombre'].lower() == nombre_arma.lower():
                return arma
    return "Arma no encontrada."

def buscar_hechizos_por_tipo(data, tipo_hechizo):
    # Busca hechizos por tipo y muestra todos los hechizos de ese tipo con su descripción.
    hechizos = [hechizo for hechizo in data['elden_ring']['armamento']['hechizos'] if hechizo['tipo'].lower() == tipo_hechizo.lower()]  # Corrected path
    return hechizos

def buscar_aliado_y_recomendar_armas(data, nombre_aliado):
    # Busca un aliado por nombre y muestra toda la información relacionada, incluyendo armas recomendadas.
    for aliado in data['elden_ring']['historia']['alianzas']:
        if aliado['nombre'].lower() == nombre_aliado.lower():
            tipo_aliado = aliado['tipo']
            recomendaciones = []
            if tipo_aliado == "Aliado":
                recomendaciones = ['Espada de la Luz', 'Lanza del Amanecer']
            return {'Aliado': aliado, 'Recomendaciones de Armas': recomendaciones}
    return "Aliado no encontrado."