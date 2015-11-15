def loss_or_profit(income, outcome):
    income_sum = sum(income)
    outcome_sum = sum(outcome)

    if income_sum > outcome_sum:
        return "+" + str(income_sum - outcome_sum)
    if income_sum < outcome_sum:
        return "-" + str(outcome_sum - income_sum)
    if income_sum == outcome_sum:
        return "=0"


def main():
    print(loss_or_profit([10], [10]))
    print(loss_or_profit([10], [20, 30]))
    print(loss_or_profit([1, 2, 3], [3]))

if __name__ == '__main__':
    main()
