exceptions = [ZeroDivisionError(), FileNotFoundError(), NameError()]
num_zd_errors = num_fnf_errors = num_name_errors = 0

# Si estuvieramos en la versión 3.11 de Python, se dispararían
# los 3 erorres en la variable 'exceptions'
try:
    raise ExceptionGroup("Errors Occurred", exceptions)
except ZeroDivisionError:
# except* ZeroDivisionError: ! Version de Python >= 3.11
    num_zd_errors += 1
except FileNotFoundError:
# except* FileNotFoundError:
    num_fnf_errors += 1
except NameError:
# except* NameError:
    num_name_errors += 1
finally:
    print(f"ZeroDivisionError was raised {num_zd_errors} times.")
    print(f"FileNotFoundError was raised {num_fnf_errors} times.")
    print(f"NameError was raised {num_name_errors} times.")