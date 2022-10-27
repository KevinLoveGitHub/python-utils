import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

##样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xi = np.array([17.1, 17.4, 17.8, 18.2])  # 身高
Yi = np.array([7.8, 7.1, 7.5, 6.5])  # 体重

# 画样本点
plt.figure(figsize=(8, 6))  ##指定图像比例： 8：6
plt.scatter(Xi, Yi, color="green", label="样本数据", linewidth=1)
plt.show()
