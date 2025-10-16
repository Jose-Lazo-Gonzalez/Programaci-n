g1=(input("dime el grupo sanguineo del receptor"))
g2=(input("dime el grupo sanguineo del donador"))
match g1:
    case "AB+":
        print("es receptor de todos los grupos")
    case "AB-":
        if g2=="0-" or g2=="A-" or g2=="B-" or g2=="AB-":
            print("AB- es receptor de",g2)
        else:
            print("no son compatible")
    case "B+":
        if g2=="0-" or g2=="0+" or g2=="B-"or g2=="B+":
            print("B+ es receptor de",g2)
        else:
            print("no son compatibles")
    case "B-":
        if g2=="0-" or g2=="B-":
            print("B- es receptor de",g2)
        else:
            print("no son compatibles")