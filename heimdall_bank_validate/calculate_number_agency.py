class CalculateAgency:
    def __init__(self, agency):
        self.agency = agency

    def calculate_agency_bb(self):
        """
            Calcula número da agência do Banco do Brasil
        """
        sumSeq = CalculateAgency.calculate_agency_generic(self.agency)
        return Modules().module_bb(sumSeq)

    def calculate_agency_bradesco(self):
        """
          Calcula número da agência do Bradesco
        """
        sumSeq = CalculateAgency.calculate_agency_generic( self.agency)
        return Modules().module_bradesco_agency(sumSeq)

    @staticmethod
    def calculate_agency_generic(agency):
        numbers = []
        for number in agency:
            numbers.append(number)

        sumSeq = 0

        for i in range(len(numbers)):
            seq = 5 - i
            sumSeq += (float(numbers[i]) * seq)

        return sumSeq

class Modules():
    @staticmethod
    def module_bb(sumSeq):
        result = 11 - (sumSeq % 11)
        if result == 10:
            return 'X'
        if result == 11:
            return '0'

        return str(int(result))

    @staticmethod
    def module_bradesco_agency(sumSeq):
        module = 11 - (sumSeq % 11)
        if module == 10:
            return 'P'

        if module == 11:
            return '0'

        return str(int(module))