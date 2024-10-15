v = float(input())
if v <=0:
    print("фантазёр")
elif v <= 7.8:
    print("ты упал")
elif 7.8 < v < 11.2:
    print("ты спутник Земли")
elif 11.2 <= v <= 16.4:
    print("ты спутник Солнца")
elif v >= 16.4:
    print("ты улетел от нас")