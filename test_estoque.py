
import unittest
from unittest.mock import patch
import estoque


class TestesUnitarios(unittest.TestCase):

    def setUp(self):
        estoque.produtos.clear()

    def test_cadastrar_produto(self):
        with patch("builtins.input", side_effect=["Body Estrelinha", "10", "3"]):
            estoque.cadastrar_produto()

        self.assertEqual(len(estoque.produtos), 1)
        self.assertEqual(estoque.produtos[0]["nome"], "Body Estrelinha")
        self.assertEqual(estoque.produtos[0]["quantidade"], 10)

    def test_nao_cadastrar_nome_vazio(self):
        with patch("builtins.input", return_value=" "):
            estoque.cadastrar_produto()

        self.assertEqual(len(estoque.produtos), 0)

    def test_validar_quantidade_negativa(self):
        with patch("builtins.input", side_effect=["-2", "5"]):
            quantidade = estoque.ler_quantidade("Quantidade: ")

        self.assertEqual(quantidade, 5)

    def test_verificar_estoque_baixo(self):
        estoque.produtos.append({
            "nome": "Body Estrelinha",
            "quantidade": 2,
            "minimo": 3
        })

        with patch("builtins.print") as saida:
            estoque.verificar_estoque()

        saida.assert_any_call("ALERTA: Estoque baixo - Body Estrelinha")

    def test_registrar_saida(self):
        estoque.produtos.append({
            "nome": "Body Estrelinha",
            "quantidade": 10,
            "minimo": 3
        })

        with patch("builtins.input", side_effect=["Body Estrelinha", "4"]):
            estoque.registrar_saida()

        self.assertEqual(estoque.produtos[0]["quantidade"], 6)


class TesteIntegracao(unittest.TestCase):

    def setUp(self):
        estoque.produtos.clear()

    def test_fluxo_completo_do_menu(self):
        entradas = [
            "1",
            "Body Estrelinha",
            "10",
            "3",
            "4",
            "Body Estrelinha",
            "2",
            "2",
            "0"
        ]

        with patch("builtins.input", side_effect=entradas):
            estoque.menu()

        self.assertEqual(len(estoque.produtos), 1)
        self.assertEqual(estoque.produtos[0]["quantidade"], 8)


if __name__ == "__main__":
    unittest.main()
