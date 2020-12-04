def first():

    bld_price = float(input("Build price:"))
    sel_price = float(input("Sell price:"))
    num_volume = int(input("Volume of sells:"))

    def calculate(build_price, sell_price, volume):
        diffrence = 0
        diffrence = sell_price - build_price
        return diffrence * volume

    print(calculate(bld_price,sel_price,num_volume))

def second():
    tms_day = int(input("How many times a day do you wash your hands:"))
    n_mnth = int(input("For how many months do you want a calculation"))

    def wash_hands(n, months):
        sec_day = 21*n
        sec_calc = sec_day * months * 30
        return sec_calc / 60

    print(wash_hands(tms_day,n_mnth))