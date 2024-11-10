



from src.entrega2.tipos.Cola_prioridad import ColaPrioridad

def test_cola_prioridad():
    cola = ColaPrioridad[str, int]()

    cola.add('Paciente A', 3)
    cola.add('Paciente B', 2)
    cola.add('Paciente C', 1)

    assert cola.elements() == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de la cola es incorrecto."

    atencion = []
    while not cola.is_empty():
        atencion.append(cola.remove())

    assert atencion == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de atención no es correcto."

    print("Pruebas superadas exitosamente.")

if __name__ == '__main__':
    test_cola_prioridad()

