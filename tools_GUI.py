import string
import matplotlib.pyplot as plt

alphabets = string.ascii_letters


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

def CheckSTR(text):
    for char in text:
        if(char not in alphabets):
            return "Non STR"
    return "STR"

def Plot(time, amount):
    def x_fmt(x, _y=None):
        hour = str(int(x / 60))
        if(len(hour) == 1):
            hour = '0' + hour

        min = str(int(x % 60))
        if(len(min) == 1):
            min = '0' + min

        return f"{hour}:{min}"

    fig, ax = plt.subplots()
    ax.xaxis.set_major_formatter(x_fmt)
    plt.plot(time, amount)

    plt.xlabel("Time (in 24hr system)")
    plt.ylabel("Amount")
    
    for i in range(len(time)):
        ax.annotate(x_fmt(time[i]), (time[i], amount[i]))

    plt.gcf().autofmt_xdate()
    plt.show()