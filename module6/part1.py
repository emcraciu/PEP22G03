import time

x = 2

try:
    time.sleep(10)
    for i in range(x):
        if i == 0:
            raise ArithmeticError
        print(1/(-1 + i))


except ZeroDivisionError:

    print("Divizia cu 0 nepermisa.")

except ArithmeticError:
    print("Other math error")
    time.sleep(10)


except Exception:
    print('Something else happend')

except:
    print("All other error")

