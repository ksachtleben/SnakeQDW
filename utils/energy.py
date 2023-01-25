import math

class QuantumEnergy():
    def __init__(self):


        EM0 = 9.1091e-28
        EMB = 0.067 * EM0
        EP0 = 12.9
        HB = 1.0545e-27
        EC = 4.8029e-10

        AB = (HB * HB * EP0) / (EMB * EC * EC)
        RY = (EC * EC) / (2 * EP0 * AB)
        ONEA = 1.0e-8
        ABA = (AB) / (ONEA)

        ONEMEV = 1.6021e-15
        RYMEV = (RY) / (ONEMEV)

        v00 = 250
        v11 = 250
        l00 = 45
        l11 = 100

        d = 1000
        self.v0 = v00/RYMEV
        self.v1 = v11/RYMEV
        self.l0 = l00/ABA
        self.l1 = l11/ABA
        self.l2 = 0/ABA
        self.passo = 1/d
        self.enp = {}
        j = 0

    def funp(self,e):
        k1 = math.sqrt(self.v0 - e)
        k2 = math.sqrt(e)
        k3 = math.sqrt(self.v1 - e)

        m = self.l0 + self.l1
        n = m + self.l2

        w1 = (k2)  / (math.cos(k2*self.l1))
        w2 = (-k2)*(math.tan(k2*self.l1))*(math.exp(k1*self.l1)) - k1*(math.exp(k1*self.l1))
        w3 = (-k2)*(math.tan(k2*self.l1))*(math.exp(-k3*self.l1)) + k3*(math.exp(-k3*self.l1))
        w4 = (-k1)*(math.exp(-k3*m)) - k3*(math.exp(-k3*m))
        w5 = (k1)*(math.cos(k2*m)) + k2*(math.sin(k2*m))
        w6 = (k1)*(math.sin(k2*m)) - k2*(math.cos(k2*m))
        w7 = (k2)/(math.cos(k2*n))
        w8 = (-k2)*(math.exp(-k3*n))*(math.tan(k2*n)) + k3*(math.exp(-k3*n))
        w9 = (k2)*(math.cos(k2*self.l1))/(k1) + (math.sin(k2*self.l1))
        w10 = (w1)*(math.exp(k1*self.l1))/(w9) + w2
        w11 = (w1)*(math.exp(-k3*self.l1))/(w9) + w3
        w12 = (-w11)*(math.exp(k1*m))/(w10) + math.exp(-k3*m)
        w13 = (w4)*(math.cos(k2*m))/(w12) + (w5)
        w14 = (w4)*(math.sin(k2*m))/(w12) + (w6)
        w15 = ((-math.cos(k2*n))*w14)/(w13) + (math.sin(k2*n))
        w16 = (w7)*(math.exp(-k3*n))/(w15) + (w8)

        return  k1*w9*w10*w12*w13*w15*w16

    def zbrent(self, a, b):
        fa = self.funp(a)
        fb = self.funp(b)
        tol = 1.0e-18

        if fa * fb < 0:
            fc = fb
            for i in range(1, 1001):
                if fb * fc > 0:
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

                tol1 = 2 * 1e-10 * abs(b) + 0.5 * tol
                xm = 0.5 * (c - b)

                if abs(xm) <= tol1 or fb == 0:
                    return b

                if abs(e) >= tol1 and abs(fa) > abs(fb):
                    s = fb/fa
                    if a == c:
                        p = 2*xm*s
                        q = -s
                    else:
                        q = fa/fc
                        r = fb/fc
                        p = s*(2*xm*q*(q-r)-(b-a)*(r-1))
                        q = ((q-1)*(r-1)*(s-1))

                    if p > 0:
                        q = -q
                        p = abs(p)
                        if 2*p < min(3*xm*q - abs(tol1*q), abs(e*q)):
                            e = d
                            d = p/q
                        else:
                            d = xm
                            e = d
                    else:
                        d = xm
                        e = d
                    a  = b
                    fa = fb

                    if abs(d) > tol1:
                        b = b + d
                    else:
                        b = b + abs(tol1)*(xm / abs(xm))

                fb = self.funp(b)
        return b

    def calc_energy(self):
        for i in range(1, int((self.d*self.v0 - 0.0001))):
            a = (i)/(self.d)
            b = (i)/(self.d) + self.passo
            f1 = self.funp(a)
            f2 = self.funp(b)
            if( f1*f2 <= 0 ):
                self.enp[j] = self.RYMEV*self.zbrent(a , b)
                j+=1
            
        print(self.enp)
        return self.enp