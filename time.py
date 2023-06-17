class Time:
    def __init__(self, hh, mm, ss):
        self.s = ss
        self.m = mm
        self.h = hh
        self.fix()

    # sum two times
    def sum(self, time2):
        s_new = self.s + time2.s
        m_new = self.m + time2.m
        h_new = self.h + time2.h
        result = Time(h_new, m_new, s_new)
        self.fix()
        return result

    # fix time
    def fix(self):
        if self.s >= 60:
            self.s -= 60
            self.m += 1

        if self.m >= 60:
            self.m -= 60
            self.h += 1
        
        if self.s < 0:
            self.s += 60
            self.m -= 1
        
        if self.m < 0:
            self.m += 60
            self.h -= 1

    # show time
    def show(self):
        print(self.h, ":", self.m, ":", self.s)

    #check digital format
    def convert_to_digital(self):
        if self.s < 10:
            sss = str(self.s)
            self.s = "0" + sss

        if self.m < 10:
            mmm = str(self.m)
            self.m = "0" + mmm

        if self.h < 10:
            hhh = str(self.h)
            self.h = "0" + hhh


zaman1 = Time(4, 36, 45)
zaman1.show()

zaman2 = Time(2, 26, 17)

zaman3 = zaman1.sum(zaman2)
zaman3.convert_to_digital()
zaman3.show()
