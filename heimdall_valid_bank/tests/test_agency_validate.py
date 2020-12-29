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
