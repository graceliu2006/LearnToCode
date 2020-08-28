class Pagination:
    def __init__(self,input_list,n=10):
        self.content=input_list
        self.pagesize=int(n)
        self.page_no=0
    
    def nextpage(self):
        if self.page_no*self.pagesize<len(self.content):
            self.page_no+=1
    
    def last(self):
        self.page_no=max(len(self.content)-1,0)//self.pagesize
            
    def getVisibleItems(self):
        return self.content[self.page_no*self.pagesize:self.page_no*self.pagesize+self.pagesize]
            
        

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

print(p.getVisibleItems())

p.nextpage()

print(p.getVisibleItems())

p.last()

print(p.getVisibleItems())


my_list=["a","b","c"]
print(my_list[0:10)

