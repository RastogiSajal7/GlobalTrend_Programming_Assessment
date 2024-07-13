import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

def preprocess_dataframe(df):
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ])

    df_cleaned = preprocessor.fit_transform(df)

    num_feature_names = numerical_cols
    cat_feature_names = preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_cols)
    feature_names = list(num_feature_names) + list(cat_feature_names)
    
    df_cleaned = pd.DataFrame(df_cleaned, columns=feature_names)
    
    return df_cleaned

data = {
    'age': [25, 30, 35, np.nan, 40],
    'salary': [50000, 60000, np.nan, 80000, 70000],
    'city': ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Delhi']
}

df = pd.DataFrame(data)
df_cleaned = preprocess_dataframe(df)
print(df_cleaned)
