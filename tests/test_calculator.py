"""
Calculator Tests
完整的单元测试套件
"""

import pytest
from src.calculator import Calculator


class TestCalculator:
    """Calculator 类的测试套件"""

    def setup_method(self):
        """每个测试方法前的设置"""
        self.calc = Calculator()

    # 加法测试
    def test_add_positive_numbers(self):
        """测试正数加法"""
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(10, 20) == 30

    def test_add_negative_numbers(self):
        """测试负数加法"""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.add(-10, 5) == -5

    def test_add_zero(self):
        """测试零的加法"""
        assert self.calc.add(0, 5) == 5
        assert self.calc.add(5, 0) == 5

    def test_add_floats(self):
        """测试浮点数加法"""
        result = self.calc.add(1.5, 2.5)
        assert abs(result - 4.0) < 0.0001

    # 减法测试
    def test_subtract_positive_numbers(self):
        """测试正数减法"""
        assert self.calc.subtract(10, 5) == 5
        assert self.calc.subtract(20, 8) == 12

    def test_subtract_negative_numbers(self):
        """测试负数减法"""
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.subtract(5, -3) == 8

    def test_subtract_zero(self):
        """测试零的减法"""
        assert self.calc.subtract(5, 0) == 5
        assert self.calc.subtract(0, 5) == -5

    # 乘法测试
    def test_multiply_positive_numbers(self):
        """测试正数乘法"""
        assert self.calc.multiply(5, 3) == 15
        assert self.calc.multiply(10, 10) == 100

    def test_multiply_negative_numbers(self):
        """测试负数乘法"""
        assert self.calc.multiply(-5, 3) == -15
        assert self.calc.multiply(-5, -3) == 15

    def test_multiply_by_zero(self):
        """测试乘以零"""
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.multiply(0, 10) == 0

    def test_multiply_floats(self):
        """测试浮点数乘法"""
        result = self.calc.multiply(1.5, 2.0)
        assert abs(result - 3.0) < 0.0001

    # 除法测试
    def test_divide_positive_numbers(self):
        """测试正数除法"""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(15, 3) == 5

    def test_divide_negative_numbers(self):
        """测试负数除法"""
        assert self.calc.divide(-10, 2) == -5
        assert self.calc.divide(-10, -2) == 5

    def test_divide_by_zero_raises_error(self):
        """测试除以零抛出异常"""
        with pytest.raises(ValueError, match="除数不能为0"):
            self.calc.divide(10, 0)

    def test_divide_floats(self):
        """测试浮点数除法"""
        result = self.calc.divide(5.0, 2.0)
        assert abs(result - 2.5) < 0.0001

    # 幂运算测试
    def test_power_positive_exponent(self):
        """测试正指数幂运算"""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 2) == 25

    def test_power_zero_exponent(self):
        """测试零指数幂运算"""
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(100, 0) == 1

    def test_power_negative_exponent(self):
        """测试负指数幂运算"""
        assert self.calc.power(2, -1) == 0.5
        result = self.calc.power(4, -2)
        assert abs(result - 0.0625) < 0.0001

    def test_power_fractional_exponent(self):
        """测试分数指数幂运算"""
        assert self.calc.power(4, 0.5) == 2
        assert self.calc.power(27, 1/3) - 3 < 0.0001

    # 平方根测试
    def test_square_root_positive_numbers(self):
        """测试正数平方根"""
        assert self.calc.square_root(4) == 2
        assert self.calc.square_root(9) == 3
        assert self.calc.square_root(16) == 4

    def test_square_root_zero(self):
        """测试零的平方根"""
        assert self.calc.square_root(0) == 0

    def test_square_root_negative_raises_error(self):
        """测试负数平方根抛出异常"""
        with pytest.raises(ValueError, match="不能对负数开平方根"):
            self.calc.square_root(-4)

    def test_square_root_floats(self):
        """测试浮点数平方根"""
        result = self.calc.square_root(2)
        assert abs(result - 1.414213562) < 0.0001


# 参数化测试示例
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, -50, 50),
    (1.5, 2.5, 4.0),
])
def test_add_parametrized(a, b, expected):
    """参数化测试加法"""
    calc = Calculator()
    assert calc.add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (6, 2, 3),
    (10, 5, 2),
    (-10, 2, -5),
    (7, 2, 3.5),
])
def test_divide_parametrized(a, b, expected):
    """参数化测试除法"""
    calc = Calculator()
    assert calc.divide(a, b) == expected
