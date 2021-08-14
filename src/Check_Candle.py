import sys

def Check_Candle_data(filename):
    
    file = open(filename,"r")
    filetext=file.read()
    
    separatebyline=filetext.split('\n')
    
    print('Please select a mode to check data.')
    print('PM : Check if PM data is complete.')
    print('NUM : Check if the number of sticks in every period correct.')
    Mode=input()
    
    pre_tperiod='AM'
    tperiod='AM'
    pre_period='AM'
    period='AM'
    counter=1
    
    for i in range(1,len(separatebyline)-1):
        
        tdate=separatebyline[i].split(',')[0]
        ttime=separatebyline[i].split(',')[1]
        timelist=ttime.split(':')
        
        
        if (int(timelist[0])<=23)and(int(timelist[0])>=15):
            tperiod='PM1'
        elif (int(timelist[0])<=5)and(int(timelist[0])>=0):
            tperiod='PM2'
        elif (int(timelist[0])<=13)and(int(timelist[0])>=8):
            tperiod='AM'
        
        
        if(Mode=="PM"):
            if(pre_tperiod!=tperiod):
                pre_period=period
                period=tperiod
                if((period=='PM2')and(pre_period!='PM1')):
                    print(tdate)
        elif(Mode=="NUM"):
            if((ttime=='13:45:00')or(ttime=='23:59:00')or(ttime=='05:00:00')or((ttime=='13:30:00')and(separatebyline[i+1].split(',')[1]!='13:31:00'))):
                if ((tperiod=='PM1')and(counter!=539))or((tperiod=='PM2')and(counter!=301))or((tperiod=='AM')and((counter!=300)and(counter!=285))):
                    print(tdate+' '+pre_tperiod+'~'+str(counter))
                counter=0
        
        
        counter+=1
        pre_tperiod=tperiod
        
    print("Finished!!")


if __name__=='__main__':
    Check_Candle_data(sys.argv[1])