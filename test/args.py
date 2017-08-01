def func(a,b,c = 0,*args,**kw):
      print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw
      func(1,2)
#      a=1 b=2 c=0 args={},kw={}
      func(1,2,c=3)
#      a=1 b=2 c=3 args={},kw={}
      func(1,2,3,'a','b')
#      a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
       # 通过一个tuple和dict也可以调用该函数
     args = (1, 2, 3, 4)
     kw = {'x': 99}
     func(*args, **kw)
#     a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}
