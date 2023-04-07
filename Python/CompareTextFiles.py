import filecmp

f1 = "/Users/hunteradder626/Desktop/Python/Projects/Learning/What_Does_Reddit_Care_about/2022/Jan/02/COPY/TopPost.txt"
f2 = "/Users/hunteradder626/Desktop/Python/Projects/Learning/What_Does_Reddit_Care_about/2022/Jan/02/TopPost.txt"

f1 = open(f1, "r")  
f2 = open(f2, "r")  

i = 0
  
for line1 in f1:
    i += 1
      
    for line2 in f2:
          
        # matching line1 from both files
        if line1 == line2:  
            # print IDENTICAL if similar
            # print("Line ", i, ": IDENTICAL")
            pass       
        else:
            print("Line ", i, ":")
            # else print that line from both files
            print("\tFile 1:", line1, end='')
            print("\tFile 2:", line2, end='')
        break
  
# closing files
f1.close()                                       
f2.close()   