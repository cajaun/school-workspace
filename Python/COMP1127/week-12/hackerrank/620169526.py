def completionTime(l, n, cycles):
    processes = [(cycles[i], i) for i in range(n)]  
    currentTime = 0

    while processes:
        remainingCycles, processId = processes.pop(0) 

        if remainingCycles <= l:
     
            currentTime += remainingCycles
            return currentTime
        else:

            currentTime += l
            processes.append((remainingCycles - l, processId))