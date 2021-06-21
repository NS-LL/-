#柱状图显示temp1结果
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
#这里使用pandas读取csv文件
data = pd.read_csv('temp1.csv')

component_col = data['current_service']
component_categories = component_col.unique()
print('部位类别为:')
print(component_categories)

categories_grouped = data.groupby('current_service')
categories_count = categories_grouped['current_service'].count()
print(categories_count)

categories_count.plot(kind='bar')
plt.title('temp1')
plt.tight_layout()
plt.show()
