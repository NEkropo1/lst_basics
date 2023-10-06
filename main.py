def dark_elven_fighter(number: int=0):
    def inner(func):
        print(f"func {func} is being decorated")
        def wrapper(*args, **kwargs):
            print(f'fubction {func} is badass')
            for i in range(number):
                print(i + 1)
            return func(*args, **kwargs)
        return wrapper
    return inner


@dark_elven_fighter(3)
def printer(name: str="Vasya"):
    return f'Helllo {name}'


print(printer("hfhffjjf"))
