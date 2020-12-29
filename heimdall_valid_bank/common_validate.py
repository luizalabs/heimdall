import re
class CommonValidate:
    @staticmethod
    def agency_is_valid(agency):
        """
            validates the bank agency pattern
        """
        regex = re.compile('^(?!0000)([0-9]{4})$', re.I)
        return bool(regex.match(agency))

    @staticmethod
    def agency_digit_is_valid(agency_digit):
        """
            validates the pattern of the bank agency digit
        """
        regex = re.compile('^[a-zA-Z0-9]{0,1}$', re.I)
        return bool(regex.match(agency_digit))

    @staticmethod
    def account_is_valid(account):
        """
            validates the pattern of the bank account
        """
        regex = re.compile('^[0-9]{1,12}$', re.I)
        return bool(regex.match(account))

    @staticmethod
    def account_digit_is_valid(account_digit):
        """
            validates the pattern of the bank account digit
        """
        regex = re.compile('^[a-zA-Z0-9]{1}$', re.I)
        return bool(regex.match(account_digit))
