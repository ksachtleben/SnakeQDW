import math

class QuantumEnergy():
    def __init__(self, time):
        EM0 = 9.1091e-28
        EMB = 0.067 * EM0
        EP0 = 12.9
        HB = 1.0545e-27
        EC = 4.8029e-10

        AB = (HB * HB * EP0) / (EMB * EC * EC)
        RY = (EC * EC) / (2 * EP0 * AB)
        ONEA = 1.0e-8
        self.ABA = (AB) / (ONEA)
        self.time = time

        ONEMEV = 1.6021e-15
        self.RYMEV = (RY) / (ONEMEV)

        v00 = 250
        v11 = 250
        l00 = 45
        l11 = 100

        self.d = 100
        self.v0 = v00/self.RYMEV
        self.v1 = v11/self.RYMEV
        self.l0 = l00/self.ABA
        self.l1 = l11/self.ABA
        self.passo = 1/self.d
        self.j = 0

    def funp(self,e):
        k1 = math.sqrt(self.v0 - e)
        k2 = math.sqrt(e)
        k3 = math.sqrt(self.v1 - e)
        l2 = 100/self.ABA + math.cos(self.time/10) * 50/self.ABA

        m = self.l0 + self.l1
        n = m + l2

        cos_k2l1 = math.cos(k2*self.l1)
        sin_k2l1 = math.sin(k2*self.l1)
        sin_k2m = math.sin(k2*m)
        cos_k2m = math.cos(k2*m)
        sin_k2n = math.sin(k2*n)
        cos_k2n = math.cos(k2*n)
        tan_k2l1 = math.tan(k2*self.l1)
        tan_k2n = math.tan(k2*n)
        exp_k1l1 = math.exp(k1*self.l1)
        exp_k3l1 = math.exp(-k3*self.l1)
        exp_k3m = math.exp(-k3*m)
        exp_k3n = math.exp(-k3*n)
        exp_k1m = math.exp(k1*m)

        w1 = (k2)  / (cos_k2l1)
        w2 = (-k2)*(tan_k2l1)*(exp_k1l1) - k1*(exp_k1l1)
        w3 = (-k2)*(tan_k2l1)*(exp_k3l1) + k3*(exp_k3l1)
        w4 = (-k1)*(exp_k3m) - k3*(exp_k3m)
        w5 = (k1)*(cos_k2m) + k2*(sin_k2m)
        w6 = (k1)*(sin_k2m) - k2*(cos_k2m)
        w7 = (k2)/(math.cos(k2*n))
        w8 = (-k2)*(exp_k3n)*(tan_k2n) + k3*(exp_k3n)
        w9 = (k2)*(cos_k2l1)/(k1) + (sin_k2l1)
        w10 = (w1)*(exp_k1l1)/(w9) + w2
        w11 = (w1)*(exp_k3l1)/(w9) + w3
        w12 = (-w11)*(exp_k1m)/(w10) + exp_k3m
        w13 = (w4)*(cos_k2m)/(w12) + (w5)
        w14 = (w4)*(sin_k2m)/(w12) + (w6)
        w15 = ((-cos_k2n)*w14)/(w13) + (sin_k2n)
        w16 = (w7)*(exp_k3n)/(w15) + (w8)

        return  k1*w9*w10*w12*w13*w15*w16


    def zbrent(self, a, b):
        fa = self.funp(a)
        fb = self.funp(b)
        c = a
        fc = fa
        d = b - a
        e = d
        tol=1e-18
        while abs(b - a) > tol:
            if abs(fc - fb) <= tol:
                c = a
                fc = fa
                d = b - a
                e = d
            if abs(fc) < abs(fb):
                a = b
                b = c
                c = a
                fa = fb
                fb = fc
                fc = fa

            tol1 = 2 * 1e-10 * abs(b) * 0.5 * tol
            xm = 0.5 * (c - b)

            if abs(xm) <= tol1 or fb == 0:
                return b

            if abs(e) >= tol1 and abs(fa) > abs(fb):
                s = fb / fa
                if a == c:
                    p = 2 * xm * s
                    q = -s
                else:
                    q = fa / fc
                    r = fb / fc
                    p = s * (2 * xm * q * (q - r) - (b - a) * (r - 1))
                    q = (q - 1) * (r - 1) * (s - 1)
                if p > 0:
                    q = -q
                    p = abs(p)
                    if 2 * p < min(3 * xm * q - abs(tol1 * q), abs(e * q)):
                        e = d
                        d = p / q
                    else:
                        d = xm
                        e = d
                else:
                    d = xm
                    e = d
                a = b
                fa = fb
                if d >= 0:
                    b += tol1
                else:
                    b -= tol1
            fb = self.funp(b)
        return b



    def calc_energy(self):
        enp = {}
        j = 0
        for i in range(1, int((self.d*self.v0 - 0.0001))):
            a = (i)/(self.d)
            b = (i)/(self.d) + self.passo
            f1 = self.funp(a)
            f2 = self.funp(b)
            if( f1*f2 <= 0 ):
                enp[j] = round(self.RYMEV*self.zbrent(a , b),0)
                j+=1
        print(enp)
        return enp