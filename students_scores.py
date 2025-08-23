import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report, mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from lazypredict.Supervised import LazyRegressor


data = pd.read_csv("../Students_Scores_Prediction/StudentScore.xls")

# data split
target = "writing score"
x = data.drop(target, axis = 1)
y = data[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#data preprocessing


gender_values = ["male", "female"]
parental_level_of_education_values = [ 'some high school','high school','some college',"associate's degree","bachelor's degree", "master's degree"]
test_values = x_train["test preparation course"].unique()
lunch_values = x_train["lunch"].unique()

ord_features = Pipeline([
    ("imputer", SimpleImputer(missing_values= np.nan, strategy= "most_frequent")),
    ("ordinal_encoder", OrdinalEncoder(categories=[gender_values,parental_level_of_education_values,test_values,lunch_values]))
])

nom_features = Pipeline([
    ("imputer", SimpleImputer(missing_values= np.nan, strategy= "most_frequent")),
    ("onehot_encoder",OneHotEncoder(sparse_output=True) )
])

num_features = Pipeline([
    ("imputer", SimpleImputer(missing_values= np.nan, strategy= "most_frequent")),
    ("scaler",StandardScaler())
])

preprocessor = ColumnTransformer([
    ("ord_features", ord_features, ["gender","parental level of education","test preparation course", "lunch"]),
    ("nom_features", nom_features, ["race/ethnicity"]),
    ("num_features", num_features, ["math score", "reading score"])
])

reg = Pipeline([
    ("preprocessor", preprocessor),
    ("model",RandomForestRegressor())
])

# reg.fit(x_train, y_train)
# y_predict = reg.predict(x_test)


# LINEAR REGRESSION
# MSE : 14.980822041816777
# MAE : 3.2039447691582152
# R2 : 0.9378432907399291

# # DECISION TREE
# params = {
#     "model__criterion" : ["squared_error", "absolute_error","poisson"],
#     "model__max_depth" : (None, 2 ,5)
# }
#
# grid_search = GridSearchCV(param_grid=params, estimator=reg, cv = 5, verbose=2)
# grid_search.fit(x_train, y_train)
# y_predict = grid_search.predict(x_test)

#DECISION TREE RESULT
# MSE : 25.629691544327233
# MAE : 4.025918900831273
# R2 : 0.8936602222962626

params = {
    "model__criterion" : ["squared_error", "absolute_error","poisson"],
    "model__max_depth" : (None, 2 ,5),
    "model__n_estimators" : [100,200,300],
    "preprocessor__num_features__imputer__strategy" :["mean","median"]
}

grid_search = GridSearchCV(param_grid=params, estimator=reg, cv = 5, verbose=2,scoring="r2")
grid_search.fit(x_train, y_train)
y_predict = grid_search.predict(x_test)

MSE = mean_squared_error(y_test, y_predict)
MAE = mean_absolute_error(y_test, y_predict)
R2 = r2_score(y_test, y_predict)
print("MSE : {}".format(MSE))
print("MAE : {}".format(MAE))
print("R2 : {} ".format(R2))

# random forest
# MSE : 20.133723597222218
# MAE : 3.6168916666666666
# R2 : 0.9164634623879824

clf = LazyRegressor(verbose=0, ignore_warnings=False, custom_metric=None)
models, predictions = clf.fit(x_train, x_test, y_train, y_test)