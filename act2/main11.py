#exceptions Try -> Except -> Finally
try: 
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You cant divide by zero ")
except ValueError:
    print("Only numbers expected")
except Exception:
    print("Something went wrong")
finally:
    print("Do some cleanup here")   