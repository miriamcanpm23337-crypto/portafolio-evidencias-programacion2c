import unittest
from cuenta import Cuenta

class TestCuenta(unittest.TestCase):
    
    def setUp(self):
        """
        Se ejecuta antes de cada prueba
        """
        self.cuenta = Cuenta("Fulanito Perez Mengano", "001")
        
    # ------------- PRUEBAS DEL CONSTRUCTOR --------------
    
    def test_validar_saldo(self):
        self.assertEqual(self.cuenta.saldo, 0, "El saldo inicial debería ser 0 por defecto")
        
    def test_validar_cliente(self):
        self.assertEqual(self.cuenta.cliente, "Fulanito Perez Mengano", "El nombre del cliente no es corecto")
    
    # ------------- PRUEBAS DE DEPOSITO ------------------
    
    def test_depositar_dinero_valido(self):
        result = self.cuenta.deposito(500.00)
        self.assertTrue(result)
        self.assertEqual(self.cuenta.saldo, 500, "El saldo actual debería ser de 500.00")
        
    def test_depositar_cantidad_negativa(self):
        result = self.cuenta.deposito(-200)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "El saldo actual debería ser 0")
        
    # test para validar deposito en 0
    def test_depositar_cantidad_invalida(self):
        result = self.cuenta.deposito(0)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "El saldo debería ser 0 al no poder depositar una cantidad menor o igual a 0")
    
    # ---------------- PRUEBAS DE RETIRO -----------------------
    
    # 1. test para validar retiro con cantidad 0
    def test_retirar_cantidad_invalida(self):
        result = self.cuenta.retirar(0)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "El saldo debería permanecer en 0 si la cantidad a retirar es mayor o igual al saldo actual")
    
    # 2. test para validar retiro con cantidad negativa
    def test_retirar_cantidad_negativa(self):
        result = self.cuenta.retirar(-500)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "El saldo debería ser 0 si la cantidad a retirar es menor a 0")
    
    # 3. test para validad cantidad mayor al saldo
    def test_retirar_cantidad_mayor_saldo(self):
        result = self.cuenta.retirar(1000)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "El saldo debería ser 0, no se puede retirar una cantidad mayor al saldo")
    