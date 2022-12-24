import time


def cal(bal):
    print("")
    required500 = bal // 500
    bal = bal - (required500 * 500)

    required100 = bal // 100
    bal = bal - (required100 * 100)

    required50 = bal // 50
    bal = bal - (required50 * 50)

    required20 = bal // 20
    bal = bal - (required20 * 20)

    required10 = bal // 10
    bal = bal - (required10 * 10)

    required5 = bal // 5
    bal = bal - (required5 * 5)

    required1 = bal // 1
    bal = bal - (required1 * 1)

    if required500 == 0:
        False
    else:
        print("500 x", required500)
    if required100 == 0:
        False
    else:
        print("100 x", required100)
    if required50 == 0:
        False
    else:
        print("50x :", required50)
    if required20 == 0:
        False
    else:
        print("20x :", required20)
    if required10 == 0:
        False
    else:
        print("10x :", required10)
    if required5 == 0:
        False
    else:
        print("5x :", required5)
    if required1 == 0:
        False
    else:
        print("1x :", required1)
    return "\nSECOND CALCULATION :"


while True:
    id = int(
        input(
            """
--------------------------------
1 | division and split
2 | split

Do you need 1 or 2? :"""
        )
    )
    if id == 1:
        startingfund = int(input("total number? :"))
        takeawayfund = int(input("takeaway fund? :"))
        startingfund = startingfund - takeawayfund
        print(cal(startingfund))
        cal(takeawayfund)

    elif id == 2:
        bal = int(input("how much money do you need? :"))
        cal(bal)
    else:
        print("unrecognised input...")
