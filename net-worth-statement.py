from prettytable import PrettyTable

def calculate_liquid_assets() -> int:
    """Easily accessible sources of cash"""

    print('$ Liquid Assets $')

    liquid_assets = int(input('- Cash in hand: '))
    liquid_assets += int(input('- Cash held in current account: '))
    liquid_assets += int(input('- Cash value of life insurance: '))
    liquid_assets += int(input('- Money market funds: '))
    liquid_assets += int(input('- Certificates of deposit: '))
    liquid_assets += int(input('- Short-term investments: '))

    print('')

    return liquid_assets

def calculate_investment_assets() -> int:
    """Convertible to cash in the short or long term"""

    print('$ Investment Assets $')

    investment_assets = int(input('- Term deposits held at the bank: '))
    investment_assets += int(input('- Securities, stocks, shares, or bonds: '))
    investment_assets += int(input('- Investment real estate: '))
    investment_assets += int(input('- Endowment policies: '))
    investment_assets += int(input('- Retirement funds: '))

    print('')

    return investment_assets

def calculate_personal_assets() -> int:
    """Can be sold for cash but may take time"""

    print('$ Personal Assets $')

    personal_assets = int(input('- Home, which can be sold if downsizing: '))
    personal_assets += int(input('- Additional property such as a vacation home: '))
    personal_assets += int(input('- Art, jewelry, and other valuables: '))
    personal_assets += int(input('- Furniture, especially collectable pieces: '))
    personal_assets += int(input('- Vehicles (although they lose value quickly): '))

    print('')

    return personal_assets

def calculate_assets() -> int:
    liquid_assets = calculate_liquid_assets()
    investment_assets = calculate_investment_assets()
    personal_assets = calculate_personal_assets()
    assets = liquid_assets + investment_assets + personal_assets

    statement = PrettyTable(['Assets', assets])
    statement.add_row(['Liquid Assets', liquid_assets])
    statement.add_row(['Investment Assets', investment_assets])
    statement.add_row(['Personal Assets', personal_assets])

    print('$ Assets $')
    print(statement, end='\n\n')

    return assets

def calculate_short_term_liabilities() -> int:
    """Payable within the next 12 months"""

    print('$ Short-term Liabilities $')

    short_term_liabilities = int(input('- Credit card interest and capital repayments: '))
    short_term_liabilities += int(input('- Repayments on a personal or student loan: '))
    short_term_liabilities += int(input(
        '- Current monthly household bills (e.g., for utilities, communications, and insurance): '))
    short_term_liabilities += int(input('- Unpaid personal income tax for the year: '))

    print('')

    return short_term_liabilities

def calculate_long_term_liabilities() -> int:
    """Payable over more than 12 months"""

    print('$ Long-term Liabilities $')

    long_term_liabilities = int(input('- Mortgage or rental payments: '))
    long_term_liabilities += int(input('- Child support or alimony if separated or divorced: '))
    long_term_liabilities += int(input('- Children’s education through to college: '))
    long_term_liabilities += int(input('- Payments to a pension fund: '))
    long_term_liabilities += int(input('- A hire-purchase contract or lease for a car: '))

    print('')

    return long_term_liabilities

def calculate_contingent_liabilities() -> int:
    """May be owed in the future"""

    print('$ Contingent Liabilities $')

    contingent_liabilities = int(input('- Taxes such as capital gains: '))
    contingent_liabilities += int(input(
        '- Car or other loan guarantees for children who may fail to pay: '))
    contingent_liabilities += int(input('- Damage claims such as lawsuits: '))
    contingent_liabilities += int(input('- Attorney fees for personal legal disputes: '))

    print('')

    return contingent_liabilities

def calculate_debts() -> int:
    short_term_liabilities = calculate_short_term_liabilities()
    long_term_liabilities = calculate_long_term_liabilities()
    contingent_liabilities = calculate_contingent_liabilities()
    debts = short_term_liabilities + long_term_liabilities + contingent_liabilities

    statement = PrettyTable(['Debts', debts])
    statement.add_row(['Short-term Liabilities', short_term_liabilities])
    statement.add_row(['Long-term Liabilities', long_term_liabilities])
    statement.add_row(['Contingent Liabilities', contingent_liabilities])

    print('$ Debts $')
    print(statement, end='\n\n')

    return debts

def calculate_net_worth():
    """Individuals can calculate their net worth at any given time
    by subtracting debts from assets"""

    assets = calculate_assets()
    debts = calculate_debts()
    net_worth = assets - debts

    statement = PrettyTable(['Net Worth', net_worth])
    statement.add_row(['Assets', assets])
    statement.add_row(['Debts', debts])

    print('$ Net Worth $')
    print(statement)

if __name__ == '__main__':
    calculate_net_worth()
