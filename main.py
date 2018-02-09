from Process import Process

processes = []
cord = -1

while(True):
    print("#######  MENU  #######")
    print('1.add processes')
    print('2.toggle a process')
    print('3.current cord')
    print('\n')

    choice = input("Enter your choice : \n")
    choice = int(choice)

    if(choice == 1):
        if(processes == []):
            n = int(input("Enter no of processes : \n"))
            for i in range(n):
                processes.append(Process(i))
            print("\n Processes created with priorities:")    
            for process in processes:
                print(process.priority)  
        else:
            print("Porcesses already created with priorities : \n")
            for process in processes:
                print(process.priority)  


    if(choice==2):
        if(processes):
            n = int(input("Enter the process pri to toggle: \n"))
            print(processes[n].toggle())
        else:
            print("first create the processes \n")