def myquick_sort(l):
    if len(l)>=2:
        f=open("output.txt","w")
        p=0
        s=1
        e=len(l)-1
        f1=0
        f2=0
        while s<len(l) and e>0:
            if e<s or s==e and l[e]<=l[p]:
                t=l[p]
                l[p]=l[e]
                l[e]=t
                f.write(f"{l}\n")
                print(l,"l[0:e]=",l[0:e],"l[e]=",l[e])
                l1=list(myquick_sort(l[0:e]))
                l1.append(l[e])
                l2=list(myquick_sort(l[e+1:len(l)]))
                print("The l1:",l1,"The l2:",l2,"The l[e]:",l[e])
                l3=l1+l2            
                return l3
            elif f1 and f2:
                t=l[s]
                l[s]=l[e]
                l[e]=t
                f1=f2=0
            else:

                if l[p]>=l[s] and f1==0:
                    s+=1
                else:
                    f1=1
                if l[p]<l[e] and f2==0:
                    e-=1
                else:
                    f2=1
        else:
            if e<=0:
                l4=myquick_sort(l[e+1:len(l)])
                print("Hello ")
                l4.insert(0,l[0])
                print(l4)
                return  l4
    else:
        return l

                

if __name__ =="__main__":
    print("Started")
    l=[64,25,12,22,11]
    print("The final list",myquick_sort(l))