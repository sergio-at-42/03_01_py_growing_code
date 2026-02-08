def ft_count_harvest_recursive():
    def ft_print_day(day):
        if day > 1:
            ft_print_day(day - 1)
        print("Day ", day)
    nb_days = int(input("Days until harvest: "))
    ft_print_day(nb_days)
    print("Harvest time!")
