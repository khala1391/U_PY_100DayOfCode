# try:
#     age = int(input("number:"))
# except Exception as ValueError:
#     print("error try again")
#     age = int(input("number"))

# print(age)

# ----------------------------------------------------


while True:
    try:
        numerator = 10
        denominator = int(input("Enter a non-zero denominator: "))
        result = numerator / denominator
        print("Result:", result)
        break  # Exit the loop if successful
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Try again.")
    except ValueError:
        print("Error: Please enter a valid integer. Try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Try again.")


try:
    pass
except Exception as e:
    raise e
else:
    pass

# ----------------------------------------------------
