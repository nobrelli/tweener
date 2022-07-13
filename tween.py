import time
from enum import Enum, auto
from ease import Ease
from collections.abc import Callable


class Easing(Enum):
    LINEAR = auto()
    SINE = auto()
    QUAD = auto()
    CUBIC = auto()
    QUART = auto()
    QUINT = auto()
    EXPO = auto()
    CIRC = auto()
    BACK = auto()
    ELASTIC = auto()
    BOUNCE = auto()


class EasingMode(Enum):
    IN = auto()
    OUT = auto()
    IN_OUT = auto()


class Tween:
    def __init__(self,
                 begin: float = 0.0, end: float = 1.0,
                 duration: int = 600,
                 easing: Easing = Easing.LINEAR,
                 easing_mode: EasingMode = EasingMode.IN,
                 boomerang: bool = False,
                 loop: bool = False,
                 reps: int = 0):

        self._begin = begin
        self._origin = begin
        self._end = end
        self._duration = duration
        self._boomerang = boomerang
        self._loop = loop
        self._reps = reps
        self._count = 1

        self._easing = easing
        self._easing_mode = easing_mode

        self._pause_start = 0
        self._pause_dur = 0
        self._paused = False

        self._start_time = 0
        self._animating = False
        self._value = self._begin
        self._step = 0

        # Determine which function to use
        self._ease: Callable[[float], float]
        self._eval_func()

    def _eval_func(self):
        match self._easing:
            case Easing.SINE:
                match self._easing_mode:
                    case EasingMode.IN:
                        self._ease = Ease.in_sine
                    case EasingMode.OUT:
                        self._ease = Ease.out_sine
                    case EasingMode.IN_OUT:
                        self._ease = Ease.in_out_sine
            case Easing.QUAD:
                match self._easing_mode:
                    case EasingMode.IN:
                        self._ease = Ease.in_quad
                    case EasingMode.OUT:
                        self._ease = Ease.out_quad
                    case EasingMode.IN_OUT:
                        self._ease = Ease.in_out_quad
            case Easing.CUBIC:
                match self._easing_mode:
                    case EasingMode.IN:
                        self._ease = Ease.in_cubic
                    case EasingMode.OUT:
                        self._ease = Ease.out_cubic
                    case EasingMode.IN_OUT:
                        self._ease = Ease.in_out_cubic
            case Easing.QUART:
                match self._easing_mode:
                    case EasingMode.IN:
                        self._ease = Ease.in_quart
                    case EasingMode.OUT:
                        self._ease = Ease.out_quart
                    case EasingMode.IN_OUT:
                        self._ease = Ease.in_out_quart
            case Easing.QUINT:
                match self._easing_mode:
                    case EasingMode.IN:
                        self._ease = Ease.in_quint
                    case EasingMode.OUT:
                        self._ease = Ease.out_quint
                    case EasingMode.IN_OUT:
                        self._ease = Ease.in_out_quint
            case Easing.EXPO:
                match self._easing_mode:
                    case EasingMode.IN:
                        self._ease = Ease.in_expo
                    case EasingMode.OUT:
                        self._ease = Ease.out_expo
                    case EasingMode.IN_OUT:
                        self._ease = Ease.in_out_expo
            case Easing.CIRC:
                match self._easing_mode:
                    case EasingMode.IN:
                        self._ease = Ease.in_circ
                    case EasingMode.OUT:
                        self._ease = Ease.out_circ
                    case EasingMode.IN_OUT:
                        self._ease = Ease.in_out_circ
            case Easing.BACK:
                match self._easing_mode:
                    case EasingMode.IN:
                        self._ease = Ease.in_back
                    case EasingMode.OUT:
                        self._ease = Ease.out_back
                    case EasingMode.IN_OUT:
                        self._ease = Ease.in_out_back
            case Easing.ELASTIC:
                match self._easing_mode:
                    case EasingMode.IN:
                        self._ease = Ease.in_elastic
                    case EasingMode.OUT:
                        self._ease = Ease.out_elastic
                    case EasingMode.IN_OUT:
                        self._ease = Ease.in_out_elastic
            case Easing.BOUNCE:
                match self._easing_mode:
                    case EasingMode.IN:
                        self._ease = Ease.in_bounce
                    case EasingMode.OUT:
                        self._ease = Ease.out_bounce
                    case EasingMode.IN_OUT:
                        self._ease = Ease.in_out_bounce
            case _:
                self._ease = Ease.linear

    def start(self):
        if not self.animating:
            self._start_time = time.time()
            self._animating = True

    @property
    def easing_mode(self):
        return self._easing_mode

    @easing_mode.setter
    def easing_mode(self, value):
        self._easing_mode = value
        self._eval_func()

    @property
    def step(self):
        return self._step

    @property
    def value(self):
        return self._value

    @property
    def animating(self):
        return self._animating

    def pause(self):
        if not self._paused:
            self._paused = True
            self._pause_start = time.time()

    def resume(self):
        if self._paused:
            self._paused = False
            self._pause_dur = time.time() - self._pause_start
            self._start_time += self._pause_dur

    def update(self):
        if self.animating and not self._paused:
            this_time = time.time()
            elapsed = (this_time - self._start_time) * 1000.0  # convert to ms
            self._step = min(elapsed / self._duration, 1.0)
            delta = self._end - self._begin

            # Normalized version
            self._value = self._ease(self.step) * delta + self._begin
            # Absolute version
            # self._value = Ease2.linear(elapsed, self._begin, delta, self._duration)

            # Once this is the end of the animation state...
            if self.step == 1.0:
                if self._boomerang:
                    self._start_time = this_time
                    self._begin, self._end = self._end, self._begin

                    if self.value == self._origin:
                        if self._loop:
                            self._do_loop()
                        else:
                            self._animating = False
                else:
                    if self._loop:
                        self._do_loop()
                    else:
                        self._animating = False

    def _do_loop(self):
        if self._reps == 0:
            self._animating = False
            self.start()
        else:
            if self._count < self._reps:
                self._count += 1
                self._animating = False
                self.start()
            else:
                self._count = 1
                self._animating = False
