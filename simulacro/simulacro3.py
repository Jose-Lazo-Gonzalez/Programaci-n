dia=int(input("dime dia"))
mes=int(input("mes"))
año=int(input("año"))
suma_mes=0
if año%4==0:
    for i in range (1,mes):
        match i:
            case 1:
                mes=31   
            case 2:
                mes=29    
            case 3:
                mes=31    
            case 4:
                mes=30   
            case 5:
                mes=31   
            case 6:
                mes=30    
            case 7:
                mes=31   
            case 8:
                mes=31    
            case 9:
                mes=30    
            case 10:
                mes=31    
            case 11:
                mes=30   
            case 12:
                mes=31
        suma_mes=mes+suma_mes
else:
    for i in range (1,mes):
        match i:
            case 1:
                mes=31   
            case 2:
                mes=28    
            case 3:
                mes=31    
            case 4:
                mes=30   
            case 5:
                mes=31   
            case 6:
                mes=30    
            case 7:
                mes=31   
            case 8:
                mes=31    
            case 9:
                mes=30    
            case 10:
                mes=31    
            case 11:
                mes=30   
            case 12:
                mes=31
        suma_mes=mes+suma_mes
print(dia+suma_mes)