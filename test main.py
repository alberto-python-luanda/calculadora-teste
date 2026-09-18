from main import dividir, somar, multiplicar

def test_somar():
    assert somar(2, 3) == 5

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(10, 0) == 0

def test_multiplicar():
    assert multiplicar(3, 4) == 12

print("Todos os testes passaram!")
