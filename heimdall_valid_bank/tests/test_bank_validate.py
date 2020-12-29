from unittest import TestCase
from heimdall_valid_bank.bank_validate import BankValidate
class TestBankValidate(TestCase):
    def test_start_bank_validate(self):
        banks_code = ['001', '237', '341', '033', '745', '399', '041', '260']
        bank_return = []
        for bank in banks_code:
            bank_valid = BankValidate(bank_code=bank).start()
            bank_return.append(bank_valid)

        assert [True, True, True, True, True, True, True, True] == bank_return
    
    def test_start_bank_generic(self):
        bank_valid = BankValidate(bank_code='987').start()
        
        assert bank_valid == True
    
    def test_start_bank_invalid(self):
        with self.assertRaises(Exception):
            BankValidate('***').start()
