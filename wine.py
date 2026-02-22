import pandas as pd



## Data retrieval
df_red   = pd.read_excel("C:/Users/khnda/Python/data/winequality-red.xlsx", header=0, skiprows=1)
df_white = pd.read_excel("C:/Users/khnda/Python/data/winequality-white.xlsx", header=0, skiprows=1)

print("Red wine dataset shape:", df_red.shape)
print("White wine dataset shape:", df_white.shape)

print(df_red.head())
print(df_red.isnull().sum())
print(df_white.isnull().sum())

## Replacing Numericals
num_cols_red = df_red.select_dtypes(include='number').columns
num_cols_white = df_white.select_dtypes(include='number').columns

df_red[num_cols_red] = df_red[num_cols_red].fillna(df_red[num_cols_red].median())
df_white[num_cols_white] = df_white[num_cols_white].fillna(df_white[num_cols_white].median())

## Replacing Categorical columns (if any exist)
cat_cols_red = df_red.select_dtypes(include='object').columns
cat_cols_white = df_white.select_dtypes(include='object').columns

for col in cat_cols_red:
    df_red[col] = df_red[col].fillna("Unknown")

for col in cat_cols_white:
    df_white[col] = df_white[col].fillna("Unknown")

## Remove Duplicates
df_red = df_red.drop_duplicates()
df_white = df_white.drop_duplicates()

## Creating a new column 'type'
df_red['type'] = 'red'
df_white['type'] = 'white'

## Combine dataset
df_wine = pd.concat([df_red, df_white], ignore_index=True)

## Create new features
df_wine['alcohol_level'] = pd.cut(df_wine['alcohol'], bins=3, labels=['low','medium','high'])
df_wine['acidity_level'] = pd.cut(df_wine['pH'], bins=[0,3,3.5,14], labels=['high','medium','low'])
df_wine['sugar_alcohol_ratio'] = df_wine['residual sugar'] / df_wine['alcohol']

## Descriptive statistics
print("Red wine statistics:\n", df_red.describe())
print("White wine statistics:\n", df_white.describe())
print("Combined wine statistics:\n", df_wine.describe())

## Comparison table
features = ['alcohol', 'pH', 'residual sugar', 'fixed acidity', 'volatile acidity', 'quality']

comparison = pd.DataFrame({
    'Red Mean': df_red[features].mean(),
    'White Mean': df_white[features].mean(),
    'Red Median': df_red[features].median(),
    'White Median': df_white[features].median(),
    'Red Std': df_red[features].std(),
    'White Std': df_white[features].std(),
    'Red Min': df_red[features].min(),
    'White Min': df_white[features].min(),
    'Red Max': df_red[features].max(),
    'White Max': df_white[features].max()
}).round(2)

print(comparison)


features = ['alcohol', 'pH', 'residual sugar',
            'fixed acidity', 'volatile acidity', 'quality']

# Red
red_stats = df_red[features].describe().T
red_stats['median'] = df_red[features].median()

# White
white_stats = df_white[features].describe().T
white_stats['median'] = df_white[features].median()

# Combined
combined_stats = df_wine[features].describe().T
combined_stats['median'] = df_wine[features].median()

print("Red wine stats:\n", red_stats)
print("\nWhite wine stats:\n", white_stats)
print("\nCombined wine stats:\n", combined_stats)


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)

red_stats.describe()

df_red.describe().T
df_white.describe().T
df_wine.describe().T


## Check normality
df_wine['alcohol'].plot.hist(bins=30)
df_wine['residual sugar'].plot.hist(bins=30)
df_wine['pH'].plot.hist(bins=30)
df_wine['quality'].plot.hist(bins=30)


df_red['alcohol'].plot.hist(alpha=0.5, bins=30)
df_white['alcohol'].plot.hist(alpha=0.5, bins=30)

df_wine.boxplot(column='alcohol', by='type')



# Plot 1: 5 Bins
df_wine['pH'].hist(bins=5)

# Plot 2: 10 Bins
df_wine['pH'].hist(bins=10)


import matplotlib.pyplot as plt

# 1. Create the heatmap
plt.figure(figsize=(10, 8))
plt.imshow(corr_matrix, cmap='coolwarm')

# 2. Add the labels so you can read the graph
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)

# 3. Add a colorbar to see the scale (-1 to +1)
plt.colorbar()
plt.show()
