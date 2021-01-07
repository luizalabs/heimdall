from unittest import TestCase
from heimdall_valid_bank.agency_validate import AgencyValidate


class TestAgencyValidate(TestCase):
    def test_start_agency_validate(self):
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
        return_agency_valid = []
        for bank in banks_valids:
            agency_valid = AgencyValidate(
                bank_code=bank,
                agency=banks_valids[bank]['agency'],
                digit_agency=banks_valids[bank].get('digit_agency')
            ).start()

            return_agency_valid.append(agency_valid)

        assert [True, True, True, True, True, True, True, True] == return_agency_valid

    def test_start_agency_validate_caixa_with_length_less_than_minimum(self):
        bank_code = '104'
        bank_agency = '2004'
        account = '123456'
        account_is_valid = AgencyValidate(
            bank_code=bank_code,
            agency=bank_agency,
            account=account
        ).start()

        assert account_is_valid is False

    def test_start_agency_validate_bradesco_with_blank_digit_separator(self):
        bank_code = '237'
        bank_agency = '3890-3'
        account_is_valid = AgencyValidate(
            bank_code=bank_code,
            agency=bank_agency
        ).start()

        assert account_is_valid is True

    def test_start_agency_validate_bradesco_without_blank_digit_separator(self):
        bank_code = '237'
        bank_agency = '38903'
        account_is_valid = AgencyValidate(
            bank_code=bank_code,
            agency=bank_agency
        ).start()

        assert account_is_valid is True

    def test_start_agency_validate_banrisul(self):
        bank_code = '041'
        bank_agency = '2664-18'
        account_is_valid = AgencyValidate(
            bank_code=bank_code,
            agency=bank_agency
        ).start()

        assert account_is_valid is True

    def test_start_agency_validate_generic_with_only_zeros_and_valid_digit(self):
        bank_code = '399'
        bank_agency = '0000-11'
        account_is_valid = AgencyValidate(
            bank_code=bank_code,
            agency=bank_agency
        ).start()

        assert account_is_valid is False

    def test_start_agency_validate_generic_with_only_zeros(self):
        bank_code = '399'
        bank_agency = '0000'
        account_is_valid = AgencyValidate(
            bank_code=bank_code,
            agency=bank_agency
        ).start()

        assert account_is_valid is False

    def test_start_agency_validate_generic_with_not_only_zeros(self):
        bank_code = '399'
        bank_agency = '0001'
        account_is_valid = AgencyValidate(
            bank_code=bank_code,
            agency=bank_agency
        ).start()

        assert account_is_valid is True
