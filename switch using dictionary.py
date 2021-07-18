def switch_demo(a):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4:"April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher[a]
n=int(input ("Enter a number:"))
print (switch_demo(n))