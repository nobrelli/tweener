import math

PI = math.pi
TAU = math.tau


class Ease2:
    """Easing equations by Robert Penner"""
    #############################################################
    # LINEAR
    #############################################################
    @staticmethod
    def linear(t, b, c, d):
        t = min(t / d, 1.0)
        return c * t + b

    #############################################################
    # SINUSOIDAL
    #############################################################
    @staticmethod
    def in_sine(t, b, c, d):
        t = min(t / d, 1.0)
        if t == 1.0:
            return b + c
        return c * (1 - math.cos(t * (PI / 2))) + b

    @staticmethod
    def out_sine(t, b, c, d):
        t = min(t / d, 1.0)
        return c * math.sin(t * (PI / 2)) + b

    @staticmethod
    def in_out_sine(t, b, c, d):
        t = min(t / d, 1.0)
        return c / 2 * (1 - math.cos(PI * t)) + b

    #############################################################
    # QUADRATIC
    #############################################################
    @staticmethod
    def in_quad(t, b, c, d):
        t = min(t / d, 1.0)
        return c * math.pow(t, 2) + b

    @staticmethod
    def out_quad(t, b, c, d):
        t = min(t / d, 1.0)
        return -c * t * (t - 2) + b

    @staticmethod
    def in_out_quad(t, b, c, d):
        t /= d / 2
        if t < 1:
            return c / 2 * math.pow(t, 2) + b

        t = min(t - 1, 1.0)
        return -c / 2 * (t * (t - 2) - 1) + b

    #############################################################
    # CUBIC
    #############################################################
    @staticmethod
    def in_cubic(t, b, c, d):
        t = min(t / d, 1.0)
        return c * math.pow(t, 3) + b

    @staticmethod
    def out_cubic(t, b, c, d):
        t = min(t / d, 1.0)
        return c * (math.pow(t - 1, 3) + 1) + b

    @staticmethod
    def in_out_cubic(t, b, c, d):
        t = min(t / (d / 2), 2.0)
        if t < 1:
            return c / 2 * math.pow(t, 3) + b

        return c / 2 * (math.pow(t - 2, 3) + 2) + b

    #############################################################
    # QUARTIC
    #############################################################
    @staticmethod
    def in_quart(t, b, c, d):
        t = min(t / d, 1.0)
        return c * math.pow(t, 4) + b

    @staticmethod
    def out_quart(t, b, c, d):
        t = min(t / d, 1.0)
        return -c * (math.pow(t - 1, 4) - 1) + b

    @staticmethod
    def in_out_quart(t, b, c, d):
        t = min(t / (d / 2), 2.0)
        if t < 1:
            return c / 2 * math.pow(t, 4) + b

        return -c / 2 * (math.pow(t - 2, 4) - 2) + b

    #############################################################
    # QUINTIC
    #############################################################
    @staticmethod
    def in_quint(t, b, c, d):
        t = min(t / d, 1.0)
        return c * math.pow(t, 5) + b

    @staticmethod
    def out_quint(t, b, c, d):
        t = min(t / d, 1.0)
        return c * (math.pow(t - 1, 5) + 1) + b

    @staticmethod
    def in_out_quint(t, b, c, d):
        t = min(t / (d / 2), 2.0)
        if t < 1:
            return c / 2 * math.pow(t, 5) + b

        return c / 2 * (math.pow(t - 2, 5) + 2) + b

    #############################################################
    # EXPONENTIAL
    #############################################################
    @staticmethod
    def in_expo(t, b, c, d):
        t = min(t / d, 1.0)
        return c * math.pow(2, 10 * (t - 1)) + b

    @staticmethod
    def out_expo(t, b, c, d):
        t = min(t / d, 1.0)
        if t == 1.0:
            return b + c
        return c * (1 - math.pow(2, -10 * t)) + b

    @staticmethod
    def in_out_expo(t, b, c, d):
        t = min(t / (d / 2), 2.0)
        if t == 0.0:
            return b
        elif 0.0 < t < 1.0:
            return c / 2 * math.pow(2, 10 * (t - 1)) + b
        elif t == 2.0:
            return b + c

        return c / 2 * (2 - math.pow(2, -10 * (t - 1))) + b

    #############################################################
    # CIRCULAR
    #############################################################
    @staticmethod
    def in_circ(t, b, c, d):
        t = min(t / d, 1.0)
        return -c * (math.sqrt(1 - math.pow(t, 2)) - 1) + b

    @staticmethod
    def out_circ(t, b, c, d):
        t = min(t / d, 1.0)
        return c * math.sqrt(1 - math.pow(t - 1, 2)) + b

    @staticmethod
    def in_out_circ(t, b, c, d):
        t = min(t / (d / 2), 2.0)
        if t < 1:
            return c / 2 * (1 - math.sqrt(1 - math.pow(t, 2))) + b

        return c / 2 * (math.sqrt(1 - math.pow(t - 2, 2)) + 1) + b

    #############################################################################
    # SPECIAL FUNCTIONS
    # From: https://web.archive.org/web/20181122181216/http://kodhus.com/easings/
    # P.S. The original link is dead :(
    #############################################################################
    @staticmethod
    def in_back(t, b, c, d):
        C1 = 1.70158
        t = min(t / d, 1.0)
        if t == 1.0:
            return b + c
        return c * math.pow(t, 2) * ((C1 + 1) * t - C1) + b

    @staticmethod
    def out_back(t, b, c, d):
        C1 = 1.70158
        t = min(t / d, 1.0)
        if t == 1.0:
            return b + c
        return c * (math.pow(t - 1, 2) * ((C1 + 1) * (t - 1) + C1) + 1) + b

    @staticmethod
    def in_out_back(t, b, c, d):
        C2 = 2.5949095
        t = min(t / (d / 2), 2.0)

        if t < 1:
            return c / 2 * (t * t * ((C2 + 1) * t - C2)) + b

        t -= 2
        return c / 2 * (t * t * ((C2 + 1) * t + C2) + 2) + b

    @staticmethod
    def in_elastic(t, b, c, d):
        s = 1.70158
        p, a = 0, c

        if t == 0:
            return b

        t = min(t / d, 1.0)
        if t == 1:
            return b + c

        if p == 0:
            p = d * .3

        if a < math.fabs(c):
            a = c
            s = p / 4
        else:
            s = p / TAU * math.asin(c / a)

        t -= 1
        return -(a * math.pow(2, 10 * t) * math.sin((t * d - s) * TAU / p)) + b

    @staticmethod
    def out_elastic(t, b, c, d):
        s = 1.70158
        p, a = 0, c

        if t == 0:
            return b

        t = min(t / d, 1.0)
        if t == 1:
            return b + c

        if p == 0:
            p = d * .3

        if a < math.fabs(c):
            a = c
            s = p / 4
        else:
            s = p / TAU * math.asin(c / a)

        return a * math.pow(2, -10 * t) * math.sin((t * d - s) * TAU / p) + c + b

    @staticmethod
    def in_out_elastic(t, b, c, d):
        s = 1.70158
        p, a = 0, c

        if t == 0:
            return b

        t = min(t / (d / 2), 2.0)
        if t == 2:
            return b + c

        if p == 0:
            p = d * .3 * 1.5

        if a < math.fabs(c):
            a = c
            s = p / 4
        else:
            s = p / TAU * math.asin(c / a)

        if t < 1:
            t -= 1
            return -.5 * a * math.pow(2, 10 * t) * math.sin((t * d - s) * TAU / p) + b

        t -= 1
        return a * math.pow(2, -10 * t) * math.sin((t * d - s) * TAU / p) * .5 + c + b

    @staticmethod
    def in_bounce(t, b, c, d):
        return c - Ease2.out_bounce(d - t, 0, c, d) + b

    @staticmethod
    def out_bounce(t, b, c, d):
        t = min(t / d, 1.0)

        if t < 0.0:
            t = 0.0

        if t < (1 / 2.75):
            return c * (7.5625 * math.pow(t, 2)) + b
        elif t < (2 / 2.75):
            return c * (7.5625 * math.pow(t - (1.5 / 2.75), 2) + .75) + b
        elif t < (2.5 / 2.75):
            return c * (7.5625 * math.pow(t - (2.25 / 2.75), 2) + .9375) + b
        else:
            return c * (7.5625 * math.pow(t - (2.625 / 2.75), 2) + .984375) + b

    @staticmethod
    def in_out_bounce(t, b, c, d):
        if t < d / 2:
            return Ease2.in_bounce(t * 2, 0, c, d) * .5 + b
        return Ease2.out_bounce(t * 2 - d, 0, c, d) * .5 + c * .5 + b
