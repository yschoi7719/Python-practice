### For whom want to quickly plot a data file into 2D graph and see the results
### Matplotlib should be installed in advance.
#Example input
#1 5.2 10.6 
#2 6.1 8.3
#3 7.2 7.2

#Example command
#./Plot.py -i input -u 1:3
#./Plot.py -i input -u 1:2 -i input -u 1:3

import matplotlib.pyplot as plt
import sys

total = len(sys.argv)
argv = sys.argv
input_name = ""
inp_i = False
inp_u = False
i = 1
col1 = 1
col2 = 2

for i in range(1,total-1):
    if argv[i][0] == "-":
        cmd = argv[i][1]
        if cmd == "u":
            col1 = argv[i+1][0]
            col2 = argv[i+1][2]
            inp_u = True
        elif cmd == "i":
            input_name = str(argv[i+1])
            inp_i = True
    if inp_i == True and inp_u == True:
        #plot graph
        datax = []
        datay = []
        graph_file = open(input_name,"r")
        lines = graph_file.readlines()
        for line in lines:
            words = line.split()
            x = float(words[int(col1)-1])
            y = float(words[int(col2)-1])
            datax.append(x)
            datay.append(y)
        plt.plot(datax, datay)
        plt.scatter(datax, datay)
        inp_i = False
        inp_u = False

plt.show()
