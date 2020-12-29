from unittest import TestCase
from heimdall_valid_bank.calculate_number_agency import CalculateAgency
from heimdall_valid_bank.tests.data import BANCO_DO_BRASIL, BRADESCO

class TestCalculateAgency(TestCase):

    def test_calculate_agency_bb_valid(self):
        bank = BANCO_DO_BRASIL['valid_combinations']
        digits_calculated = []
        branchs_digit = []
        for i in range(len(bank)):
            calculate_agency = CalculateAgency(
                agency=bank[i]['branch']
            ).calculate_agency_bb()

            digits_calculated.append(calculate_agency)
            branchs_digit.append(bank[i]['branch_digit'])

        assert digits_calculated == branchs_digit

    def test_calculate_agency_bradesco_valid(self):
        bank = BRADESCO['valid_combinations']
        digits_calculated = []
        branchs_digit = []
        for i in range(len(bank)):
            calculate_agency = CalculateAgency(
                agency=bank[i]['branch']
            ).calculate_agency_bradesco()

            digits_calculated.append(calculate_agency)
            
            if bank[i]['branch_digit'] == '0' or bank[i]['branch_digit'] == 'P':
                bank[i]['branch_digit'] = calculate_agency
                
            branchs_digit.append(bank[i]['branch_digit'])

        assert digits_calculated == branchs_digit
