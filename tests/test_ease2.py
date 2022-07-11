from unittest import TestCase
from ease2 import Ease2


class TestEase2(TestCase):
    def setUp(self):
        self.t = 3000
        self.b = 0
        self.c = 500
        self.d = 3000

    def test_linear(self):
        v = Ease2.linear(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.linear(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_sine(self):
        v = Ease2.in_sine(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_sine(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_out_sine(self):
        v = Ease2.out_sine(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.out_sine(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_out_sine(self):
        v = Ease2.in_out_sine(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_out_sine(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_quad(self):
        v = Ease2.in_quad(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_quad(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_out_quad(self):
        v = Ease2.out_quad(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.out_quad(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_out_quad(self):
        v = Ease2.in_out_quad(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_out_quad(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_cubic(self):
        v = Ease2.in_cubic(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_cubic(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_out_cubic(self):
        v = Ease2.out_cubic(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.out_cubic(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_out_cubic(self):
        v = Ease2.in_out_cubic(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_out_cubic(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_quart(self):
        v = Ease2.in_quart(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_quart(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_out_quart(self):
        v = Ease2.out_quart(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.out_quart(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_out_quart(self):
        v = Ease2.in_out_quart(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_out_quart(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_quint(self):
        v = Ease2.in_quint(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_quint(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_out_quint(self):
        v = Ease2.out_quint(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.out_quint(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_out_quint(self):
        v = Ease2.in_out_quint(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_out_quint(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_expo(self):
        v = Ease2.in_expo(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_expo(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_out_expo(self):
        v = Ease2.out_expo(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.out_expo(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_out_expo(self):
        v = Ease2.in_out_expo(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_out_expo(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_circ(self):
        v = Ease2.in_circ(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_circ(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_out_circ(self):
        v = Ease2.out_circ(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.out_circ(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_out_circ(self):
        v = Ease2.in_out_circ(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_out_circ(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_back(self):
        v = Ease2.in_back(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_back(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_out_back(self):
        v = Ease2.out_back(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.out_back(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_out_back(self):
        v = Ease2.in_out_back(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_out_back(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_elastic(self):
        v = Ease2.in_elastic(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_elastic(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_out_elastic(self):
        v = Ease2.out_elastic(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.out_elastic(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_out_elastic(self):
        v = Ease2.in_out_elastic(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_out_elastic(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_bounce(self):
        v = Ease2.in_bounce(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_bounce(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_out_bounce(self):
        v = Ease2.out_bounce(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.out_bounce(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)

    def test_in_out_bounce(self):
        v = Ease2.in_out_bounce(self.t, self.b, self.c, self.d)
        self.assertEqual(self.c + self.b, v)

        v = Ease2.in_out_bounce(self.t, self.c + self.b, -self.c, self.d)
        self.assertEqual(self.b, v)
