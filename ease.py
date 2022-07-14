import math

PI = math.pi
TAU = math.tau
FBE = 1.70158  # Fallback effect constant


class Ease:
    """
    Easing functions based on https://easings.net/
    
    * time_step - The current time/step of the animation. Domain: **[0.0-1.0]**
    **Returns** a value from range **[0.0-1.0]**
    """
    #############################################################
    # LINEAR
    #############################################################
    @staticmethod
    def linear(time_step: float) -> float:
        return time_step

    #############################################################
    # SINUSOIDAL
    #############################################################
    @staticmethod
    def in_sine(time_step: float) -> float:
        return time_step if time_step == 1.0 else 1 - math.cos((time_step * PI) / 2)

    @staticmethod
    def out_sine(time_step: float) -> float:
        return math.sin((time_step * PI) / 2)

    @staticmethod
    def in_out_sine(time_step: float) -> float:
        return -(math.cos(PI * time_step) - 1) / 2

    #############################################################
    # QUADRATIC
    #############################################################
    @staticmethod
    def in_quad(time_step: float) -> float:
        return math.pow(time_step, 2)

    @staticmethod
    def out_quad(time_step: float) -> float:
        return 1 - math.pow(1 - time_step, 2)

    @staticmethod
    def in_out_quad(time_step: float) -> float:
        return 2 * math.pow(time_step, 2) if time_step < 0.5 \
            else 1 - math.pow(-2 * time_step + 2, 2) / 2

    #############################################################
    # CUBIC
    #############################################################
    @staticmethod
    def in_cubic(time_step: float) -> float:
        return math.pow(time_step, 3)

    @staticmethod
    def out_cubic(time_step: float) -> float:
        return 1 - math.pow(1 - time_step, 3)

    @staticmethod
    def in_out_cubic(time_step: float) -> float:
        return 4 * math.pow(time_step, 3) if time_step < 0.5 \
            else 1 - math.pow(-2 * time_step + 2, 3) / 2

    #############################################################
    # QUARTIC
    #############################################################
    @staticmethod
    def in_quart(time_step: float) -> float:
        return math.pow(time_step, 4)

    @staticmethod
    def out_quart(time_step: float) -> float:
        return 1 - math.pow(1 - time_step, 4)

    @staticmethod
    def in_out_quart(time_step: float) -> float:
        return 8 * math.pow(time_step, 4) if time_step < 0.5 \
            else 1 - math.pow(-2 * time_step + 2, 4) / 2

    #############################################################
    # QUINTIC
    #############################################################
    @staticmethod
    def in_quint(time_step: float) -> float:
        return math.pow(time_step, 5)

    @staticmethod
    def out_quint(time_step: float) -> float:
        return 1 - math.pow(1 - time_step, 5)

    @staticmethod
    def in_out_quint(time_step: float) -> float:
        return 16 * math.pow(time_step, 5) if time_step < 0.5 \
            else 1 - math.pow(-2 * time_step + 2, 5) / 2

    #############################################################
    # EXPONENTIAL
    #############################################################
    @staticmethod
    def in_expo(time_step: float) -> float:
        return time_step if time_step == 0.0 \
            else math.pow(2, 10 * time_step - 10)

    @staticmethod
    def out_expo(time_step: float) -> float:
        return time_step if time_step == 1.0 \
            else 1 - math.pow(2, -10 * time_step)

    @staticmethod
    def in_out_expo(time_step: float) -> float:
        if time_step == 0.0 or time_step == 1.0:
            return time_step
        elif time_step < 0.5:
            return math.pow(2, 20 * time_step - 10) / 2
        else:
            return (2 - math.pow(2, -20 * time_step + 10)) / 2

    #############################################################
    # CIRCULAR
    #############################################################
    @staticmethod
    def in_circ(time_step: float) -> float:
        return 1 - math.sqrt(1 - math.pow(time_step, 2))

    @staticmethod
    def out_circ(time_step: float) -> float:
        return math.sqrt(1 - math.pow(time_step - 1, 2))

    @staticmethod
    def in_out_circ(time_step: float) -> float:
        return (1 - math.sqrt(1 - pow(2 * time_step, 2))) / 2 if time_step < 0.5\
            else (math.sqrt(1 - math.pow(-2 * time_step + 2, 2)) + 1) / 2

    #############################################################
    # SPECIAL FUNCTIONS
    #############################################################
    @staticmethod
    def in_back(time_step: float) -> float:
        return time_step if time_step == 1.0 \
            else (FBE + 1) * math.pow(time_step, 3) - FBE * math.pow(time_step, 2)

    @staticmethod
    def out_back(time_step: float) -> float:
        return time_step if time_step == 0.0 \
            else 1 + (FBE + 1) * math.pow(time_step - 1, 3) + FBE * math.pow(time_step - 1, 2)

    @staticmethod
    def in_out_back(time_step: float) -> float:
        FBE2 = 2.5949095
        return math.pow(2 * time_step, 2) * ((FBE2 + 1) * 2 * time_step - FBE2) / 2 if time_step < 0.5 \
            else (math.pow(2 * time_step - 2, 2) * ((FBE2 + 1) * (time_step * 2 - 2) + FBE2) + 2) / 2

    @staticmethod
    def in_elastic(time_step: float) -> float:
        ANGLE = TAU / 3
        return time_step if time_step == 0 or time_step == 1 \
            else -math.pow(2, 10 * time_step - 10) * math.sin((time_step * 10 - 10.75) * ANGLE)

    @staticmethod
    def out_elastic(time_step: float) -> float:
        ANGLE = TAU / 3
        return time_step if time_step == 0.0 or time_step == 1.0 \
            else math.pow(2, -10 * time_step) * math.sin((time_step * 10 - 0.75) * ANGLE) + 1

    @staticmethod
    def in_out_elastic(time_step: float) -> float:
        ANGLE = TAU / 4.5
        if time_step == 0.0 or time_step == 1.0:
            return time_step
        elif time_step < 0.5:
            return -(math.pow(2, 20 * time_step - 10) * math.sin((20 * time_step - 11.125) * ANGLE)) / 2
        else:
            return math.pow(2, -20 * time_step + 10) * math.sin((20 * time_step - 11.125) * ANGLE) / 2 + 1

    @staticmethod
    def in_bounce(time_step: float) -> float:
        return 1 - Ease.out_bounce(1 - time_step)

    @staticmethod
    def out_bounce(time_step: float) -> float:
        if time_step < (1 / 2.75):
            return 7.5625 * math.pow(time_step, 2)
        elif time_step < (2 / 2.75):
            return 7.5625 * math.pow(time_step - 1.5 / 2.75, 2) + .75
        elif time_step < (2.5 / 2.75):
            return 7.5625 * math.pow(time_step - 2.25 / 2.75, 2) + .9375
        else:
            return 7.5625 * math.pow(time_step - 2.625 / 2.75, 2) + .984375

    @staticmethod
    def in_out_bounce(time_step: float) -> float:
        return (1 - Ease.out_bounce(1 - 2 * time_step)) / 2 if time_step < 0.5 \
            else (1 + Ease.out_bounce(2 * time_step - 1)) / 2
    
