import ChangeCalculator

def main():
    change_required = 0.08
    available_denominations = [[0.05, 0.05], [0.04, 0.08], [0.01, 0.03]]
    result = ChangeCalculator.exactChange(change_required, available_denominations)
    

if __name__ == '__main__':
    main()
