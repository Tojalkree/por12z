print("1 - km, 2 - m, 3 - cm, 4 - mm, 5 - mi, 6 - yd")

src = input("Source unit (1-6): ")
dst = input("Target unit (1-6): ")
value = float(input("Value: "))

if src == "1":
    k_src, n_src = 1000.0, "km"
elif src == "2":
    k_src, n_src = 1.0, "m"
elif src == "3":
    k_src, n_src = 0.01, "cm"
elif src == "4":
    k_src, n_src = 0.001, "mm"
elif src == "5":
    k_src, n_src = 1609.344, "mi"
else:
    k_src, n_src = 0.9144, "yd"

if dst == "1":
    k_dst, n_dst = 1000.0, "km"
elif dst == "2":
    k_dst, n_dst = 1.0, "m"
elif dst == "3":
    k_dst, n_dst = 0.01, "cm"
elif dst == "4":
    k_dst, n_dst = 0.001, "mm"
elif dst == "5":
    k_dst, n_dst = 1609.344, "mi"
else:
    k_dst, n_dst = 0.9144, "yd"

result = value * k_src / k_dst
print(f"{value} {n_src} = {result:.4f} {n_dst}")