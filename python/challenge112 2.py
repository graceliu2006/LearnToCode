with open("jabberwocky.txt", 'a') as jabberwocky_file:
    for i in range(2,13):
        for j in range(2,13):
            print("{:2} times {} is {}".format(j,i,i*j), file=jabberwocky_file)
        
            