# -*- coding: utf-8 -*-

(h1, m1)=map(int, raw_input().split(":"))
(h2, m2)=map(int, raw_input().split(":"))

#(h1, m1) = times
#(h2, m2) = times

t1 = h1*60 + m1 

t2 = h2*60 + m2


t3 = t1 + t2 



ans1 = (t3/60)%24

ans2 = t3%60


print '%02d:%02d' %(ans1,ans2)
