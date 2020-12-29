import re
from heimdall_valid_bank.base_validate_error import InvalidCodeBank

class BankValidate():
    def __init__(self, **kwargs):
        self.bank_code = kwargs.get('bank_code')

    def start(self):
        switcher = {
            '001': 'Banco do Brasil',
            '237': 'Bradesco',
            '341': 'Itaú',
            '033': 'Santander',
            '745': 'Citibank',
            '399': 'HSBC',
            '041': 'Banrisul',
            '260': 'Nubank'
        }

        bank_valid = switcher.get(self.bank_code)

        if not bank_valid:
            return self.valid_bank_generic()

        return True

    def valid_bank_generic(self):
        """
            Valida bancos genéricos
        """
        regex = re.compile('^([0-9A-Za-x]{3,5})$', re.I)
        match = bool(regex.match(self.bank_code))

        if match == False:
            raise InvalidCodeBank()

        return True
