# exceptii

def create_fraction(number):

    try:
        # result = number / 1
        if number >= 0:
            result = 1 / number
        else:
            raise ValueError("Number is small, can't use it")
    except ZeroDivisionError:
        result = 'Infinit'
        print('Cant use 0 divider')
    except ValueError:
        raise
    except:
        result = 0
        print('This is an unknown Error')

    return result

print(create_fraction(3))
#print(create_fraction(-1))

print(create_fraction(0))
print('Done')