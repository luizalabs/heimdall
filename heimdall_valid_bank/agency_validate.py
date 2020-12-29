import re
from heimdall_valid_bank.utils.constants import GenericVariables
from heimdall_valid_bank.base_validate_error import (InvalidAgencyNumber, InvalidDigitAgencyNumber)
from heimdall_valid_bank.calculate_number_agency import CalculateAgency
from heimdall_valid_bank.common_validate import CommonValidate
from heimdall_valid_bank.generic_validators import GenericValidators

class AgencyValidate(CommonValidate):
    """ 
        This class is responsible for validating the bank agency number
        
        Attributes: 
            bank_code (string): Bank code, usually 3 digits ex.: 001. 
            agency (string): Agency number with or without the digit ex.: 2345-9, 2345.
            digit_agency (String): Digit of the agency, if passed with the agency it is not necessary to inform the digit here.
    """
    
    def __init__(self, **kwargs):
        self.bank_code = kwargs.get('bank_code')
        self.agency = kwargs.get('agency')
        self.digit_agency = kwargs.get('digit_agency')

    def start(self):
        try:
            regex = re.match('^[0-9]{1,4}(-[0-9a-zA-Z]{1,2})?$', self.agency)
            if not regex:
                raise InvalidAgencyNumber()
            
            if  len(self.agency) > 4:
                agency = re.sub('[^A-Za-z0-9]+', '', self.agency)
                self.agency = agency[0:4]
                self.digit_agency = agency[4:len(agency)]
            
            if self.bank_code not in GenericVariables.LIST_BANKS:
                return self.valid_agency_generic()
            
            switcher = {
                '001': self.valid_agency_bb,
                '237': self.valid_agency_bradesco,
                '341': self.valid_agency_itau,
                '033': self.valid_agency_santander,
                '745': self.valid_agency_citibank,
                '041': self.valid_agency_banrisul,
                '104': self.valid_agency_caixa,
                '260': self.valid_agency_nubank
            }

            return switcher.get(self.bank_code)()
        except Exception:
            return False

    def valid_agency_generic(self):
        """
          Valida agências genéricas
        """
        result = GenericValidators.agency_is_valid(self.agency)
        
        if self.digit_agency:
            result = GenericValidators.agency_digit_is_valid(self.digit_agency)

        return result

    def valid_agency_bb(self):
        """
           Valida a agência e o dígito verificador do banco do Brasil
           Tamanho da Agência - 4 Dígitos + 1 DV
        """
        agency_is_valid = super().agency_is_valid(self.agency)

        if not agency_is_valid:
            raise InvalidAgencyNumber()

        result_digit_agency_valid = super().agency_digit_is_valid(self.digit_agency)

        if not result_digit_agency_valid or len(self.digit_agency) != 1:
            raise InvalidDigitAgencyNumber()

        check_number_calculated_digit = CalculateAgency(self.agency).calculate_agency_bb()

        if not check_number_calculated_digit:
            raise InvalidAgencyNumber()
      
        return check_number_calculated_digit == self.digit_agency.upper()

    def valid_agency_banrisul(self):
        """
          Valida a agência e dígito verificador do banco Banrisul
          Tamanho da Agência - 4 Dígitos
        """
        result_agency_valid = super().agency_is_valid(self.agency)
        
        if not result_agency_valid:
            raise InvalidAgencyNumber()

        return True

    def valid_agency_bradesco(self):
        """
            Valida a agência e o dígito verificador do banco Bradesco
            Tamanho da Agência - 4 Dígitos + 2 DV
        """
        result_agency_valid = super().agency_is_valid(self.agency)
        
        if not result_agency_valid:
            raise InvalidAgencyNumber()
      
        result_digit_agency_valid = super().agency_digit_is_valid(self.digit_agency)
       
        if not result_digit_agency_valid:
            raise InvalidDigitAgencyNumber()

        check_number_calculated_agency = CalculateAgency(self.agency).calculate_agency_bradesco()
        if not check_number_calculated_agency:
            raise InvalidAgencyNumber()
        
        check_number_informed_digit = self.digit_agency.upper()
        if check_number_informed_digit == '0':
            return check_number_calculated_agency == check_number_informed_digit or check_number_calculated_agency == 'P'
        
        return check_number_calculated_agency == check_number_informed_digit

    def valid_agency_citibank(self):
        """
          Valida a agência do banco Citibank
          Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        result_agency_valid = super().agency_is_valid(self.agency)

        if not result_agency_valid:
            raise InvalidAgencyNumber()

        return True

    def valid_agency_itau(self):
        """
          Valida a agência do banco Itaú
          Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        result_agency_valid = super().agency_is_valid(self.agency)
        
        if not result_agency_valid:
            raise InvalidAgencyNumber()

        return True

    def valid_agency_santander(self):
        """
           Valida a agência do banco Santander
           Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        result_agency_valid = super().agency_is_valid(self.agency)

        if not result_agency_valid:
            raise InvalidAgencyNumber()

        return True

    def valid_agency_caixa(self):
        """
           Valida a agência do banco Caixa Econômica Federal
           Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        result_agency_valid = super().agency_is_valid(self.agency)

        if not result_agency_valid:
            raise InvalidAgencyNumber()

        return True

    def valid_agency_nubank(self):
        """
           Valida a agência do banco Nu Pagamentos (Nubank)
           Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        result_agency_valid = super().agency_is_valid(self.agency)

        if not result_agency_valid:
            raise InvalidAgencyNumber()
        
        return True
