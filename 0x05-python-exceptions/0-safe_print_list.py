def safe_print_integer(value):
    if type(value) == int:
        print("{:d}".format(value))
        return True
    else:
         try:
             value = int(value)
         except ValueError:
            return False
         print(value)
         return True
