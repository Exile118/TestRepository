"""
Calculator Module
提供基本的数学运算功能
"""


class Calculator:
    """一个简单的计算器类"""

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        加法运算
        
        Args:
            a: 第一个数
            b: 第二个数
            
        Returns:
            两数之和
        """
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """
        减法运算
        
        Args:
            a: 被减数
            b: 减数
            
        Returns:
            两数之差
        """
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """
        乘法运算
        
        Args:
            a: 第一个数
            b: 第二个数
            
        Returns:
            两数之积
        """
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """
        除法运算
        
        Args:
            a: 被除数
            b: 除数
            
        Returns:
            两数之商
            
        Raises:
            ValueError: 当除数为0时
        """
        if b == 0:
            raise ValueError("除数不能为0")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        """
        幂运算
        
        Args:
            a: 底数
            b: 指数
            
        Returns:
            a的b次方
        """
        return a ** b

    @staticmethod
    def square_root(a: float) -> float:
        """
        平方根运算
        
        Args:
            a: 被开方数
            
        Returns:
            a的平方根
            
        Raises:
            ValueError: 当a为负数时
        """
        if a < 0:
            raise ValueError("不能对负数开平方根")
        return a ** 0.5
