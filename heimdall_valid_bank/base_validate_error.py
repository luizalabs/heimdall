class InvalidAgencyNumber(Exception):
    def __init__(self, agency_number=None):
        self.message = 'Agência inválida.'

        if agency_number is not None:
            self.message = f'A agência deve conter {agency_number} números. Complete com zeros a esquerda se necessário.'

        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidDigitAgencyNumber(Exception):
    def __init__(self):
        self.message = f'Dígito da agência inválido.'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidAccountNumber(Exception):
    def __init__(self, account_number=None):
        self.message = 'Conta inválida'

        if account_number is not None:
            self.message = f'A conta corrente deve conter {account_number} números. Complete com zeros a esquerda se necessário'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidDigitAccountNumber(Exception):
    def __init__(self, digit_account=None):
        self.message = 'Dígito da conta não corresponde ao número da conta/agência preenchido'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InvalidCodeBank(Exception):
    def __init__(self):
        self.message = 'Banco inválido'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
