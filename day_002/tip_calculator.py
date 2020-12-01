
def main():
    """
    Splitting payment calculator
    """
    print('Welcome to tip calculator.')

    total_bill = float(input('What was the total bill? $'))
    percentage_tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
    people_to_split = int(input('How many people to split the bill? '))

    total_pay = total_bill * (1 + (percentage_tip / 100))
    per_payment = round(total_pay / people_to_split, 2)

    print(f'Each person should pay: ${per_payment}')


if __name__ == '__main__':
    main()
