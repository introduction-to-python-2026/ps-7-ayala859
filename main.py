import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


url = "https://raw.githubusercontent.com/sonarsushant/California-House-Price-Prediction/master/housing.csv"
df = pd.read_csv(url)


print(df.shape)
print(df.columns.tolist())
print(df.describe())


list2 = ['total_rooms','median_house_value','housing_median_age','median_income']
fig, axes = plt.subplots(2, 2, figsize=(12,10))
fig.suptitle("Distribution of selected characteristics", fontsize=16)

for i, data in enumerate(list2):
    row = i // 2
    col = i % 2
    axes[row,col].hist(df[data], bins=30, color='steelblue', edgecolor='white')
    axes[row,col].set_xlabel(data)
    axes[row,col].set_ylabel("frequency")
    axes[row,col].set_title("frequency of " + str(data))

plt.tight_layout()
plt.show()


fig, axes = plt.subplots(1, 3, figsize=(15,5))
plt.suptitle('Scatter graph vs. house price', fontsize=14)

list1 = ['total_rooms','median_income','housing_median_age']

for i, data in enumerate(list1):
    axes[i].scatter(df[data], df['median_house_value'], alpha=0.3, s=10)
    axes[i].set_xlabel(data)
    axes[i].set_ylabel('median_house_value')
    axes[i].set_title(str(data) + ' vs. house value')

plt.tight_layout()
plt.show()


mat = df[list2].corr()
print('Correlation matrix')
print(mat)

sns.heatmap(mat, annot=True, fmt='.3f', cmap='RdYlBu_r', center=0, square=True, linewidths=2)
plt.title('Correlation matrix of the California database', fontsize=14)
plt.tight_layout()
plt.savefig('Correlation.png', dpi=150)
plt.show()
