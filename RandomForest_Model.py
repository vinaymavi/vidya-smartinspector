#Based on the Article from
#Institue of Advanced Materials and Technology - University of Beijing
#Corrsoin Modeling reference articles from university of Lisbon
#Atmosperic corrosion Rate modeling Barzil

###Read the Data set using pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
filename = './data/rf/CorrostionDataset_v2.csv'

corrosiondata = pd.read_csv(filename)
print(corrosiondata.columns)
corrosiondata.head()
print("dimension of corrosiondata data: {}".format(corrosiondata.shape))
print(corrosiondata.groupby('corrosionindex').size())
import seaborn as sns
sns.countplot(corrosiondata['corrosionindex'],label="Count")
corrosiondata.info()
corrosiondata_features = [x for i,x in enumerate(corrosiondata.columns) if i!=6]
X_train, X_test, y_train, y_test = train_test_split(corrosiondata.loc[:, corrosiondata.columns != 'corrosionindex'],
                                                    corrosiondata['corrosionindex'], stratify=corrosiondata['corrosionindex'],
                                                    random_state=66)

#########################RandomForest ######################################
def plot_feature_importances_corrosiondata(model):
    plt.figure(figsize=(6,4))
    n_features = 6
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features), corrosiondata_features)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.ylim(-1, n_features)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, random_state=0)
rf.fit(X_train, y_train)
print("Accuracy on training set: {:.3f}".format(rf.score(X_train, y_train)))
print("Accuracy on test set: {:.3f}".format(rf.score(X_test, y_test)))
###########PLAY WITH DEPTH OF TEH LEAF###################################
#rf1 = RandomForestClassifier(max_depth=3, n_estimators=100, random_state=0)
#rf1.fit(X_train, y_train)
#print("Accuracy on training set: {:.3f}".format(rf1.score(X_train, y_train)))
#print("Accuracy on test set: {:.3f}".format(rf1.score(X_test, y_test)))
#plot_feature_importances_corrosiondata(rf)
plt.savefig('./savefig/CorrosionParamFeature_importance1')

#Save the Model file
import pickle
filename = './genrated_models/CorrosionCARF_mode2.sav'
pickle.dump(rf, open(filename, 'wb'))


