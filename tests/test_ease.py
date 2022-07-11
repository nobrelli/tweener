from unittest import TestCase
from ease import Ease


class TestEase(TestCase):
    def test_linear(self):
        self.assertEqual(0.0, Ease.linear(0.0))
        self.assertEqual(1.0, Ease.linear(1.0))

    def test_in_sine(self):
        self.assertEqual(0.0, Ease.in_sine(0.0))
        self.assertEqual(1.0, Ease.in_sine(1.0))

    def test_out_sine(self):
        self.assertEqual(0.0, Ease.out_sine(0.0))
        self.assertEqual(1.0, Ease.out_sine(1.0))

    def test_in_out_sine(self):
        self.assertEqual(0.0, Ease.in_out_sine(0.0))
        self.assertEqual(1.0, Ease.in_out_sine(1.0))

    def test_in_quad(self):
        self.assertEqual(0.0, Ease.in_quad(0.0))
        self.assertEqual(1.0, Ease.in_quad(1.0))

    def test_out_quad(self):
        self.assertEqual(0.0, Ease.out_quad(0.0))
        self.assertEqual(1.0, Ease.out_quad(1.0))

    def test_in_out_quad(self):
        self.assertEqual(0.0, Ease.in_out_quad(0.0))
        self.assertEqual(1.0, Ease.in_out_quad(1.0))

    def test_in_cubic(self):
        self.assertEqual(0.0, Ease.in_cubic(0.0))
        self.assertEqual(1.0, Ease.in_cubic(1.0))

    def test_out_cubic(self):
        self.assertEqual(0.0, Ease.out_cubic(0.0))
        self.assertEqual(1.0, Ease.out_cubic(1.0))

    def test_in_out_cubic(self):
        self.assertEqual(0.0, Ease.in_out_cubic(0.0))
        self.assertEqual(1.0, Ease.in_out_cubic(1.0))

    def test_in_quart(self):
        self.assertEqual(0.0, Ease.in_quart(0.0))
        self.assertEqual(1.0, Ease.in_quart(1.0))

    def test_out_quart(self):
        self.assertEqual(0.0, Ease.out_quart(0.0))
        self.assertEqual(1.0, Ease.out_quart(1.0))

    def test_in_out_quart(self):
        self.assertEqual(0.0, Ease.in_out_quart(0.0))
        self.assertEqual(1.0, Ease.in_out_quart(1.0))

    def test_in_quint(self):
        self.assertEqual(0.0, Ease.in_quint(0.0))
        self.assertEqual(1.0, Ease.in_quint(1.0))

    def test_out_quint(self):
        self.assertEqual(0.0, Ease.out_quint(0.0))
        self.assertEqual(1.0, Ease.out_quint(1.0))

    def test_in_out_quint(self):
        self.assertEqual(0.0, Ease.in_out_quint(0.0))
        self.assertEqual(1.0, Ease.in_out_quint(1.0))

    def test_in_expo(self):
        self.assertEqual(0.0, Ease.in_expo(0.0))
        self.assertEqual(1.0, Ease.in_expo(1.0))

    def test_out_expo(self):
        self.assertEqual(0.0, Ease.out_expo(0.0))
        self.assertEqual(1.0, Ease.out_expo(1.0))

    def test_in_out_expo(self):
        self.assertEqual(0.0, Ease.in_out_expo(0.0))
        self.assertEqual(1.0, Ease.in_out_expo(1.0))

    def test_in_circ(self):
        self.assertEqual(0.0, Ease.in_circ(0.0))
        self.assertEqual(1.0, Ease.in_circ(1.0))

    def test_out_circ(self):
        self.assertEqual(0.0, Ease.out_circ(0.0))
        self.assertEqual(1.0, Ease.out_circ(1.0))

    def test_in_out_circ(self):
        self.assertEqual(0.0, Ease.in_out_circ(0.0))
        self.assertEqual(1.0, Ease.in_out_circ(1.0))

    def test_in_back(self):
        self.assertEqual(0.0, Ease.in_back(0.0))
        self.assertEqual(1.0, Ease.in_back(1.0))

    def test_out_back(self):
        self.assertEqual(0.0, Ease.out_back(0.0))
        self.assertEqual(1.0, Ease.out_back(1.0))

    def test_in_out_back(self):
        self.assertEqual(0.0, Ease.in_out_back(0.0))
        self.assertEqual(1.0, Ease.in_out_back(1.0))

    def test_in_elastic(self):
        self.assertEqual(0.0, Ease.in_elastic(0.0))
        self.assertEqual(1.0, Ease.in_elastic(1.0))

    def test_out_elastic(self):
        self.assertEqual(0.0, Ease.out_elastic(0.0))
        self.assertEqual(1.0, Ease.out_elastic(1.0))

    def test_in_out_elastic(self):
        self.assertEqual(0.0, Ease.in_out_elastic(0.0))
        self.assertEqual(1.0, Ease.in_out_elastic(1.0))

    def test_in_bounce(self):
        self.assertEqual(0.0, Ease.in_bounce(0.0))
        self.assertEqual(1.0, Ease.in_bounce(1.0))

    def test_out_bounce(self):
        self.assertEqual(0.0, Ease.out_bounce(0.0))
        self.assertEqual(1.0, Ease.out_bounce(1.0))

    def test_in_out_bounce(self):
        self.assertEqual(0.0, Ease.in_out_bounce(0.0))
        self.assertEqual(1.0, Ease.in_out_bounce(1.0))
