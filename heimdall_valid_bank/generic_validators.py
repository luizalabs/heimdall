import re
from heimdall_valid_bank.base_validate_error import InvalidAgencyNumber, InvalidDigitAgencyNumber, InvalidAccountNumber, \
    InvalidDigitAccountNumber


class GenericValidators:
    @staticmethod
    def agency_is_valid(agency):
        regex = re.compile('^[0-9]{1,5}$', re.I)
        match = bool(regex.match(agency))

        if not match:
            raise InvalidAgencyNumber()

        return True

    @staticmethod
    def agency_digit_is_valid(digit_agency):
        regex = re.compile('^[a-zA-Z0-9]{0,2}$', re.I)
        match = bool(regex.match(digit_agency))

        if not match:
            raise InvalidDigitAgencyNumber()

        return True

    @staticmethod
    def account_is_valid(account):
        regex = re.compile('^[0-9]{1,12}$', re.I)
        match = bool(regex.match(account))

        if not match:
            raise InvalidAccountNumber()

        return True

    @staticmethod
    def account_digit_is_valid(digit_account):
        regex = re.compile('^[a-zA-Z0-9]{0,2}$', re.I)
        match = bool(regex.match(digit_account))

        if not match:
            raise InvalidDigitAccountNumber()

        return True
