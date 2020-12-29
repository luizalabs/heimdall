import re
from heimdall_bank_validate.bank_validate import BankValidate
from heimdall_bank_validate.agency_validate import AgencyValidate
from heimdall_bank_validate.account_validate import AccountValidate

class DataBankValidate():
    def __init__(self, **kwargs):
        self.bank_code = kwargs.get('bank_code')
        self.agency = kwargs.get('agency')
        self.account = kwargs.get('account')
        
        if len(self.agency) > 4:
            agency = re.sub('[^A-Za-z0-9]+', '', self.agency)
            self.agency = agency[0:4]
            self.digit_agency = agency[4:len(agency)]

        regex = re.search('[@_!#$%^&*()<>?/\-.|}{~:]', self.account)
        if regex:
            self.digit_account = self.account[regex.start()+1:len(self.account)]
        
        self.digit_agency = kwargs.get('digit_agency')
        self.digit_account = kwargs.get('digit_account')
       
    def start(self):
        try:
            if DataBankValidate._valid_bank(self.bank_code):
                if DataBankValidate._valid_agency(self.bank_code, self.agency, self.digit_agency):
                    return DataBankValidate._valid_account(self.bank_code, self.agency, self.digit_agency, self.account, self.digit_account)

        except Exception as ex:
            print(ex)
            return False

    @staticmethod
    def _valid_bank(bank_code):
        """
            valida o banco
        """
        return BankValidate(
            bank_code=bank_code
        ).start()


    @staticmethod
    def _valid_agency(bank_code, agency, digit_agency):
        """
            valida a agencia + digito agencia
        """
        return AgencyValidate(
            bank_code=bank_code,
            agency=agency,
            digit_agency=digit_agency
        ).start()

    @staticmethod
    def _valid_account(bank_code, agency, digit_agency, account, digit_account):
        """
            valida a conta + digito conta
        """
        return AccountValidate(
            bank_code=bank_code,
            agency=agency,
            digit_agency=digit_agency,
            account=account,
            digit_account=digit_account
        ).start()
