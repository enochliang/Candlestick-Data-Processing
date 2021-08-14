from datetime import datetime
from datetime import timedelta
import sys

def Filling_Out(imported,generated):
    
    file=open(imported,'r')
    filetext=file.read()
    file_new=open(generated,'a')
    separatebyline=filetext.split('\n')
    
    for i in range(0,len(separatebyline)-2):
        
        ttime=separatebyline[i].split(',')[1]
        ttimedt=datetime.strptime(ttime, "%H:%M:%S")
        next_ttime=separatebyline[i+1].split(',')[1]
        next_ttimedt=datetime.strptime(next_ttime, "%H:%M:%S")
        close=separatebyline[i].split(',')[5]
        
        
        if((next_ttimedt!=(ttimedt+timedelta(minutes=1)))and(next_ttime!='')):
            file_new.write(separatebyline[i]+'\n')
            temptimedt=ttimedt+timedelta(minutes=1)
            while(1):
                if(temptimedt==next_ttimedt):
                    break;
                file_new.write(separatebyline[i].split(',')[0]+','+temptimedt.strftime("%H:%M:%S")+','+f'{close},{close},{close},{close},0\n')
                temptimedt=temptimedt+timedelta(minutes=1)
        else:
            file_new.write(separatebyline[i]+'\n')
    
    file_new.write(separatebyline[len(separatebyline)-2]+'\n')
    print("Finished!!")
            
if __name__=='__main__':
    Filling_Out(sys.argv[1],sys.argv[2])