import math

PI = math.pi
TAU = math.tau


class Ease:
    """Taken from: https://easings.net/"""
    #############################################################
    # LINEAR
    #############################################################
    @staticmethod
    def linear(t: float):
        return t

    #############################################################
    # SINUSOIDAL
    #############################################################
    @staticmethod
    def in_sine(t: float):
        return t if t == 1.0 else 1 - math.cos((t * PI) / 2)

    @staticmethod
    def out_sine(t: float):
        return math.sin((t * PI) / 2)

    @staticmethod
    def in_out_sine(t: float):
        return -(math.cos(PI * t) - 1) / 2

    #############################################################
    # QUADRATIC
    #############################################################
    @staticmethod
    def in_quad(t: float):
        return math.pow(t, 2)

    @staticmethod
    def out_quad(t: float):
        return 1 - math.pow(1 - t, 2)

    @staticmethod
    def in_out_quad(t: float):
        return 2 * math.pow(t, 2) if t < 0.5 \
            else 1 - math.pow(-2 * t + 2, 2) / 2

    #############################################################
    # CUBIC
    #############################################################
    @staticmethod
    def in_cubic(t: float):
        return math.pow(t, 3)

    @staticmethod
    def out_cubic(t: float):
        return 1 - math.pow(1 - t, 3)

    @staticmethod
    def in_out_cubic(t: float):
        return 4 * math.pow(t, 3) if t < 0.5 \
            else 1 - math.pow(-2 * t + 2, 3) / 2

    #############################################################
    # QUARTIC
    #############################################################
    @staticmethod
    def in_quart(t: float):
        return math.pow(t, 4)

    @staticmethod
    def out_quart(t: float):
        return 1 - math.pow(1 - t, 4)

    @staticmethod
    def in_out_quart(t: float):
        return 8 * math.pow(t, 4) if t < 0.5 \
            else 1 - math.pow(-2 * t + 2, 4) / 2

    #############################################################
    # QUINTIC
    #############################################################
    @staticmethod
    def in_quint(t: float):
        return math.pow(t, 5)

    @staticmethod
    def out_quint(t: float):
        return 1 - math.pow(1 - t, 5)

    @staticmethod
    def in_out_quint(t: float):
        return 16 * math.pow(t, 5) if t < 0.5 \
            else 1 - math.pow(-2 * t + 2, 5) / 2

    #############################################################
    # EXPONENTIAL
    #############################################################
    @staticmethod
    def in_expo(t: float):
        return t if t == 0.0 else math.pow(2, 10 * t - 10)

    @staticmethod
    def out_expo(t: float):
        return t if t == 1.0 else 1 - math.pow(2, -10 * t)

    @staticmethod
    def in_out_expo(t: float):
        if t == 0.0 or t == 1.0:
            return t
        elif t < 0.5:
            return math.pow(2, 20 * t - 10) / 2
        else:
            return (2 - math.pow(2, -20 * t + 10)) / 2

    #############################################################
    # CIRCULAR
    #############################################################
    @staticmethod
    def in_circ(t: float):
        return 1 - math.sqrt(1 - math.pow(t, 2))

    @staticmethod
    def out_circ(t: float):
        return math.sqrt(1 - math.pow(t - 1, 2))

    @staticmethod
    def in_out_circ(t: float):
        return (1 - math.sqrt(1 - pow(2 * t, 2))) / 2 if t < 0.5\
            else (math.sqrt(1 - math.pow(-2 * t + 2, 2)) + 1) / 2

    #############################################################
    # SPECIAL FUNCTIONS
    #############################################################
    @staticmethod
    def in_back(t: float):
        C1 = 1.70158
        return t if t == 1.0 else (C1 + 1) * math.pow(t, 3) - C1 * math.pow(t, 2)

    @staticmethod
    def out_back(t: float):
        C1 = 1.70158
        return t if t == 0.0 else 1 + (C1 + 1) * math.pow(t - 1, 3) + C1 * math.pow(t - 1, 2)

    @staticmethod
    def in_out_back(t: float):
        C2 = 2.5949095
        return math.pow(2 * t, 2) * ((C2 + 1) * 2 * t - C2) / 2 if t < 0.5 \
            else (math.pow(2 * t - 2, 2) * ((C2 + 1) * (t * 2 - 2) + C2) + 2) / 2

    @staticmethod
    def in_elastic(t: float):
        C4 = TAU / 3
        return t if t == 0 or t == 1 \
            else -math.pow(2, 10 * t - 10) * math.sin((t * 10 - 10.75) * C4)

    @staticmethod
    def out_elastic(t: float):
        C4 = TAU / 3
        return t if t == 0.0 or t == 1.0 \
            else math.pow(2, -10 * t) * math.sin((t * 10 - 0.75) * C4) + 1

    @staticmethod
    def in_out_elastic(t: float):
        C5 = TAU / 4.5
        if t == 0.0 or t == 1.0:
            return t
        elif t < 0.5:
            return -(math.pow(2, 20 * t - 10) * math.sin((20 * t - 11.125) * C5)) / 2
        else:
            return math.pow(2, -20 * t + 10) * math.sin((20 * t - 11.125) * C5) / 2 + 1

    @staticmethod
    def in_bounce(t: float):
        return 1 - Ease.out_bounce(1 - t)

    @staticmethod
    def out_bounce(t: float):
        if t < (1 / 2.75):
            return 7.5625 * math.pow(t, 2)
        elif t < (2 / 2.75):
            return 7.5625 * math.pow(t - 1.5 / 2.75, 2) + .75
        elif t < (2.5 / 2.75):
            return 7.5625 * math.pow(t - 2.25 / 2.75, 2) + .9375
        else:
            return 7.5625 * math.pow(t - 2.625 / 2.75, 2) + .984375

    @staticmethod
    def in_out_bounce(t: float):
        return (1 - Ease.out_bounce(1 - 2 * t)) / 2 if t < 0.5 \
            else (1 + Ease.out_bounce(2 * t - 1)) / 2
    