# Actual values
actual_values = [1, 0, 1, 1, 0, 0, 1, 1, 0, 0]

# Predicted values
predicted_values = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0]

# Initialize counters
TP = 0  # True positives
TN = 0  # True negatives
FP = 0  # False positives
FN = 0  # False negatives

# Iterate over the actual and predicted values
for actual, predicted in zip(actual_values, predicted_values):
    if actual == 1 and predicted == 1:
        TP += 1  # True positive
    elif actual == 0 and predicted == 0:
        TN += 1  # True negative
    elif actual == 0 and predicted == 1:
        FP += 1  # False positive
    elif actual == 1 and predicted == 0:
        FN += 1  # False negative

# Print the results
print("True Positives (TP):", TP)
print("True Negatives (TN):", TN)
print("False Positives (FP):", FP)
print("False Negatives (FN):", FN)

# Calculate accuracy, precision, recall, and F1 score
accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1_score = 2 * (precision * recall) / (precision + recall)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1_score)