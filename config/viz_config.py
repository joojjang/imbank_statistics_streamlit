import platform
import matplotlib.pyplot as plt

# 글꼴 설정
os_name = platform.system()
if os_name == 'Darwin':     # macOS
    plt.rcParams['font.family'] = 'AppleGothic'
elif os_name == 'Windows':  # Windows
        plt.rcParams['font.family'] = 'Malgun Gothic'

# - 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False
