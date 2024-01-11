#process:[burst_time,arival_time,process_no]
def sjf(process_list):
    t=0
    gantt=[]
    completed={}
    burst_time={}
    #keeping record of burst time for future
    for i in process_list:
        burst_time[i[2]]=i[0]

    while process_list !=[]:
        available=[]
        for p in process_list:
            if p[1]<=t:
                available.append(p)
        
        if available ==[]:
            t+=1
            gantt.append("idle")
            continue
        else:
            available.sort()
            process=available[0]
            copy_process=available.pop(0)
            process[0]-=1
            t+=1
            gantt.append(process[2])
            process_list.remove(copy_process)
            if process[0]==0:
                ct=t
                tt=ct-process[1]
                wt=tt-burst_time[process[2]]
                completed[process[2]]=[ct,tt,wt]
                continue
            else:
                process_list.append(process)

            

    print("Gantt Chart\n")
    print(gantt)
    avgTt=0
    avgWt=0
    for key in completed:
        avgTt+=completed[key][1]
        avgWt+=completed[key][2]

    avgWt/=len(completed)
    avgTt/=len(completed)
    
    print("\npno ct tat wt")
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
    process_list.append([bt,at,P])

sjf(process_list)