def encode(text):
    global encoded
    encoded = ""
    for i in text:
        if i=="A" or  i=="a":
            encoded = str(encoded) + str(10)
        elif i=="B" or i=="b":
            encoded = str(encoded) + str(11)
        elif i=="C" or i=="c":                                   
            encoded = str(encoded) + str(12)    
        elif i=="D" or i=="d":                                   
            encoded = str(encoded) + str(13)
        elif i=="E" or i=="e":                                   
            encoded = str(encoded) + str(14)
        elif i=="F" or i=="f":                                   
            encoded = str(encoded) + str(15)
        elif i=="G" or i=="g":
            encoded = str(encoded) + str(16)
        elif i=="H" or i=="h":                                   
            encoded = str(encoded) + str(17)
        elif i=="I" or i=="i":                                   
            encoded = str(encoded) + str(18)
        elif i=="J" or i=="j":                                   
            encoded = str(encoded) + str(19)
        elif i=="K" or i=="k":                                   
            encoded = str(encoded) + str(20)
        elif i=="L" or i=="l":                                   
            encoded = str(encoded) + str(21)
        elif i=="M" or i=="m":                                   
            encoded = str(encoded) + str(22)
        elif i=="N" or i=="n":                                   
            encoded = str(encoded) + str(23)
        elif i=="O" or i=="o":                                   
            encoded = str(encoded) + str(24)
        elif i=="P" or i=="p":                                   
            encoded = str(encoded) + str(25)
        elif i=="Q" or i=="q":                                   
            encoded = str(encoded) + str(26)
        elif i=="R" or i=="r":                                   
            encoded = str(encoded) + str(27)
        elif i=="S" or i=="s":                                   
            encoded = str(encoded) + str(28)
        elif i=="T" or i=="t":                                   
            encoded = str(encoded) + str(29)
        elif i=="U" or i=="u":                                   
            encoded = str(encoded) + str(30)
        elif i=="V" or i=="v":                                   
            encoded = str(encoded) + str(31)
        elif i=="W" or i=="w":                                   
            encoded = str(encoded) + str(32)
        elif i=="X" or i=="x":                                   
            encoded = str(encoded) + str(33)
        elif i=="Y" or i=="y":                                   
            encoded = str(encoded) + str(34)
        elif i=="Z" or i=="z":                                   
            encoded = str(encoded) + str(35)
        elif i==" ":                                   
            encoded = str(encoded) + str(36)
        elif i=="$":                                   
            encoded = str(encoded) + str(37)
        elif i=="%":                                   
            encoded = str(encoded) + str(38)
        elif i=="*":                                   
            encoded = str(encoded) + str(39)
        elif i=="+":                                   
            encoded = str(encoded) + str(40)
        elif i=="-":                                   
            encoded = str(encoded) + str(41)
        elif i==".":                                   
            encoded = str(encoded) + str(42)
        elif i=="/":                                   
            encoded = str(encoded) + str(43)
        elif i==":":                                   
            encoded = str(encoded) + str(44)
    return encoded
