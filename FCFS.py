#process:[arival_time,burst_time,process_no]
def fcfs(process_list):
    process_list.sort()
    t=0
    gantt=[]
    completed={}
    while process_list !=[]:
        process=process_list[0];
        if process_list[0][0]>t:
            t+=1
            continue
        else:
            process=process_list.pop(0)
            gantt.append(process[2])
            t+=process[1]
            pid=process[2]
            ct=t
            tt=ct-process[0]
            wt=tt-process[1]
            completed[pid]=[ct,tt,wt]

    print("Gantt Chart\n")
    print(gantt)
    avgTt=0
    avgWt=0
    for key in completed:
        avgTt+=completed[key][1]
        
        avgWt+=completed[key][2]

    avgWt/=len(completed)
    avgTt/=len(completed)
    
    print("pno ct tat wt")
    for key in completed:
        print(key+str(completed[key]))

    print("\nAverage waiting time="+str(avgWt))
    print("Average turn around time="+str(avgTt))


process_list=[]
n=int(input("Number of process: "))
for i in range(0,n):
    P="P"+str(i)
    at=int(input("Enter arrival time of "+P+": "))
    bt=int(input("Enter burst time of "+P+": "))
        
process_list.append([at,bt,P])
fcfs(process_list)   

