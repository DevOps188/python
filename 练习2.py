class People(object):

    def __init__(self, name, Q, W, e):
        self.name = name
        self.Q = Q
        self.W = W
        self.e = e

    def QQ(self):
        print("{} 使用了 {}技能 并喊出哈撒K".format(self.name, self.Q))

    def WW(self):
        print("{} 使用了 {}技能 并喊出了面对疾风吧".format(self.name, self.W))

    def EE(self):
            print("{} 使用了 {}技能搓来搓去好似潇洒并按出了CTRL+6".format(self.name, self.e))


class yx(People):
    def EE(self):
        print("{} 还没开始就gg".format(self.name))

    def RR(self):
        print("{} 一人独自在人群中EEEER起五人后落荒而逃秀出自己的七级狗牌".format(self.name))

#  快乐风男

class klfn(People):
    def __init__(self,name,Q,W,e,D,F):
        self.name = name
        self.Q = Q
        self.W = W
        self.e = e
        self.D = D
        self.E = F

    def EE(self):
        print("{} 还没开始就gg".format(self.name))

    def RR(self):
        print("{} 一人独自在人群中EEEER起五人后落荒而逃秀出自己的七级狗牌".format(self.name))

    def DD(self):
        print("{} 选着闪现过来吓你一跳".format(self.name))



p1 = yx("亚索", "Q", "W", "E")

p1.QQ()
p1.WW()
p1.EE()
p1.RR()
p2 = klfn("快乐风男","Q","W","E","闪现","F")
p2.DD()