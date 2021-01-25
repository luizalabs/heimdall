from unittest import TestCase
from heimdall_valid_bank.account_validate import AccountValidate


class TestAccountValidate(TestCase):
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
                'account': '0238069',
                'digit_account': '2'
            },
            '341': {
                'agency': '2545',
                'account': '02366',
                'digit_account': '1'
            },
            '033': {
                'agency': '2006',
                'account': '01008407',
                'digit_account': '4'
            },
            '745': {
                'agency': '0075',
                'account': '0007500465',
                'digit_account': '8'
            },
            '104': {
                'agency': '3009',
                'account': '00100000448',
                'digit_account': '6'
            },
            '260': {
                'agency': '0001',
                'account': '9234876',
                'digit_account': '7'
            }
        }
        return_account_valid = []
        for bank in banks_valids:
            account_valid = AccountValidate(
                bank_code=bank,
                agency=banks_valids[bank]['agency'],
                digit_agency=banks_valids[bank].get('digit_agency'),
                account=banks_valids[bank]['account'],
                digit_account=banks_valids[bank].get('digit_account')
            ).start()

            return_account_valid.append(account_valid)

        assert len(return_account_valid) > 0

    def test_start_account_validate_santander(self):
        bank_code = '033'
        bank_agency = '4442'
        account = '01090717-7'
        account_is_valid = AccountValidate(
            bank_code=bank_code,
            agency=bank_agency,
            account=account
        ).start()

        assert account_is_valid is True

    def test_start_account_validate_caixa(self):
        bank_code = '104'
        bank_agency = '2004'
        account = '00100000448-6'
        account_is_valid = AccountValidate(
            bank_code=bank_code,
            agency=bank_agency,
            account=account
        ).start()

        assert account_is_valid is True

    def test_start_account_validate_false_bradesco(self):
        bank_code = '237'
        bank_agency = '3890-3'
        account = '9658-5'
        account_is_valid = AccountValidate(
            bank_code=bank_code,
            agency=bank_agency,
            account=account
        ).start()

        assert account_is_valid is False

    def test_start_account_validate_true_bradesco(self):
        bank_code = '237'
        bank_agency = '3890-3'
        account = '0004307-9'
        account_is_valid = AccountValidate(
            bank_code=bank_code,
            agency=bank_agency,
            account=account
        ).start()

        assert account_is_valid is True

    def test_start_account_validate_true_bradesco_without_digit_separator(self):
        bank_code = '237'
        bank_agency = '3890-3'
        account = '00043079'
        account_is_valid = AccountValidate(
            bank_code=bank_code,
            agency=bank_agency,
            account=account
        ).start()

        assert account_is_valid is True

    def test_start_account_validate_banrisul(self):
        bank_code = '041'
        bank_agency = '2664-18'
        account = '358507671-8'
        account_is_valid = AccountValidate(
            bank_code=bank_code,
            agency=bank_agency,
            account=account,
        ).start()

        assert account_is_valid is True

    def test_start_account_validate_nubank(self):
        bank_code = '260'
        bank_agency = '0001'
        account = '7956865-6'
        account_is_valid = AccountValidate(
            bank_code=bank_code,
            agency=bank_agency,
            account=account
        ).start()

        assert account_is_valid is True

    def test_start_account_validate_itau_with_blank_digit_separator(self):
        bank_code = '341'
        bank_agency = '2545'
        account = '02366-1'
        account_is_valid = AccountValidate(
            bank_code=bank_code,
            agency=bank_agency,
            account=account
        ).start()

        assert account_is_valid is True

    def test_start_account_validate_itau_without_blank_digit_separator(self):
        bank_code = '341'
        bank_agency = '2545'
        account = '023661'
        account_is_valid = AccountValidate(
            bank_code=bank_code,
            agency=bank_agency,
            account=account
        ).start()

        assert account_is_valid is True

    def test_start_account_validate_generic_with_only_zeros(self):
        bank_code = '399'
        bank_agency = '1234'
        account = '000000'
        account_is_valid = AccountValidate(
            bank_code=bank_code,
            agency=bank_agency,
            account=account
        ).start()

        assert account_is_valid is False

    def test_start_account_validate_generic_with_only_zeros_and_valid_digit(self):
        bank_code = '399'
        bank_agency = '1234'
        account = '000000-12'
        account_is_valid = AccountValidate(
            bank_code=bank_code,
            agency=bank_agency,
            account=account
        ).start()

        assert account_is_valid is False

    def test_start_account_validate_generic_with_not_only_zeros(self):
        bank_code = '399'
        bank_agency = '1234'
        account = '00001'
        account_is_valid = AccountValidate(
            bank_code=bank_code,
            agency=bank_agency,
            account=account
        ).start()

        assert account_is_valid is True
