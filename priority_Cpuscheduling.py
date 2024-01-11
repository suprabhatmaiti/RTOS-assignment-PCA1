#process:[priority,burst_time,arival_time,process_no]
def priority(process_list):
    t=0
    gantt=[]
    completed={}
    while process_list != []:
        available=[]
        for p in process_list:
            if p[2]<=t:
                available.append(p)
        if available ==[]:
            gantt.append("idle")
            t+=1
            continue
        else:
            available.sort()
            process=available[0]
            process_list.remove(process)
            pid=process[3]
            gantt.append(pid)
            t+=process[1]
            ct=t
            tt=ct-process[2]
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
    pt=int(input("Enter priority of "+P+": "))
    process_list.append([pt,bt,at,P])

priority(process_list)