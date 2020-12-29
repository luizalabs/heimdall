from unittest import TestCase
from heimdall_valid_bank.calculate_number_account import CalculateAccount
from heimdall_valid_bank.tests.data import BANCO_DO_BRASIL, BRADESCO, BANRISUL, CAIXA_ECONOMICA_FEDERAL, SANTANDER, CITIBANK, ITAU, NUBANK

class TestCalculateAccount(TestCase):

    def test_calculate_account_bb_valid(self):
        bank = BANCO_DO_BRASIL['valid_combinations']
        digits_calculated = []
        accounts_digit = []
      
        for i in range(len(bank)):
            account = bank[i]['account']
            if len(account) < 8:
                account = f'%08d' % int(account)
                
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=account
                
            ).calculate_account_bb()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])
        
        assert digits_calculated == accounts_digit        
        
    def test_calculate_account_bb_invalid(self):
        bank = BANCO_DO_BRASIL['invalid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
                
            ).calculate_account_bb()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])
      
        assert digits_calculated != accounts_digit
        
    def test_calculate_account_banrisul_valid(self):
        bank = BANRISUL['correct_account']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                account=bank[i][0]
            ).calculate_account_banrisul()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i][1])
        assert digits_calculated == accounts_digit        
      
    def test_calculate_account_bradesco_valid(self):
        bank = BRADESCO['valid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            account = bank[i]['account']
            if len(account) < 7:
                account = f'%07d' % int(account)
                
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=account
                
            ).calculate_account_bradesco()
            
            digits_calculated.append(calculate_account)
            if bank[i]['account_digit'] == '0' or bank[i]['account_digit'] == 'P':
                bank[i]['account_digit'] = calculate_account
                
            accounts_digit.append(bank[i]['account_digit'])
    
        assert digits_calculated == accounts_digit  
        
    def test_calculate_account_bradesco_invalid(self):
        bank = BRADESCO['invalid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
                
            ).calculate_account_bradesco()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])
    
        assert digits_calculated != accounts_digit    
        
    def test_calculate_account_itau_valid(self):
        bank = ITAU['valid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            account = bank[i]['branch'] + bank[i]['account']
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=account
                
            ).calculate_account_itau()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])

        assert digits_calculated == accounts_digit
        
    def test_calculate_account_itau_invalid(self):
        bank = ITAU['invalid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            account = bank[i]['branch'] + bank[i]['account']
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=account
                
            ).calculate_account_itau()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])

        assert digits_calculated != accounts_digit
    
    def test_calculate_account_santander_valid(self):
        bank = SANTANDER['valid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
            ).calculate_account_santander()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])

        assert digits_calculated == accounts_digit
        
    def test_calculate_account_santander_invalid(self):
        bank = SANTANDER['invalid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
            ).calculate_account_santander()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])

        assert digits_calculated != accounts_digit
        
    def test_calculate_account_citibank_valid(self):
        bank = CITIBANK['valid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
            ).calculate_account_citibank()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])

        assert digits_calculated == accounts_digit
    
    def test_calculate_account_caixa_valid(self):
        bank = CAIXA_ECONOMICA_FEDERAL['valid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
            ).calculate_account_caixa()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])

        assert digits_calculated == accounts_digit
        
    def test_calculate_account_caixa_invalid(self):
        bank = CAIXA_ECONOMICA_FEDERAL['invalid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
            ).calculate_account_caixa()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])

        assert digits_calculated != accounts_digit
        
    def test_calculate_account_nubank_valid(self):
        bank = NUBANK['valid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
            ).calculate_account_nubank()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])

        assert digits_calculated == accounts_digit
     
     
    