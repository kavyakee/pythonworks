while True:
    try:
        x=int(input("enter the number"))
        y=int(input("enter the number"))
        z=x/y
        print(z)
        break
    except:
        print("plz enter the valid number")



while True:
    try:
        x=int(input("enter the number"))
        y=int(input("enter the number"))
        z=x/y
        print(z)
        break
    except ZeroDivisionError:
        print(" zero cnt be divided")
    except TypeError:
        print("enter crct vlue")
    except ValueError:
        print("enter a valid number")
    finally:
        print("tq")



while True:
    try:
        x= int(input("enter the number"))
        if x%2==0:
            print("x is an even number")
            break
        else:
            print(" x is n ot an even no")
    except TypeError:
        print("enter crrct value")
    except ValueError:
        print("enter a valid number")
    finally:
        print("tq")




