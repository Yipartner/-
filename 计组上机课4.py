import sys

class nenv:
    def __init__(self,dir):
        self.dir = dir
        self.file = None
        self.freeZone = [
            [0,300,300]
        ]
        self.useZone = []
    def free(self,start):
        useZone = None
        for i in self.useZone:
            if i[0]==start:
                useZone = i
                break
        self.useZone = [i for i in self.useZone if i[0]!=start]
        self.freeZone.append(useZone)
        self.freeZone.sort()
        l = len(self.freeZone)
        # print(l)
        i = 0
        while i!=l-1:  
            # print(i,self.freeZone[i])
            if self.freeZone[i][1]==self.freeZone[i+1][0]:
                self.freeZone[i][1]=self.freeZone[i+1][1]
                self.freeZone[i][2]=self.freeZone[i][2]+self.freeZone[i+1][2]
                del self.freeZone[i+1]
                i=i-1
                l-=1
            i+=1
        # print(self.freeZone)
    def findZone(self,cl):
        l =len(self.freeZone)
        for i in range(l):
            if cl <= self.freeZone[i][2]:
                if len == self.freeZone[i][2]:
                    temp = self.freeZone[i].copy()
                    self.useZone.append(self.freeZone[i])
                    self.useZone.sort()
                    del self.freeZone[i]
                    return temp

                else:
                    temp = [self.freeZone[i][0],self.freeZone[i][0]+cl,cl]
                    self.useZone.append([self.freeZone[i][0],self.freeZone[i][0]+cl,cl])
                    self.useZone.sort()
                    self.freeZone[i][0]+=cl
                    self.freeZone[i][2]-=cl
                    return temp
        return [-1,-1,-1]
    def ls(self):
        print('.',end = ' ')
        print('..',end = ' ')
        for i in self.dir.child:
            if isinstance(self.dir.child[i],dir):
                print(''+i+'(d)',end = ' ')
            else:
                print(''+i+'(f)',end = ' ')
        print()
    def mkdir(self,name):
        if name in self.dir.child:
            print('name has exist')
            return
        child = dir(name,self.dir)
        self.dir.child[name]=child
    def cd(self,name):
        if name == '.':
            return
        if name == '..':
            self.dir=self.dir.parent
            return
        if name not in self.dir.child:
            print('dir not found')
            return
        self.dir=self.dir.child[name]
    def rmdir(self,name):
        if name not in self.dir.child:
            print('dir not found')
            return
        del self.dir.child[name]
    def rm(self,name):
        if name not in self.dir.child:
            print('file not found')
            return
        if name == self.file.name:
            print('file is opened,cant be remove!')
            return
        self.free(self.dir.child[name].start)
        del self.dir.child[name]
    def create(self,name):
        if name in self.dir.child:
            print('name has exist')
            return
        f = file(name,self.dir)
        self.dir.child[name]=f
    def open(self,name):
        if name not in self.dir.child:
            print('file not found')
            return
        if isinstance(self.dir.child[name],file)==False:
            print('type error!')
            return
        self.file = self.dir.child[name]
    def close(self):
        self.file = None
    def write(self,content):
        if self.file.content !='':
            self.free(self.file.start)
        p=self.findZone(len(content))
        if p[0]==-1:
            print('freeZone not enough')
            return
        self.file.content = content
        self.file.start=p[0]
        self.file.end=p[1]
    def read(self,name):
        if name not in self.dir.child:
            print('file not found')
            return
        f = self.dir.child[name]
        print('fileName:',f.name)
        print('fileLength:',len(f.content))
        print('fileContent:',f.content)
        print('fileZone:','['+str(f.start)+','+str(f.end)+']')
    def show(self):
        print('freeZone:',self.freeZone)
        print('useZone:',self.useZone)
class file:
    def __init__(self,name,parent):
        self.name = name
        self.parent = parent
        self.content = ''
        self.start,self.end = -1,-1
class dir:
    def __init__(self,name,parent):
        self.name = name
        self.parent = parent
        self.child = {}


    
ndir = dir('root','#')
env = nenv(ndir)

while True:
    print('hanxiao',end =':')
    k = [i for i in input().split()]
    cmd = k[0]
    if cmd == 'mkdir':
        env.mkdir(k[1])
    if cmd == 'rmdir':
        env.rmdir(k[1])
    if cmd == 'ls':
        env.ls()
    if cmd == 'cd':
        env.cd(k[1])
    if cmd == 'create':
        env.create(k[1])
    if cmd == 'open':
        env.open(k[1])
    if cmd == 'close':
        env.close
    if cmd == 'write':
        env.write(k[1])
    if cmd == 'read':
        env.read(k[1])
    if cmd == 'rm':
        env.rm(k[1])
    if cmd == 'show':
        env.show()
    if cmd == 'exit':
        print('感谢使用!')
        print('学号：20167593')
        print('序号：160207')
        print('姓名：韩笑')
        exit()
    
    
