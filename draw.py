import sys
import math
import random
import pdb
printing=[]
variables={}
variable=0
variableholder=[]
final={}
drawer=[]


class line:
    def __init__(self, draw, index):
        self.linex=float(draw[(index+1)])
        self.liney=float(draw[(index+2)])
        self.linex1=float(draw[(index+3)])
        self.liney1=float(draw[(index+4)])
    def rotation(self, rotate):
        self.linexrot= (self.linex*(math.cos(rotate))) - (self.liney*(math.sin(rotate)))
        self.lineyrot= self.linex*(math.sin(rotate)) + self.liney*(math.cos(rotate))
        self.linex1rot=self.linex1*(math.cos(rotate)) - self.liney1*(math.sin(rotate))
        self.liney1rot=self.linex1*(math.sin(rotate)) + self.liney1*(math.cos(rotate))
        self.linex=self.linexrot
        self.liney=self.lineyrot
        self.linex1=self.linex1rot
        self.liney1=self.liney1rot
    def translate(self, translatex, translatey):
        self.linex=self.linex+translatex
        self.liney=self.liney+translatey
        self.linex1=self.linex1+translatex
        self.liney1=self.liney1+translatey
    def scale(self, scale):
        self.linex=self.linex * scale
        self.liney=self.liney * scale
        self.linex1=self.linex1 * scale
        self.liney1=self.liney1 * scale
    def drawing(self):
        print(self.linex, self.liney, "moveto")
        print(self.linex1, self.liney1, "lineto")
        print('stroke')
class filledline(line):
    def drawing(self):
        print(self.linex, self.liney, "moveto")
        print(self.linex1, self.liney1, "lineto")
        print('fill')
class rectangle(line):
    def __init__(self, draw, index):
        self.linex1=float(draw[(index+1)])
        self.liney1=float(draw[(index+2)])
        self.linex3=float(draw[(index+3)])+float(draw[(index+1)])
        self.liney3=float(draw[(index+4)])+float(draw[(index+2)])
        self.linex2=self.linex3
        self.liney2=self.liney1
        self.linex4=self.linex1
        self.liney4=self.liney3
    def drawing(self):
        print(self.linex1, self.liney1, "moveto")
        print(self.linex2, self.liney2, "lineto")
        print(self.linex3, self.liney3, "lineto")
        print(self.linex4, self.liney4, "lineto")
        print(self.linex1, self.liney1, "lineto")
        print('stroke')
    def translate(self, translatex, translatey):
        self.linex1=self.linex1+translatex
        self.liney1=self.liney1+translatey
        self.linex2=self.linex2+translatex
        self.liney2=self.liney2+translatey
        self.linex3=self.linex3+translatex
        self.liney3=self.liney3+translatey
        self.linex4=self.linex4+translatex
        self.liney4=self.liney4+translatey
    def rotation(self, rotate):
        self.rotx1= self.linex1*math.cos(rotate) - self.liney1*math.sin(rotate)
        self.roty1= self.linex1*math.sin(rotate) + self.liney1*math.cos(rotate)
        self.rotx2= (self.linex2)*math.cos(rotate) - self.liney2*math.sin(rotate)
        self.roty2= (self.linex2)*math.sin(rotate) + self.liney2*math.cos(rotate)
        self.rotx3= (self.linex3)*math.cos(rotate) - (self.liney3)*math.sin(rotate)
        self.roty3= (self.linex3)*math.sin(rotate) + (self.liney3)*math.cos(rotate)
        self.rotx4= (self.linex4)*math.cos(rotate) - (self.liney4)*math.sin(rotate)
        self.roty4= (self.linex4)*math.sin(rotate) + (self.liney4)*math.cos(rotate)
        self.linex1=self.rotx1
        self.liney1=self.roty1
        self.linex2=self.rotx2
        self.liney2=self.roty2
        self.linex3=self.rotx3
        self.liney3=self.roty3
        self.linex4=self.rotx4
        self.liney4=self.roty4
    def scale(self, scale):
        self.linex1=self.linex1*scale
        self.liney1=self.liney1*scale
        self.linex2=self.linex2*scale
        self.liney2=self.liney2*scale
        self.linex3=self.linex3*scale
        self.liney3=self.liney3*scale
        self.linex4=self.linex4*scale
        self.liney4=self.liney4*scale
class filledrectangle(rectangle):
    def drawing(self):
        print(self.linex1, self.liney1, "moveto")
        print(self.linex2, self.liney2, "lineto")
        print(self.linex3, self.liney3, "lineto")
        print(self.linex4, self.liney4, "lineto")
        print(self.linex1, self.liney1, "lineto")
        print('fill')
class ngon:
    def __init__(self, draw, index):
        self.n = int(draw[(index+4)])
        self.nfloat=float(self.n)
        self.vertex = float(draw[(index+3)])
        self.polyx=float(draw[(index+1)])
        self.polyy=float(draw[(index+2)])
        self.holder=[]
        self.bigholder=[]
        self.hodlx=0.0
        self.hodly=0.0
        self.calculate()
    def calculate(self):
        for g in range(1,(self.n+1)):
            self.z=float(g)
            self.linex=float(self.polyx+self.vertex*(math.cos(self.z*((2*math.pi)/self.nfloat))))
            self.liney=float(self.polyy+self.vertex*(math.sin(self.z*((2*math.pi)/self.nfloat))))
            self.holder.append(self.linex)
            self.holder.append(self.liney)
            self.bigholder.append(self.holder)
            self.holder = []
    def rotation(self, rotate):
        for p in self.bigholder:
            self.hodlx=p[0]*math.cos(rotate) - p[1]*math.sin(rotate)
            self.hodly=p[0]*(math.sin(rotate)) + p[1]*(math.cos(rotate))
            p[0]=self.hodlx
            p[1]=self.hodly
    def scale(self, scale):
        for p in self.bigholder:
            self.hodlx=p[0]*scale
            self.hodly=p[1]*scale
            p[0]=self.hodlx
            p[1]=self.hodly
    def translate(self, translatex, translatey):
        for p in self.bigholder:
            self.hodlx=p[0]+translatex
            self.hodly=p[1]+translatey
            p[0]=self.hodlx
            p[1]=self.hodly
    def drawing(self):
        print((self.bigholder[-1][0]), self.bigholder[-1][1], 'moveto')
        for p in self.bigholder:
            print(p[0], p[1], 'lineto')
        print('stroke')
class filledngon(ngon):
    def drawing(self):
        print((self.bigholder[-1][0]), self.bigholder[-1][1], 'moveto')
        for p in self.bigholder:
            print(p[0], p[1], 'lineto')
        print('fill')
class penta(ngon):
    def __init__(self, draw, index):
        self.n = 5
        self.nfloat=float(self.n)
        self.vertex = float(draw[(index+3)])
        self.polyx=float(draw[(index+1)])
        self.polyy=float(draw[(index+2)])
        self.holder=[]
        self.bigholder=[]
        self.hodlx=0.0
        self.hodly=0.0
        self.calculate()
class filledpenta(penta):
    def drawing(self):
        print((self.bigholder[-1][0]), self.bigholder[-1][1], 'moveto')
        for p in self.bigholder:
            print(p[0], p[1], 'lineto')
        print('fill')
class hexa(ngon):
    def __init__(self, draw, index):
        self.n = 6
        self.nfloat=float(self.n)
        self.vertex = float(draw[(index+3)])
        self.polyx=float(draw[(index+1)])
        self.polyy=float(draw[(index+2)])
        self.holder=[]
        self.bigholder=[]
        self.hodlx=0.0
        self.hodly=0.0
        self.calculate()
class filledhexa(hexa):
    def drawing(self):
        print((self.bigholder[-1][0]), self.bigholder[-1][1], 'moveto')
        for p in self.bigholder:
            print(p[0], p[1], 'lineto')
        print('fill')
class tri(ngon):
    def __init__(self, draw, index):
        self.n = 3
        self.nfloat=float(self.n)
        self.vertex = float(draw[(index+3)])
        self.polyx=float(draw[(index+1)])
        self.polyy=float(draw[(index+2)])
        self.holder=[]
        self.bigholder=[]
        self.hodlx=0.0
        self.hodly=0.0
        self.calculate()
class filledtri(tri):
    def drawing(self):
        print((self.bigholder[-1][0]), self.bigholder[-1][1], 'moveto')
        for p in self.bigholder:
            print(p[0], p[1], 'lineto')
        print('fill')
class square(ngon):
     def __init__(self, draw, index):
        self.n = 4
        self.nfloat=float(self.n)
        self.vertex = float(draw[(index+3)])
        self.polyx=float(draw[(index+1)])
        self.polyy=float(draw[(index+2)])
        self.holder=[]
        self.bigholder=[]
        self.hodlx=0.0
        self.hodly=0.0
        self.calculate()
class filledsquare(square):
    def drawing(self):
        print((self.bigholder[-1][0]), self.bigholder[-1][1], 'moveto')
        for p in self.bigholder:
            print(p[0], p[1], 'lineto')
        print('fill')
class sector:
    def __init__(self, draw, index):
        self.centerx=float(draw[(index+1)])
        self.centery=float(draw[(index+2)])
        self.radius=float(draw[(index+3)])
        self.angle1=float(draw[(index+4)])
        self.angle2=float(draw[(index+5)])
        while self.angle2 >= 360:
            r=self.angle2//360
            self.angle2=self.angle2-(r*360)
        while self.angle1 >= 360:
            r=self.angle1//360
            self.angle1=self.angle1-(r*360)
        while self.angle2 > 360:
            r=self.angle2//360
            self.angle2=self.angle2-(r*360)
        while self.angle2 < 0:
            self.angle2 = self.angle2 + 360
        while self.angle1 < 0:
            self.angle1 = self.angle1 + 360
        self.calculate()
    def calculate(self):
        self.angle1rads=math.radians(self.angle1)
        self.angle2rads=math.radians(self.angle2)
        self.vertice1x=(self.radius)*math.sin(((math.pi/2)-self.angle1rads))+self.centerx
        self.vertice1y=(self.radius)*math.sin(self.angle1rads)+self.centery
    def rotation(self, rotate):
        self.angle1=self.angle1+math.degrees(rotate)
        self.angle2=self.angle2+math.degrees(rotate)
        while self.angle2 >= 360:
            r=self.angle2//360
            self.angle2=self.angle2-(r*360)
        while self.angle1 >= 360:
            r=self.angle1//360
            self.angle1=self.angle1-(r*360)
        while self.angle2 > 360:
            r=self.angle2//360
            self.angle2=self.angle2-(r*360)
        while self.angle2 < 0:
            self.angle2 = self.angle2 + 360
        while self.angle1 < 0:
            self.angle1 = self.angle1 + 360
        self.centerxrot= self.centerx*(math.cos(rotate)) - self.centery*(math.sin(rotate))
        self.centeryrot= self.centerx*(math.sin(rotate)) + self.centery*(math.cos(rotate))
        self.vertice1xrot= self.vertice1x*(math.cos(rotate)) - self.vertice1y*(math.sin(rotate))
        self.vertice1yrot= self.vertice1x*(math.sin(rotate)) + self.vertice1y*(math.cos(rotate))
        self.centerx=self.centerxrot
        self.centery=self.centeryrot
        self.vertice1x=self.vertice1xrot
        self.vertice1y=self.vertice1yrot
    def translate(self, translatex, translatey):
        self.centerx=self.centerx+translatex
        self.centery=self.centery+translatey
        self.vertice1x=self.vertice1x+translatex
        self.vertice1y=self.vertice1y+translatey
    def scale(self, scale):
        self.radius=self.radius*scale
        self.centerx = self.centerx*scale
        self.centery = self.centery*scale
        self.vertice1x=self.vertice1x*scale
        self.vertice1y=self.vertice1y*scale
    def drawing(self):
        print(self.centerx, self.centery, "moveto")
        print(self.vertice1x, self.vertice1y, "lineto")
        print(self.centerx, self.centery, self.radius, self.angle1, self.angle2, "arc")
        print(self.centerx, self.centery, "lineto")
        print("stroke")
class filledsector(sector):
    def drawing(self):
        print(self.centerx, self.centery, "moveto")
        print(self.vertice1x, self.vertice1y, "lineto")
        print(self.centerx, self.centery, self.radius, self.angle1, self.angle2, "arc")
        print(self.centerx, self.centery, "lineto")
        print("fill")
class color:
    def __init__(self, draw, index):
        self.r = float(draw[(index+1)])
        self.g = float(draw[(index+2)])
        self.b = float(draw[(index+3)])
    def drawing(self):
        print(self.r, self.g, self.b, "setrgbcolor")
class linewidth:
    def __init__(self, draw, index):
        self.w = float(draw[(index+1)])
    def drawing(self):
        print(self.w, "setlinewidth")


def postfixer(draw1):
    draw=draw1
    index=0
    resultpost=[]
    translatex=0
    translatey=0
    scale=1
    pointer=0
    holder=0
    global jarjar
    global larlar
    global variables
    global variable
    global final
    global drawer
    global variableholder
    for index, u in enumerate(draw):
        if u in variableholder and (draw[(index-1)]!=":=") and (draw[(index-1)]!="for"):
            draw[index]=variables[draw[index]]
    for index, u in enumerate(draw):
        if u == '*':
            resultpost.append(float(draw[index+1]) * float(draw[index+2]))
        elif u == '+':
            resultpost.append(float(draw[index+1]) + float(draw[index+2]))
        elif u == "-":
            resultpost.append(float(draw[index+1]) - float(draw[index+2]))
        elif u == "/":
            resultpost.append(float(draw[index+1]) / float(draw[index+2]))
        elif u == "cos":
            holder=math.radians(float(draw[(index+1)]))
            holder=math.cos(holder)
            resultpost.append(holder)
        elif u == 'for':
            for index2 in draw:
                final[index2].rotation(rotate)
                resultpost.append(index2)
        elif u == "sin":
            holder=math.radians(float(draw[(index+1)]))
            holder=math.sin(holder)
            resultpost.append(holder)
        elif u == ":=":
            variables[(draw[(index+1)])] = draw[(index+2)]
            variableholder.append(draw[(index+1)])
        elif u == "color":
            pointer=random.randint(1111,22222)
            final[pointer]=color(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "linewidth":
            pointer=random.randint(1111,22222)
            final[pointer]=linewidth(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "rotate":
            rotate=(float(draw[-1]))
            if abs(rotate) > 360:
                r=rotate//360
                rotate=rotate-(r*360)
            rotate=math.radians(rotate)
            for index2 in draw[1:-1]:
                final[index2].rotation(rotate)
                resultpost.append(index2)
        elif u == "translate":
            translatex=float(draw[-2])
            translatey=float(draw[-1])
            for index2 in draw[1:-2]:
                final[index2].translate(translatex, translatey)
                resultpost.append(index2)
        elif u == "scale":
            scale=float(draw[(-1)])
            for index2 in draw[1:-1]:
                final[index2].scale(scale)
                resultpost.append(index2)
        elif u == "line":
            pointer=random.randint(1111,22222)
            final[pointer]=line(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "filledline":
            pointer=random.randint(1111,22222)
            final[pointer]=filledline(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "rect":
            pointer=random.randint(1111,22222)
            final[pointer]=rectangle(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "filledrect":
            pointer=random.randint(1111,22222)
            final[pointer]=filledrectangle(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "ngon":
            pointer=random.randint(1111,22222)
            final[pointer]=ngon(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "filledngon":
            pointer=random.randint(1111,22222)
            final[pointer]=filledngon(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "square":
            pointer=random.randint(1111,22222)
            final[pointer]=square(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "filledsquare":
            pointer=random.randint(1111,22222)
            final[pointer]=filledsquare(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "penta":
            pointer=random.randint(1111,22222)
            final[pointer]=penta(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "filledpenta":
            pointer=random.randint(1111,22222)
            final[pointer]=filledpenta(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "hexa":
            pointer=random.randint(1111,22222)
            final[pointer]=hexa(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "filledhexa":
            pointer=random.randint(1111,22222)
            final[pointer]=filledhexa(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "tri":
            pointer=random.randint(1111,22222)
            final[pointer]=tri(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "filledtri":
            pointer=random.randint(1111,22222)
            final[pointer]=filledtri(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "sector":
            pointer=random.randint(1112,22222)
            final[pointer]=sector(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "filledsector":
            pointer=random.randint(1112,22222)
            final[pointer]=filledsector(draw, index)
            drawer.append(pointer)
            resultpost.append(pointer)
        elif u == "group":
            for x in draw:
                if x != "group":
                    resultpost.append(x)
       # elif type(u) == int:
            #if int(u) > 1111:
                #resultpost.append(u)
    return resultpost

def cal(stuff):
    lol=stuff
    index=1
    draw1 =[]
    range1=0
    range2=0
    indexreturn=0
    J=0
    global variables
    global variableholder
    global jarjar
    global drawer
    while index < len(lol):
        jarjar=lol[index]
        if lol[index] == "(":
            indexreturn, result =cal(lol[index:])
            index = index + indexreturn
            for x in result:
                draw1.append(x)
        elif lol[index] == ")":
            result = postfixer(draw1)
            return index, result
        elif lol[index] == "for":
            range1=int(lol[(index+2)])
            range2=int(lol[(index+3)])
            var=(lol[(index+1)])
            variables[var]=range1
            variableholder.append(var)
            if range1 < range2:
                holder=calalt(lol[(index+3):])+index+4
                lol.insert(holder, ")")
                j=index+4
                lol.insert(j, "group")
                lol.insert(j, "(")
                for I in range(range1,(range2+1)):
                    variables[var]=I
                    indexreturn, result =cal(lol[(index+4):])
                    variables[var]=range2
                    for x in result:
                        draw1.append(x)
                return holder-1, 'wat'
            elif range1 > range2:
                indexreturn = calalt(lol[(index+3):])
                return (indexreturn+3+index), '0'
        else:
            draw1.append(lol[index])
        index= index+1
    return (len(lol)), 'wat'
test=['(','for','1','2','(','line','5','5','5','5',')',')','(','linewidth','5',')']
def calalt(lol):

    index=1
    while index <= len(lol):
        if lol[index] == "(":
            indexreturn = calalt(lol[index:])
            index =  index + indexreturn
        elif lol[index] == ")":
            return (index)
        index = index +1



stuff = sys.stdin.read()
stuff = stuff.replace("(", " ( ")
stuff = stuff.replace(")", " ) ")
stuff = stuff.split()
reach=len(stuff)
stuff.insert(0, "(")
stuff.append(")")
print('%!PS-Adobe-3.0 EPSF-3.0')
print('%%BoundingBox: 0 0 1239 1752')
hah=cal(stuff)
for x in drawer:
    final[x].drawing()
