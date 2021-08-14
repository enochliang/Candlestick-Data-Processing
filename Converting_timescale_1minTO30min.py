import sys
from pathlib import Path
import os

def Converting_timescale_1minTO30min(imported,generated):
    touchfile = Path('./'+generated)
    touchfile.touch(exist_ok=True)
    file_new = open(generated,"a")
    file = open(imported,"r")
    
    if(os.path.getsize('./'+generated)==0):
        file_new.write('Date,Time,Open,High,Low,Close,Volume\n')
    
    filetext=file.read()
    #print(filetext)
    
    separatebyline=filetext.split('\n')
    OPEN=0
    HIGH=0
    LOW=0
    CLOSE=0
    VOL=0
    
    counter=1
    for i in range(1,len(separatebyline)-1):
        
        
        tdate_THIS=separatebyline[i].split(',')[0]
        ttime_THIS=separatebyline[i].split(',')[1]
        
        OPEN_THIS=int(separatebyline[i].split(',')[2])
        HIGH_THIS=int(separatebyline[i].split(',')[3])
        LOW_THIS=int(separatebyline[i].split(',')[4])
        CLOSE_THIS=int(separatebyline[i].split(',')[5])
        VOL_THIS=int(separatebyline[i].split(',')[6])
        
        if(counter==1):
            OPEN=OPEN_THIS
            HIGH=HIGH_THIS
            LOW=LOW_THIS
            CLOSE=CLOSE_THIS
            VOL=VOL_THIS
        else:
            CLOSE=CLOSE_THIS
            VOL+=VOL_THIS
            if(HIGH_THIS>HIGH):
                HIGH=HIGH_THIS
            if(LOW_THIS<LOW):
                LOW=LOW_THIS
            if((counter==30)or((counter==15) and (separatebyline[i].split(',')[1]=='13:30:00') and (separatebyline[i+1].split(',')[1]!='13:31:00'))):
                if(counter==15):
                    file_new.write(tdate_THIS+","+"13:45:00"+","+str(OPEN)+","+str(HIGH)+","+str(LOW)+","+str(CLOSE)+","+str(VOL)+'\n')
                    print(tdate_THIS+","+"13:45:00"+","+str(OPEN)+","+str(HIGH)+","+str(LOW)+","+str(CLOSE)+","+str(VOL))
                    OPEN=0
                    HIGH=0
                    LOW=0
                    CLOSE=0
                    VOL=0
                    counter=1
                    continue
                else:
                    file_new.write(tdate_THIS+","+ttime_THIS+","+str(OPEN)+","+str(HIGH)+","+str(LOW)+","+str(CLOSE)+","+str(VOL)+'\n')
                    print(tdate_THIS+","+ttime_THIS+","+str(OPEN)+","+str(HIGH)+","+str(LOW)+","+str(CLOSE)+","+str(VOL))
                    OPEN=0
                    HIGH=0
                    LOW=0
                    CLOSE=0
                    VOL=0
                    counter=1
                    continue

        counter+=1
    
    file.close()
    file_new.close()

if __name__=='__main__':
    Converting_timescale_1minTO30min(sys.argv[1],sys.argv[2])
    