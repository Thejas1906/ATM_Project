def IntInput(msg, bounds=(None, None), digit=None):
    while(True):
        try:
            out = input(msg).strip()
            out = int(out)
            if(bounds != (None, None) and not (bounds[0] <= out <= bounds[1])):
                return "out of bounds"
                continue
            if(digit != None):
                if(len(str(out)) != digit):
                    return "digit error"
                    continue
            return out
        except:
            pass