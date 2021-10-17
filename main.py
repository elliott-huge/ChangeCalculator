import ChangeCalculator

def main():
    change_required = 1.03
    available_denominations = [[0.03, 0.9], [0.10, 3], [0.12, 6], [0.02, 0.5], [0.50, 3]]
    result = ChangeCalculator.exactChange(change_required, available_denominations)
    

if __name__ == '__main__':
    main()
