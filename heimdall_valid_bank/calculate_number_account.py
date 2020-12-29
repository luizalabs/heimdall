class CalculateAccount:
    def __init__(self, **kwargs):
        self.account = kwargs.get('account')
        self.agency = kwargs.get('agency')

    def calculate_account_bb(self):
        """
            Calcula o dígito verificador da conta do Banco do Brasil
        """
        numbers = [number for number in self.account]
        sumSeq = 0

        for i in range(len(numbers)):
            seq = 9 - int(i)
            sumSeq += (int(numbers[i]) * seq)

        return Modules().module_bb(sumSeq)

    def calculate_account_banrisul(self):
        """
            Calcula o dígito verificador da conta do Banrisul
        """
        numbers = [number for number in self.account]
        sumSeq = 0

        for i in range(len(numbers)):
            weight = [3, 2, 4, 7, 6, 5, 4, 3, 2]
            number = int(numbers[i])
            sumSeq += (number * weight[i])

        return Modules().module_eleven(sumSeq)

    def calculate_account_bradesco(self):
        """
            Calcula o dígito verificador da conta do Bradesco
        """
        if len(self.account) > 7:
            return False
        
        numbers = [number for number in self.account]

        sumSeq = 0
        for i in range(len(numbers)):
            weight = [2, 7, 6, 5, 4, 3, 2]
            number = int(numbers[i])
            sumSeq += (number * weight[i])

        return Modules().module_bradesco_account(sumSeq)

    def calculate_account_itau(self):
        """
            Calcula o dígito verificador da conta do Itau
        """
        numbers = [number for number in self.account]
        sumSeq = 0
        sequence = 0

        for i in range(len(numbers)):
            number = int(numbers[i])
            sequence = number * (2 if i % 2 == 0 else 1)
            sequence = CalculateAccount._adjust_according_length(sequence)
            sumSeq += sequence

        return Modules().module_itau(sumSeq)

    def calculate_account_santander(self):
        """
            Calcula o dígito verificador da conta do banco Santander
        """
        relevant_data = self.agency + '00' + self.account
        pivot = '97310097131973'
        values = [int(x) * int(y) for x, y in zip(relevant_data.zfill(len(pivot)), pivot)]

        result = sum(values)
        result = 10 - (result % 10)

        return '0' if result == 10 else str(result)

    def calculate_account_citibank(self):
        """
            Calcula o dígito verificador da conta do banco Citibank
        """
        if len(self.account) < 10:
            self.account = '%10d' % int(self.account)

        numbers = [number for number in self.account]
        sumSeq = 0
        for i in range(len(numbers)):
            weight = [10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
            number = int(numbers[i])
            sumSeq += (number * weight[i])

        return Modules().module_citibank(sumSeq)

    def calculate_account_caixa(self):
        """
            Calcula o dígito verificador de uma conta da Caixa Econômica Federal
        """
        pivot = '876543298765432'
        relevant_data = self.agency + self.account
        dv = sum([int(x) * int(y) for x, y in zip(relevant_data.zfill(len(pivot)), pivot)])
        dv *= 10
        dv %= 11
        return '0' if dv == 10 else str(dv)

    def calculate_account_nubank(self):
        """
            Calcula o dígito verificador de uma conta Nu Pagamentos (Nubank)
        """
        inverter_index_table = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                         [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
                         [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
                         [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
                         [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
                         [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
                         [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
                         [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
                         [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
                         [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]

        inverter_locate_table = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                   [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
                   [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
                   [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
                   [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
                   [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
                   [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
                   [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]

        account_with_zero = str(self.account) + '0'

        reversed_identify_code = tuple(int(n) for n in reversed(str(account_with_zero)))
        verificator_index = 0
        for i, n in enumerate(reversed_identify_code):
            verificator_index = inverter_index_table[verificator_index][inverter_locate_table[i % 8][n]]

        check_digit = inverter_index_table[verificator_index].index(0)

        return str(check_digit)

    @staticmethod
    def _adjust_according_length(sequence):
        if sequence > 9:
            numbers_sequence = []

            for number in list(str(sequence)):
                numbers_sequence.append(number)
            
            sequence = 0
            
            for i in range(len(numbers_sequence)):
                sequence += int(numbers_sequence[i])
        
        return sequence

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
    def module_eleven(sumSeq):
        module = sumSeq % 11
        if module == 0:
            return '0'

        if module == 1:
            return '6'

        return str(11 - module)

    @staticmethod
    def module_bradesco_account(sumSeq):
        module = sumSeq % 11
        if module == 0:
            return '0'

        if module == 1:
            return 'P'

        return str(int((11 - module)))

    @staticmethod
    def module_citibank(sumSeq):
        module = sumSeq % 11
        if module == 0:
            return '0'

        return str(int(11 - module))

    @staticmethod
    def module_itau(sumSeq):
        module = sumSeq % 10
        if module == 0:
            return '0'

        return str((10 - module))
