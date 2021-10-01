import pandas as pd
#%%
# importing data
everything = pd.read_csv('/Users/arunkrishnavajjala/Documents/GMU/URA/project/USCovidPM.csv', sep=',')

print(everything)
#%%
# sorting data into their own arrats
mortality = everything.Mortality
pm = everything.pm

pm2 = []

for i in pm:
    lst = []
    lst.append(i)
    pm2.append(lst)
print(pm2)

pm2 = pd.DataFrame(pm2)

#%%
# splittin data into test and train
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(pm2, mortality, test_size=0.2)
print (X_train.shape, y_train.shape)
print (X_test.shape, y_test.shape)

#%%
# importing various regression models
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVR

#clf = DecisionTreeRegressor()
#clf = KNeighborsRegressor(n_neighbors=3)
# predictind
clf = make_pipeline(StandardScaler(0), SVR(C=1, epsilon=.2))
clf = clf.fit(X_train, y_train)
result = clf.predict(X_test)

#%%
# calculating accuracy
result = abs(result)
count = 0
cor = 0
for i in y_test:
    if abs(i - result[count]) < 0.035:
        cor += 1
    count += 1

print(result)
print(y_test)

decision = cor/len(result)
print(decision)
#%%

# plotting accuracies 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')

names = ["SVM", "Decision Tree", "K-Nearest Neighbors"]
nums = [0.7272727272727273, 0.7272727272727273, 0.8181818181818182]

y_pos = np.arange(len(names))

plt.bar(y_pos, nums, align='center', alpha=0.5)
plt.xticks(y_pos, names)
plt.ylabel('Accuracy')
plt.xlabel('Prediction Algorithms')
plt.title('Accurracy of Mortality Rate Predictions')
plt.show()























