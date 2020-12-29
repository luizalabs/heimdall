## Heimdall

> Heimdall is the guardian of the rainbow bridge, which is the onlu way to Asgard (heaven) bouding with Midgard (earth) os nordic mithology, for this project Heimdall is responsible for not letting invalid bank data to be accepted.

![image](https://github.com/thaisribeiro/Heimdall/blob/c5bde46bbcad0a25061179241f0edee2248273be/heimdall%2Fimage%2Fheimdall.png)

## Bank Account Validate

Heimdall is a Python package which validates the main brazilian banks: Itaú, Bradesco, Caixa, Banco do Brasil, Citibank, Santander, Banrisul and Nubank.
For the remaining ones it is used a default validation:
* Agency is required to have 1 up to 5 digits
* Agency Branch is required to have 0 up to 2 characters
* Account is required to have 1 up to 12 digits
* Account Branch is required to have 0 up to 2 characters
## Basic Usage

Install with pip:

```
pip install wheel && pip install heimdall_valid_bank
```

To validate the entire bank account, follow these steps:


``` {.sourceCode .python}
from heimdall_valid_bank.data_bank_validate import DataBankValidate

valid_bank = DataBankValidate(
                bank_code='001',
                agency='1584',
                digit_agency='9',
                account='00210169',
                digit_account='6'
            ).start()

if valid_bank == True:
    print('Bank Valid')
else:
    print('Bank Invalid')

```
You can also validate in stages, using `BankValidate`, `AgencyValidate`, `AccountValidate`,:
### Examples:

* basic agency validation:
  
``` {.sourceCode .python}
from heimdall_valid_bank.agency_validate import AgencyValidate

valid_bank = AgencyValidate(
                bank_code='237',
                agency='2377-8'
            ).start()

if valid_bank == True:
    print('Agency Valid')
else:
    print('Agency Invalid')

```

* validation with agency branch
  
``` {.sourceCode .python}
from heimdall_valid_bank.agency_validate import AgencyValidate

valid_bank = AgencyValidate(
                bank_code='001',
                agency='1584',
                digit_agency='9'
            ).start()

if valid_bank == True:
    print('Agency Valid')
else:
    print('Agency Invalid')

```

* agency validation by passing the branch directly at the agency, if you have:
  
``` {.sourceCode .python}
from heimdall_valid_bank.agency_validate import AgencyValidate

valid_bank = AgencyValidate(
                bank_code='001',
                agency='1584-9'
            ).start()

if valid_bank == True:
    print('Agency Valid')
else:
    print('Agency Invalid')

```

## License
Heimdall is released under the MIT license. See the bundled
[LICENSE](https://github.com/thaisribeiro/Heimdall/blob/783f3f3dfdd34cedc220128618582ec1e3d71303/LICENSE) file for details.

## Credits

- [Thais Ribeiro](https://github.com/thaisribeiro)
- [Bruna Baleste](https://github.com/BrunaBritoBaleste)
