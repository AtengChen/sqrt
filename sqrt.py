"""
.. math::
    A_{p}=A_{p-1}+\frac{n-A_{p-1}^{2}}{2A_{p-1}}

"""


class Sqrt:
    def __init__(self,
                 a,  # 被平方根数
                 b=None,  # 近似平方数
                 iterations=None,  # 迭代次数
                 f=False  # 负数结果是否被计入
                 ):
        if a < 0:  # a为负数
            raise ValueError("math domain error")
        if iterations == None:
            iterations = int(len(str(a)) ** 2 + len(str(a)) * 2 + 10)
        if b is None:
            l = {}  # 存储正误差
            l2 = {}  # 存储负误差

            # 查找近似平方数并统计正负误差
            for i in range(0, a + 1):
                if "-" not in str(i ** 2 - a):
                    l[abs(i ** 2 - a)] = i
                else:
                    l2[abs(i ** 2 - a)] = i

            # 获取最小正误差和最小负误差
            try:
                n = list(l)[0]  # 最小正误差
                n2 = list(l2)[-1]  # 最小负误差
            except IndexError:  # a = 0
                self.result = 0
                return

            # 根据正和负误差哪个小来决定近似平方数
            if n > n2:
                b = l2[n2] ** 2
            elif n < n2:
                b = l[n] ** 2
            else:
                b = a
                iterations = 1

        # 迭代核心算法
        self.result = b
        self.f = f
        for i in range(iterations):
            self.result = self.result + (a - self.result ** 2) / (2 * self.result)

    def __str__(self):
        try:
            if self.f:  # 负数结果是否被计入
                return " ".join((str(self.result), str(-self.result)))
            return str(self.result)
        except AttributeError:
            return "0"

    def __float__(self):
        return self.result


if __name__ == '__main__':
    s = Sqrt(int(input("")))
    print(s)
