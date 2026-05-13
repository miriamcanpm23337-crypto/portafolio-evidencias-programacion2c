class Cuenta:
    """
    Gestiona la información basica de una cuenta bancaria, asi como, los movimientos de la cuenta (depósitos y retiros)
    validando la información de la cuenta e integridad del saldo.
    
    Attributes:
        cliente (str): Nombre del cliente de la cuenta.
        cuenta (str): Numero de 10 digitos asignado a la cuenta.
        saldo (float): Saldo actual de la cuenta.
    """
    def __init__(self, cliente, cuenta, saldo = 0):
        """
        Inicializa una nueva cuenta bancaria.
        
        Args:
            cliente (str): Nombre del cliente de la cuenta.
            cuenta (str): Numero de 10 digitos asignado a la cuenta.
            saldo (float): Saldo de la cuenta.
        """
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo
    
    def deposito(self, cantidad):
        """
        Deposita la cantidad deseada a la cuenta, validando que la cantidad sea mayor a 0
        
        Args:
            cantidad (float): Valor numerico flotante de la cantidad a depositar a la cuenta.
            
        Returns:
            (bool): True si el deposito fue exitoso.
                False si la cantidad es invalida. 
        """
        if cantidad > 0:
            self.saldo += cantidad #self.saldo = self.saldo + cantidad
            return True
        return False
    
    def retirar(self, cantidad):
        """
        Retira una cantidad mayor a 0 y menor o igual al saldo de la cuenta.
        
        Args:
            cantidad (float): Valor numerico flotante de la cantidad a retirar a la cuenta.
            
        Returns:
            (bool): True si el retiro fue exitoso.
                False si la cantidad es invalida. 
        """
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False

def main():
    pass

if __name__ == "__main__":
    main()
    