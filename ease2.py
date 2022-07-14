import math

PI = math.pi
TAU = math.tau


class Ease2:
    """
    Easing equations by Robert Penner

    * step - the current time/step of the animation
    * start - the starting value of the property
    * delta - the amount of change between the start and end values, i.e. (end - start)
    * duration - the total the length of time that an animation takes to complete
    """
    
    #############################################################
    # LINEAR
    #############################################################
    @staticmethod
    def linear(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return delta * step + start

    #############################################################
    # SINUSOIDAL
    #############################################################
    @staticmethod
    def in_sine(step, start, delta, duration):
        step = min(step / duration, 1.0)
        if step == 1.0:
            return start + delta
        return delta * (1 - math.cos(step * (PI / 2))) + start

    @staticmethod
    def out_sine(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return delta * math.sin(step * (PI / 2)) + start

    @staticmethod
    def in_out_sine(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return delta / 2 * (1 - math.cos(PI * step)) + start

    #############################################################
    # QUADRATIC
    #############################################################
    @staticmethod
    def in_quad(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return delta * math.pow(step, 2) + start

    @staticmethod
    def out_quad(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return -delta * step * (step - 2) + start

    @staticmethod
    def in_out_quad(step, start, delta, duration):
        step /= duration / 2
        if step < 1:
            return delta / 2 * math.pow(step, 2) + start

        step = min(step - 1, 1.0)
        return -delta / 2 * (step * (step - 2) - 1) + start

    #############################################################
    # CUBIC
    #############################################################
    @staticmethod
    def in_cubic(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return delta * math.pow(step, 3) + start

    @staticmethod
    def out_cubic(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return delta * (math.pow(step - 1, 3) + 1) + start

    @staticmethod
    def in_out_cubic(step, start, delta, duration):
        step = min(step / (duration / 2), 2.0)
        if step < 1:
            return delta / 2 * math.pow(step, 3) + start

        return delta / 2 * (math.pow(step - 2, 3) + 2) + start

    #############################################################
    # QUARTIC
    #############################################################
    @staticmethod
    def in_quart(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return delta * math.pow(step, 4) + start

    @staticmethod
    def out_quart(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return -delta * (math.pow(step - 1, 4) - 1) + start

    @staticmethod
    def in_out_quart(step, start, delta, duration):
        step = min(step / (duration / 2), 2.0)
        if step < 1:
            return delta / 2 * math.pow(step, 4) + start

        return -delta / 2 * (math.pow(step - 2, 4) - 2) + start

    #############################################################
    # QUINTIC
    #############################################################
    @staticmethod
    def in_quint(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return delta * math.pow(step, 5) + start

    @staticmethod
    def out_quint(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return delta * (math.pow(step - 1, 5) + 1) + start

    @staticmethod
    def in_out_quint(step, start, delta, duration):
        step = min(step / (duration / 2), 2.0)
        if step < 1:
            return delta / 2 * math.pow(step, 5) + start

        return delta / 2 * (math.pow(step - 2, 5) + 2) + start

    #############################################################
    # EXPONENTIAL
    #############################################################
    @staticmethod
    def in_expo(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return delta * math.pow(2, 10 * (step - 1)) + start

    @staticmethod
    def out_expo(step, start, delta, duration):
        step = min(step / duration, 1.0)
        if step == 1.0:
            return start + delta
        return delta * (1 - math.pow(2, -10 * step)) + start

    @staticmethod
    def in_out_expo(step, start, delta, duration):
        step = min(step / (duration / 2), 2.0)
        if step == 0.0:
            return start
        elif 0.0 < step < 1.0:
            return delta / 2 * math.pow(2, 10 * (step - 1)) + start
        elif step == 2.0:
            return start + delta

        return delta / 2 * (2 - math.pow(2, -10 * (step - 1))) + start

    #############################################################
    # CIRCULAR
    #############################################################
    @staticmethod
    def in_circ(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return -delta * (math.sqrt(1 - math.pow(step, 2)) - 1) + start

    @staticmethod
    def out_circ(step, start, delta, duration):
        step = min(step / duration, 1.0)
        return delta * math.sqrt(1 - math.pow(step - 1, 2)) + start

    @staticmethod
    def in_out_circ(step, start, delta, duration):
        step = min(step / (duration / 2), 2.0)
        if step < 1:
            return delta / 2 * (1 - math.sqrt(1 - math.pow(step, 2))) + start

        return delta / 2 * (math.sqrt(1 - math.pow(step - 2, 2)) + 1) + start

    #############################################################################
    # SPECIAL FUNCTIONS
    # From: https://web.archive.org/web/20181122181216/http://kodhus.com/easings/
    # P.S. The original link is dead :(
    #############################################################################
    @staticmethod
    def in_back(step, start, delta, duration):
        C1 = 1.70158
        step = min(step / duration, 1.0)
        if step == 1.0:
            return start + delta
        return delta * math.pow(step, 2) * ((C1 + 1) * step - C1) + start

    @staticmethod
    def out_back(step, start, delta, duration):
        C1 = 1.70158
        step = min(step / duration, 1.0)
        if step == 1.0:
            return start + delta
        return delta * (math.pow(step - 1, 2) * ((C1 + 1) * (step - 1) + C1) + 1) + start

    @staticmethod
    def in_out_back(step, start, delta, duration):
        C2 = 2.5949095
        step = min(step / (duration / 2), 2.0)

        if step < 1:
            return delta / 2 * (step * step * ((C2 + 1) * step - C2)) + start

        step -= 2
        return delta / 2 * (step * step * ((C2 + 1) * step + C2) + 2) + start

    @staticmethod
    def in_elastic(step, start, delta, duration):
        s = 1.70158
        p, a = 0, delta

        if step == 0:
            return start

        step = min(step / duration, 1.0)
        if step == 1:
            return start + delta

        if p == 0:
            p = duration * .3

        if a < math.fabs(delta):
            a = delta
            s = p / 4
        else:
            s = p / TAU * math.asin(delta / a)

        step -= 1
        return -(a * math.pow(2, 10 * step) * math.sin((step * duration - s) * TAU / p)) + start

    @staticmethod
    def out_elastic(step, start, delta, duration):
        s = 1.70158
        p, a = 0, delta

        if step == 0:
            return start

        step = min(step / duration, 1.0)
        if step == 1:
            return start + delta

        if p == 0:
            p = duration * .3

        if a < math.fabs(delta):
            a = delta
            s = p / 4
        else:
            s = p / TAU * math.asin(delta / a)

        return a * math.pow(2, -10 * step) * math.sin((step * duration - s) * TAU / p) + delta + start

    @staticmethod
    def in_out_elastic(step, start, delta, duration):
        s = 1.70158
        p, a = 0, delta

        if step == 0:
            return start

        step = min(step / (duration / 2), 2.0)
        if step == 2:
            return start + delta

        if p == 0:
            p = duration * .3 * 1.5

        if a < math.fabs(delta):
            a = delta
            s = p / 4
        else:
            s = p / TAU * math.asin(delta / a)

        if step < 1:
            step -= 1
            return -.5 * a * math.pow(2, 10 * step) * math.sin((step * duration - s) * TAU / p) + start

        step -= 1
        return a * math.pow(2, -10 * step) * math.sin((step * duration - s) * TAU / p) * .5 + delta + start

    @staticmethod
    def in_bounce(step, start, delta, duration):
        return delta - Ease2.out_bounce(duration - step, 0, delta, duration) + start

    @staticmethod
    def out_bounce(step, start, delta, duration):
        step = min(step / duration, 1.0)

        if step < 0.0:
            step = 0.0

        if step < (1 / 2.75):
            return delta * (7.5625 * math.pow(step, 2)) + start
        elif step < (2 / 2.75):
            return delta * (7.5625 * math.pow(step - (1.5 / 2.75), 2) + .75) + start
        elif step < (2.5 / 2.75):
            return delta * (7.5625 * math.pow(step - (2.25 / 2.75), 2) + .9375) + start
        else:
            return delta * (7.5625 * math.pow(step - (2.625 / 2.75), 2) + .984375) + start

    @staticmethod
    def in_out_bounce(step, start, delta, duration):
        if step < duration / 2:
            return Ease2.in_bounce(step * 2, 0, delta, duration) * .5 + start
        return Ease2.out_bounce(step * 2 - duration, 0, delta, duration) * .5 + delta * .5 + start
