class node:
    def __init__ (self,val):
        self.val=val
        self.next=None
class Linkedlist:
    def __init__ (self):
        self.head=None
        #creat a dynamic circular linkedlist
        
    def creat(self,n):
        i=0
        while i<n:
            newnode=node(input("enter val"))
            if i==0:
                self.head=newnode
            else:
                t=self.head
                while t.next:
                    t=t.next
                t.next=newnode
            i=i+1
            newnode.next=self.head.next
    def show(self):
        t=self.head
        while t:
            print(t.val,end="-->")
            t=t.next
            ch=input("enter ok")
            if ch=='ok':
                break


obj=Linkedlist()
obj.creat(4)
obj.show()
