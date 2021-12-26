def has_fee(T: list) -> bool:
    '''Return weather a list of transaction gives fees discount or not.'''

    if len(T) >= 3 and abs(sum(T)) >= 100:
        return False
    return True


def get_card_fees(B: dict) -> int:
    '''Return the card fees amount for a year.'''
    amnt = 0
    for month in B:
        if has_fee(B[month]):
            amnt += 5
    return amnt


def outcoms(T: list) -> dict:
    '''Return outcoms per month.
    
    T: list of tuples (date, transaction) representing a year of 
    bank transactions.
    '''
    B = {}
    for trans in T:
        entry = B.setdefault(trans[0][5:7], [])
        amnt = trans[1]
        if amnt < 0:
            entry.append(amnt)
    return B


def solution(A: list, D: list):
    '''Return the balance of bank account based on given transactions.
    
    A: list of amount of the transaction (positive for incoms and negative fo outcoms)
    D: list of transaction dates
    '''
    balance = sum(A)
    withdraws = outcoms(list(zip(D,A)))
    card_fees = get_card_fees(withdraws) + ((12 - len(withdraws.keys())) * 5)
    return balance - card_fees


if __name__ == '__main__':
    print(solution([100,100,100,-10], ['2020-12-31', '2020-12-22', '2020-12-03', '2020-12-29']))
