import pandas as pd
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
y = boston.target
x = df[['CRIM','INDUS','NOX','RM', 'TAX','LSTAT']]
model = LinearRegression()
lr_model = model.fit(x,y)
print(lr_model.coef_)
print(lr_model.intercept_)


