import numpy as np
import matplotlib.pyplot as plt

def plot_normal_distribution(mu, sigma):
    """
    繪製常態分佈的機率密度函數圖形

    :param mu: 平均值
    :param sigma: 標準差
    """
    # 定義 x 軸範圍
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
    # 計算機率密度函數
    pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    # 繪製圖形
    plt.plot(x, pdf, label=f'μ={mu}, σ={sigma}')
    plt.title('Normal Distribution')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid()
    plt.show()

# 測試函數
plot_normal_distribution(0, 1)  # 平均值 0，標準差 1