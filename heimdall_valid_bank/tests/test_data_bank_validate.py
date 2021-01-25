from unittest import TestCase
from heimdall_valid_bank.data_bank_validate import DataBankValidate


class TestDataBankValidate(TestCase):
    def test_start_account_validate(self):
        banks_valids = {
            '001': {
                'agency': '1584',
                'digit_agency': '9',
                'account': '00210169',
                'digit_account': '6'
            },
            '041': {
                'agency': '2664',
                'digit_agency': '18',
                'account': '358507671',
                'digit_account': '8'
            },
            '237': {
                'agency': '2377',
                'digit_agency': '9',
                'account': '02380691',
                'digit_account': '2'
            },
            '341': {
                'agency': '2545',
                'account': '023661111',
                'digit_account': '1'
            },
            '033': {
                'agency': '2006',
                'account': '0100840711',
                'digit_account': '4'
            },
            '745': {
                'agency': '0075',
                'account': '0007500465',
                'digit_account': '8'
            },
            '104': {
                'agency': '3009',
                'account': '001000004484357',
                'digit_account': '6'
            },
            '260': {
                'agency': '0001',
                'account': '9234876483020',
                'digit_account': '7'
            }
        }
        return_account_valid = []
        for bank in banks_valids:
            account_valid = DataBankValidate(
                bank_code=bank,
                agency=banks_valids[bank]['agency'],
                digit_agency=banks_valids[bank].get('digit_agency'),
                account=banks_valids[bank]['account'],
                digit_account=banks_valids[bank].get('digit_account')
            ).start()

            return_account_valid.append(account_valid)

        assert [True, True, False, False, False, True, False, False] == return_account_valid
