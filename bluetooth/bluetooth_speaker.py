import bluetooth
nearby = bluetooth.discover_devices(lookup_names=True);
print(nearby[0][1])
corrAddr = None;
for ele in nearby:
    if 'Boxanne' == ele[1]:
        corrAddr = ele[0]
        break
if corrAddr is None:
    exit()
println("Found it!\n")
