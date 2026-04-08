# 1)Edit distance between strings s1 and s2
def edit_distance_recursive(str1, str2, len1, len2):
    # Base cases
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1

    # If last characters match
    if str1[len1 - 1] == str2[len2 - 1]:
        return edit_distance_recursive(str1, str2, len1 - 1, len2 - 1)

    # If last characters don't match
    return 1 + min(
        edit_distance_recursive(str1, str2, len1, len2 - 1),    # Insert
        edit_distance_recursive(str1, str2, len1 - 1, len2),    # Delete
        edit_distance_recursive(str1, str2, len1 - 1, len2 - 1) # Replace
    )


# Input
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

distance = edit_distance_recursive(string1, string2, len(string1), len(string2))
print("Edit Distance:", distance)

# weighted edit distance between strings s1 and s2
import numpy as np

def levenshtein_distance(str1, str2):
    rows = len(str1) + 1
    cols = len(str2) + 1

    # Create matrix
    dp_matrix = np.zeros((rows, cols), dtype=int)

    # Initialize first row and column
    for i in range(rows):
        dp_matrix[i][0] = i
    for j in range(cols):
        dp_matrix[0][j] = j

    # Fill matrix
    for i in range(1, rows):
        for j in range(1, cols):
            if str1[i - 1] == str2[j - 1]:
                dp_matrix[i][j] = min(
                    dp_matrix[i - 1][j] + 1,      # Delete
                    dp_matrix[i - 1][j - 1],      # Match
                    dp_matrix[i][j - 1] + 1       # Insert
                )
            else:
                dp_matrix[i][j] = min(
                    dp_matrix[i - 1][j] + 1,      # Delete
                    dp_matrix[i - 1][j - 1] + 1,  # Replace
                    dp_matrix[i][j - 1] + 1       # Insert
                )

    print("DP Matrix:\n", dp_matrix)
    return dp_matrix[rows - 1][cols - 1]


print("Levenshtein Distance:", levenshtein_distance("cat", "dog"))


# 3)   Two sentences are given. Compute the edit distance at the word level:

# Sentence 1: I love natural language processing
# Sentence 2: I enjoy learning language processing

def word_edit_distance(words1, words2, len1, len2):
    # Base cases
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1

    # If words match
    if words1[len1 - 1] == words2[len2 - 1]:
        return word_edit_distance(words1, words2, len1 - 1, len2 - 1)

    # If words don't match
    return 1 + min(
        word_edit_distance(words1, words2, len1, len2 - 1),    # Insert
        word_edit_distance(words1, words2, len1 - 1, len2),    # Delete
        word_edit_distance(words1, words2, len1 - 1, len2 - 1) # Replace
    )


# Input
sentence1 = input("Enter sentence 1: ")
sentence2 = input("Enter sentence 2: ")

# Convert to word lists
words_list1 = sentence1.split()
words_list2 = sentence2.split()

distance = word_edit_distance(words_list1, words_list2, len(words_list1), len(words_list2))

print("Word-level Edit Distance:", distance)# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv('Electric_Production.csv')

# Convert DATE column 
df['DATE'] = pd.to_datetime(df['DATE'], format='%d/%m/%Y')

# Set DATE as index
df.set_index('DATE', inplace=True)

df.rename(columns={'IPG2211A2N': 'Production'}, inplace=True)

# Step 3: Plot time series
plt.figure(figsize=(8, 4))
plt.plot(df['Production'], marker='o', label='Actual Production')
plt.title('Electricity Production Data')
plt.xlabel('Date')
plt.ylabel('Production')
plt.legend()
plt.show()

df['Time'] = np.arange(len(df))

# Train-test split (last 3 values)
train = df.iloc[:-3]
test = df.iloc[-3:]

# Linear Regression
lr = LinearRegression()
lr.fit(train[['Time']], train['Production'])
pred_lr = lr.predict(test[['Time']])

# Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=0)
rf.fit(train[['Time']], train['Production'])
pred_rf = rf.predict(test[['Time']])

# ARIMA
arima_model = ARIMA(train['Production'], order=(4, 1, 2))
arima_fit = arima_model.fit()
pred_arima = arima_fit.forecast(steps=3)

results = test.copy()
results['LR_Pred'] = pred_lr
results['RF_Pred'] = pred_rf
results['ARIMA_Pred'] = pred_arima.values

def evaluate(actual, predicted):
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    return mae, rmse

mae_lr, rmse_lr = evaluate(test['Production'], results['LR_Pred'])
mae_rf, rmse_rf = evaluate(test['Production'], results['RF_Pred'])
mae_arima, rmse_arima = evaluate(test['Production'], results['ARIMA_Pred'])

comparison = pd.DataFrame({
    'Model': ['Linear Regression', 'Random Forest', 'ARIMA'],
    'MAE': [mae_lr, mae_rf, mae_arima],
    'RMSE': [rmse_lr, rmse_rf, rmse_arima]
})

print("\nModel Performance Comparison:\n")
print(comparison)

plt.figure(figsize=(8, 4))
plt.plot(df.index, df['Production'], label='Actual', marker='o')
plt.plot(results.index, results['LR_Pred'], label='Linear Regression', marker='x')
plt.plot(results.index, results['RF_Pred'], label='Random Forest', marker='^')
plt.plot(results.index, results['ARIMA_Pred'], label='ARIMA', marker='s')

plt.title('Model Comparison')
plt.xlabel('Date')
plt.ylabel('Production')
plt.legend()
plt.show()

print("\nDetailed Predictions:\n")
print(results)

# Machine learning models like Random Forest fail because they do not inherently capture time dependencies unless lag features are added.
# ARIMA performs better as it models temporal relationships in time series data


# Based on the visual and numerical comparison, ARIMA gives the best performance for time series forecasting. 
# It accurately captures both the trend and time-based pattern of sales. Linear Regression performs moderately well by fitting a trend line, while Random Forest performs the weakest as it doesn’t consider time dependency. 
# Hence, ARIMA is the most suitable model for predicting future sales in this dataset.