from unittest import TestCase, main
import abc

class Calculadora(object):
    def calcula(self, value1, value2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if operacao == None:
            return 0
        else:
            resultado = operacao.executar(value1, value2)
            return resultado



class OperacaoFabrica(object):

    def criar(self, operador):

        if operador == 'soma':
            return Soma()

        elif operador == 'divisao':
            return Divisao()

        elif operador == 'subtracao':
            return Subtracao()

        elif operador == 'multiplicacao':
            return Multiplicacao()


class Operacao(metaclass=abc.ABCMeta):

    def executar(self, value1, value2):
        pass


class Soma(Operacao):
    def executar(self, value1, value2):

        return value1 + value2


class Divisao(Operacao):
    def executar(self, value1, value2):

        resultado = value1 / value2

        return resultado


class Subtracao(Operacao):
    def executar(self, value1, value2):

        resultado = value1 - value2

        return resultado


class Testes(TestCase):

    def test_divisao(self):

        dividindo = Calculadora()
        self.assertEqual(dividindo.calcula(12, 6, 'divisao'), 2)

    def test_soma(self):

        somando = Calculadora()
        self.assertEqual(somando.calcula(10, 4, 'soma'), 14)

    def test_subtracao(self):

        calcula = Calculadora()
        self.assertEqual(calcula.calcula(9, 10, 'subtracao'), -1)
    

        

surch = Calculadora()
yis = surch.calcula(5, 5, 'soma')


if __name__ == '__main__':
    main()