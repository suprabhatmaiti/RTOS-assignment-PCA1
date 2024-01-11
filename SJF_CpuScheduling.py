def SJF(burstTime,x):
    print("Process \t Burst Time \t Wating Time \t Turnaround Time")
    i=0
    wt=0
    tat=0
    wtArr=[]
    tatArr=[]
    while(i<len(burstTime)):
        tat+=burstTime[i]
        print("P"+str(x.index(burstTime[i])+1)+"\t\t\t"+str(burstTime[i])+"\t\t"+str(wt)+"\t\t"+str(tat))
        x[x.index(burstTime[i])]=-1
        wtArr.append(wt)
        tatArr.append(tat)
        wt+=burstTime[i]
        i+=1;
    return (wtArr,tatArr)


N=int(input("Enter number of process: "))
wt=[0]*N
tat=[0]*N;


bt=[];
for i in range(0,N):
    ele=int(input("Enter process brust time for p"+str(i+1)+": "))
    bt.append(ele);

lis=SJF(sorted(bt),bt);

print("\nAverage waiting time="+str(sum(lis[0])/len(lis[0])))
print("Average turn around time="+str(sum(lis[1])/len(lis[1])))
