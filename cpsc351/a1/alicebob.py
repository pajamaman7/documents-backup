for i in range(0,15):
    bit=f"{i:04d}"
    bitstr = (bit)[2:6]
    b=2+int(bitstr[1])+int(bitstr[3])-(int(bitstr[0])+int(bitstr[2])
)
    print("&"+bitstr+"&b="+str(b) + "\\\\ ")
