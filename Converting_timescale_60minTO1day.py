import sys
from pathlib import Path
import os

def Converting_timescale_60minTO1day(imported,generated):
    touchfile = Path('./'+generated)
    touchfile.touch(exist_ok=True)
    file_new = open(generated,"a")
    file = open(imported,"r")
    
    if(os.path.getsize('./'+generated)==0):
        file_new.write('Date,Open,High,Low,Close,Volume\n')

    filetext=file.read()
    #print(filetext)

    separatebyline=filetext.split('\n')
    OPEN=0
    HIGH=0
    LOW=0
    CLOSE=0
    VOL=0


    for i in range(1,len(separatebyline)-1):
        tdate_THIS=separatebyline[i].split(',')[0]
        ttime_THIS=separatebyline[i].split(',')[1]
        tH_THIS=ttime_THIS.split(':')[0]
        tM_THIS=ttime_THIS.split(':')[1]
    
        OPEN_THIS=int(separatebyline[i].split(',')[2])
        HIGH_THIS=int(separatebyline[i].split(',')[3])
        LOW_THIS=int(separatebyline[i].split(',')[4])
        CLOSE_THIS=int(separatebyline[i].split(',')[5])
        VOL_THIS=int(separatebyline[i].split(',')[6])
    
        
        if((OPEN==0)and(HIGH==0)and(LOW==0)and(CLOSE==0)and(VOL==0)):#1dayk open signal.
            OPEN=OPEN_THIS
            HIGH=HIGH_THIS
            LOW=LOW_THIS
            CLOSE=CLOSE_THIS
            VOL=VOL_THIS
        else:
            VOL+=VOL_THIS
            CLOSE=CLOSE_THIS
            if(HIGH<HIGH_THIS):
                HIGH=HIGH_THIS
            if(LOW>LOW_THIS):
                LOW=LOW_THIS
        if((int(tH_THIS)==13)and(int(tM_THIS)==45)):#1dayk close signal.
            file_new.write(tdate_THIS+","+str(OPEN)+","+str(HIGH)+","+str(LOW)+","+str(CLOSE)+","+str(VOL)+'\n')
            print(tdate_THIS+","+str(OPEN)+","+str(HIGH)+","+str(LOW)+","+str(CLOSE)+","+str(VOL))
            OPEN=0
            HIGH=0
            LOW=0
            CLOSE=0
            VOL=0
    
    file.close()
    file_new.close()


if __name__=='__main__':
    Converting_timescale_60minTO1day(sys.argv[1],sys.argv[2])