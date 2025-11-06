"""
Main Module
命令行计算器应用的入口点
"""

from calculator import Calculator


def main():
    """主函数：提供交互式计算器界面"""
    print("=" * 50)
    print("欢迎使用 Python 计算器")
    print("=" * 50)
    print("\n可用操作：")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("5. 幂运算 (^)")
    print("6. 平方根 (√)")
    print("7. 退出 (q)")
    print("=" * 50)

    calc = Calculator()

    while True:
        try:
            operation = input("\n请选择操作 (1-7 或 q): ").strip()

            if operation.lower() == 'q' or operation == '7':
                print("感谢使用，再见！")
                break

            if operation == '6':
                num = float(input("请输入数字: "))
                result = calc.square_root(num)
                print(f"√{num} = {result}")
            elif operation in ['1', '2', '3', '4', '5']:
                num1 = float(input("请输入第一个数字: "))
                num2 = float(input("请输入第二个数字: "))

                if operation == '1':
                    result = calc.add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif operation == '2':
                    result = calc.subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif operation == '3':
                    result = calc.multiply(num1, num2)
                    print(f"{num1} × {num2} = {result}")
                elif operation == '4':
                    result = calc.divide(num1, num2)
                    print(f"{num1} ÷ {num2} = {result}")
                elif operation == '5':
                    result = calc.power(num1, num2)
                    print(f"{num1} ^ {num2} = {result}")
            else:
                print("无效的操作，请重新选择！")

        except ValueError as e:
            print(f"错误: {e}")
        except Exception as e:
            print(f"发生错误: {e}")


if __name__ == "__main__":
    main()
