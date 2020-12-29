import re
from heimdall_valid_bank.utils.constants import GenericVariables
from heimdall_valid_bank.common_validate import CommonValidate
from heimdall_valid_bank.generic_validators import GenericValidators
from heimdall_valid_bank.base_validate_error import InvalidAccountNumber, InvalidDigitAccountNumber
from heimdall_valid_bank.calculate_number_account import CalculateAccount
class AccountValidate(CommonValidate):
    """ 
        This class is responsible for validating the bank account number
        
        Attributes: 
            bank_code (string): Bank code, usually 3 digits ex.: 001. 
            agency (string): Agency number with or without the digit ex.: 2345-9, 2345.
            digit_agency (String): Digit of the agency, if passed with the agency it is not necessary to inform the digit here.
            account (string): Account number with or without the digit, for example: 12345678-9, 12345678.
            digit_account (string): Account type if it exists, however, if informed with the account there is no need to inform it again.
    """
    def __init__(self, **kwargs):
        self.agency = kwargs.get('agency')
        self.bank_code = kwargs.get('bank_code')
        self.account = kwargs.get('account')
        self.digit_agency = kwargs.get('digit_agency')
        self.digit_account = kwargs.get('digit_account')

    def start(self):
        try:
            regex = re.search('[@_!#$%^&*()<>?/\-.|}{~:]', self.account)
            if regex:
                self.digit_account = self.account[regex.start() + 1:len(self.account)]
                self.account = self.account[0:regex.start()]
            
            if self.bank_code not in GenericVariables.LIST_BANKS:
                return self.valid_account_generic()
         
            switcher = {
                '001': self.valid_account_bb,
                '237': self.valid_account_bradesco,
                '341': self.valid_account_itau,
                '033': self.valid_account_santander,
                '745': self.valid_account_citibank,
                '041': self.valid_account_banrisul,
                '104': self.valid_account_caixa,
                '260': self.valid_account_nubank
            }

            return switcher.get(self.bank_code)()
        except Exception:
            return False

    def valid_account_generic(self):
        """
            Valida contas genéricas
        """
        result = GenericValidators.account_is_valid(self.account)

        if self.digit_account:
            result = GenericValidators.account_digit_is_valid(self.digit_account)

        return result

    def valid_account_bb(self):
        """
          Valida a conta e o dígito verificador do Banco do Brasil
          Tamanho da Conta - 8 Dígitos + 1 DV
        """
        check_number_calculated_account = self.check_number_calculate_account(
            account=self.account,
            digit_account=self.digit_account,
            length_account=8,
            bank='bb'
        )
        
        return check_number_calculated_account == self.digit_account.upper()

    def valid_account_banrisul(self):
        """
          Valida a conta e o dígito verificador do banco Banrisul
          Tamanho da Conta - 9 Dígitos + 1 DV (sendo os dois primeiros o tipo de conta)
        """
        check_number_calculated_account = self.check_number_calculate_account(
            account=self.account,
            digit_account=self.digit_account,
            length_account=9,
            bank='banrisul'
        )

        return check_number_calculated_account == self.digit_account

    def valid_account_bradesco(self):
        """
          Valida a conta e o dígito verificador do banco Bradesco
          Tamanho da Conta - 7 Dígitos + 1 DV
        """
        check_number_calculated_account = self.check_number_calculate_account(
            account=self.account,
            digit_account=self.digit_account,
            length_account=7,
            bank='bradesco'
        )

        check_number_informed_account = self.digit_account.upper()

        if check_number_informed_account == '0':
            return check_number_calculated_account == check_number_informed_account or check_number_calculated_account == 'P'

        return check_number_calculated_account == check_number_informed_account

    def valid_account_citibank(self):
        """
          Valida a conta e o dígito verificador do banco Banrisul
          Tamanho da Conta - 10 Dígitos + 1 DV
        """
        check_number_calculated_account = self.check_number_calculate_account(
            account=self.account,
            digit_account=self.digit_account,
            length_account=10,
            bank='citibank'
        )

        return check_number_calculated_account == self.digit_account

    def valid_account_itau(self):
        """
          Valida a conta e o dígito verificador do banco Itaú
          Tamanho da Conta - 5 Dígitos + 1 DV
        """
        account_agency = self.account + self.agency
        check_number_calculated_account = self.check_number_calculate_account(
            account=account_agency,
            digit_account=self.digit_account,
            length_account=5,
            bank='itau'
        )

        return check_number_calculated_account == self.digit_account

    def valid_account_santander(self):
        """
          Valida a conta e o dígito verificador do banco Santander
          Tamanho da Conta - 8 dígitos + 1 DV
        """
        check_number_calculated_account = self.check_number_calculate_account(
            agency=self.agency,
            account=self.account,
            digit_account=self.digit_account,
            length_account=8,
            bank='itau'
        )

        return check_number_calculated_account == self.digit_account

    def valid_account_caixa(self):
        """
          Valida a conta e o dígito verificador do banco Caixa Econômica Federal
          Tamanho da Conta - 11 Dígitos + 1 DV
        """
        
        check_number_calculated_account = self.check_number_calculate_account(
            agency=self.agency,
            account=self.account,
            digit_account=self.digit_account,
            length_account=11,
            bank='caixa'
        )

        return check_number_calculated_account == self.digit_account

    def valid_account_nubank(self):
        """
          Valida a conta e o dígito verificador do banco Nu Pagamentos (Nubank)
          Tamanho da Conta - 7 Dígitos + 1 DV
        """
        check_number_calculated_account = self.check_number_calculate_account(
            agency=self.agency,
            account=self.account,
            digit_account=self.digit_account,
            length_account=7,
            bank='nubank'
        )
        
        return check_number_calculated_account == self.digit_account

    def check_number_calculate_account(self, **kwargs):
        account, digit_account, length_account, bank = kwargs.values()
        agency = kwargs.get('agency', None)
        
        if len(account) < length_account:
            account = f'%0{length_account}d' % int(account)
       
        result_valid_account = super().account_is_valid(account)
        
        if not result_valid_account:
            raise InvalidAccountNumber()
        
        result_valid_digit_account = super().account_digit_is_valid(digit_account)
    
        if not result_valid_digit_account:
            raise InvalidDigitAccountNumber()
        
        
        switcher = {
            'bb': CalculateAccount(account=account).calculate_account_bb,
            'bradeso': CalculateAccount(account=account).calculate_account_bradesco,
            'itau': CalculateAccount(account=account).calculate_account_itau,
            'santander': CalculateAccount(account=account, agency=agency).calculate_account_santander,
            'citibank': CalculateAccount(account=account).calculate_account_citibank,
            'banrisul': CalculateAccount(account=account).calculate_account_banrisul,
            'caixa': CalculateAccount(account=account).calculate_account_caixa,
            'nubank': CalculateAccount(account=account).calculate_account_nubank,
        }
        
        result_check_number_account = switcher.get(bank)()

        if not result_check_number_account:
            raise InvalidAccountNumber()
        
        return result_check_number_account
            
        
    
    
        
        