c = 1002000
b = str(c)
parameter = 0

coin = "${:,.2f}".format(c).replace(",","n").replace(".",",").replace("n",".")

num_separated = [a for a in b]

if len(num_separated) <= 6:
    ref = "pesos"
else:
    num_lim = num_separated[-6:]

    for a in range(len(num_lim)):
        parameter = parameter + int(num_lim[a])

    if parameter == 0:
        ref = "de pesos"
    else:
        ref = "pesos"

print(coin)
print(ref)