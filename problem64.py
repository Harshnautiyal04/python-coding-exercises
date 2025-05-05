#  basic stufents marks 

marks = int(input("Enter marks : "))

if marks == 1100:
    print("Free Education.")
elif marks >1000:
    print("80% monthly fees deduction.")
elif marks > 900:
    print("60% monthly fees deduction.")
elif marks > 800:
    print("40% monthly fees deduction.")
elif marks > 700:
    print("30% monthly fees deduction.")
else:
    print("There is no scholorship.")