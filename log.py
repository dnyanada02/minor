fname = input("Enter file name: ")
num="200"
count = 0;

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==num):
                count=count+1
print("Occurrences of the number:",count)
