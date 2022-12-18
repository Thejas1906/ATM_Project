def CheckInt(no, bounds=(None, None), digit=None):
    try:
        no = int(no)
        if(bounds != (None, None) and not (bounds[0] <= no <= bounds[1])):
            return "Out Of Bounds"
        if(digit != None):
            if(len(str(no)) != digit):
                return "Digit Error"
        return "Int"
    except:
        return "Non Int"

