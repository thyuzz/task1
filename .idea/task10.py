# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
#   Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})
# data.head() |

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

# без get_dummies
unique_values = data['whoAmI'].unique()
one_data = pd.DataFrame()
for value in unique_values:
    one_data[value] = (data['whoAmI'] == value).astype(int)
print(one_data)

# c get_dummies
unique_values2 = data['whoAmI'].unique()
two_data = pd.get_dummies(data['whoAmI'])
for value in unique_values2:
    two_data[value] = (data['whoAmI'] == value).astype(int)
print(two_data)