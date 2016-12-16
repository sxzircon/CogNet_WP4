
def time_slot (time): #HH:MM:SS
    x = time[0:2]
    if x == "00" or x == "01":
        output = "0"
    elif x == "02" or x == "03":
        output = "1"
    elif x == "04" or x == "05":
        output = "2"
    elif x == "06" or x == "07":
        output = "3"
    elif x == "08" or x == "09":
        output = "4"
    elif x == "10" or x == "11":
        output = "5"
    elif x == "12" or x == "13":
        output = "6"
    elif x == "14" or x == "15":
        output = "7"
    elif x == "16" or x == "17":
        output = "8"
    elif x == "18" or x == "19":
        output = "9"
    elif x == "20" or x == "21":
        output = "10"
    elif x == "22" or x == "23":
        output = "11"
    else:
        output = "NA"
    return output;



def Two_time_slot (time): #HH:MM:SS
    x = time[0:2]
    if x == "00" or x == "01":
        output = 0
    elif x == "02" or x == "03":
        output = 1
    elif x == "04" or x == "05":
        output = 2
    elif x == "06" or x == "07":
        output = 3
    elif x == "08" or x == "09":
        output = 4
    elif x == "10" or x == "11":
        output = 5
    elif x == "12" or x == "13":
        output = 6
    elif x == "14" or x == "15":
        output = 7
    elif x == "16" or x == "17":
        output = 8
    elif x == "18" or x == "19":
        output = 9
    elif x == "20" or x == "21":
        output = 10
    elif x == "22" or x == "23":
        output = 11
    else:
        output = -1
    return output;


def days_per_month (month):
    ThirtyOne_Days = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
    Thirty_Days = ["Apr", "Jun", "Sep", "Nov"]
    TwentyEight_Days = ["Feb"]
    if any(month in s for s in ThirtyOne_Days):
        days = 31
    if any(month in s for s in Thirty_Days):
        days = 30
    if any(month in s for s in TwentyEight_Days):
        days = 28
    return days;

def Eight_time_slot (time): #HH:MM:SS
    x = time[0:2]
    if x == "00" or x == "01" or x == "02" or x == "03" or x == "04" or x == "05" or x == "06" or x == "07":
        output = 0
    elif x == "08" or x == "09" or x == "10" or x == "11" or x == "12" or x == "13" or x == "14" or x == "15":
        output = 1
    elif x == "16" or x == "17" or x == "18" or x == "19" or x == "20" or x == "21" or x == "22" or x == "23":
        output = 2
    else:
        output = -1
    return output;

def Four_time_slot (time): #HH:MM:SS
    x = time[0:2]
    if x == "00" or x == "01" or x == "02" or x == "03":
        output = 0
    elif x == "04" or x == "05" or x == "06" or x == "07":
        output = 1
    elif x == "08" or x == "09" or x == "10" or x == "11":
        output = 2
    elif x == "12" or x == "13" or x == "14" or x == "15":
        output = 3
    elif x == "16" or x == "17" or x == "18" or x == "19":
        output = 4
    elif x == "20" or x == "21" or x == "22" or x == "23":
        output = 5
    else:
        output = -1
    return output;

def one_time_slot (time): #HH:MM:SS
    x = time[0:2]
    if x == "00":   output = 0
    elif x=="01":   output = 1
    elif x=="02":   output = 2
    elif x=="03":   output = 3
    elif x=="04":   output = 4
    elif x=="05":   output = 5
    elif x=="06":   output = 6
    elif x=="07":   output = 7
    elif x=="08":   output = 8
    elif x=="09":   output = 9
    elif x=="10":   output = 10
    elif x=="11":   output = 11
    elif x=="12":   output = 12
    elif x=="13":   output = 13
    elif x=="14":   output = 14
    elif x=="15":   output = 15
    elif x=="16":   output = 16
    elif x=="17":   output = 17
    elif x=="18":   output = 18
    elif x=="19":   output = 19
    elif x=="20":   output = 20
    elif x=="21":   output = 21
    elif x=="22":   output = 22
    elif x=="23":   output = 23
    else:   output =-1
    return output;