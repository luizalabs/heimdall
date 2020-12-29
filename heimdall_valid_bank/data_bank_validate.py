import re
from heimdall_valid_bank.bank_validate import BankValidate
from heimdall_valid_bank.agency_validate import AgencyValidate
from heimdall_valid_bank.account_validate import AccountValidate
from heimdall_valid_bank.base_validate_error import InvalidAgencyNumber

class DataBankValidate():
    """ 
        This class is responsible for validating bank details 
        
        Attributes: 
            bank_code (string): Bank code, usually 3 digits ex.: 001. 
            agency (string): Agency number with or without the digit ex.: 2345-9, 2345.
            digit_agency (String): Digit of the agency, if passed with the agency it is not necessary to inform the digit here.
            account (string): Account number with or without the digit, for example: 12345678-9, 12345678.
            digit_account (string): Account type if it exists, however, if informed with the account there is no need to inform it again.
    """
    def __init__(self, **kwargs):
        self.bank_code = kwargs.get('bank_code')
        self.agency = kwargs.get('agency')
        self.account = kwargs.get('account')
        self.digit_agency = kwargs.get('digit_agency')
        self.digit_account = kwargs.get('digit_account')
       
    def start(self):
        try:
            regex_agency = re.match('^[0-9]{1,4}(-[0-9a-zA-Z]{1,2})?$', self.agency)
            if not regex_agency:
                raise InvalidAgencyNumber()
            
            if  len(self.agency) > 4:
                agency = re.sub('[^A-Za-z0-9]+', '', self.agency)
                self.agency = agency[0:4]
                self.digit_agency = agency[4:len(agency)]
            
            regex_account = re.search('[@_!#$%^&*()<>?/\-.|}{~:]', self.account)
            if regex_account:
                self.digit_account = self.account[regex_account.start() + 1:len(self.account)]
                self.account = self.account[0:regex_account.start()]
            
            if self.__valid_bank():
                if self.__valid_agency():
                    return self.__valid_account()

        except Exception as ex:
            return False

    def __valid_bank(self):
        """
            valida o banco
        """
        return BankValidate(
            bank_code=self.bank_code
        ).start()
  
    def __valid_agency(self):
        """
            valida a agencia + digito agencia
        """
        return AgencyValidate(
            bank_code=self.bank_code,
            agency=self.agency,
            digit_agency=self.digit_agency
        ).start()

    def __valid_account(self):
        """
            valida a conta + digito conta
        """
        return AccountValidate(
            bank_code=self.bank_code,
            agency=self.agency,
            digit_agency=self.digit_agency,
            account=self.account,
            digit_account=self.digit_account
        ).start()