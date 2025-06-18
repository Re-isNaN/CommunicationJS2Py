import sys
import json
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import LogisticRegression

"""
PARAMETERS FOR PROSPECTING:
- FIRST IMPRESSION IS THE MOST IMPORTANT
- THE EVOLUTION OF INTERACTIONS AFFECTS THE CHANCE OF CLOSING THE DEAL

Interactions Types: 'bad', 'neutral', 'good'
prospectus: YES (1), NOT (0)


interaction_1:  good   bad   bad       bad    bad       good      good      neutral   good   good      bad       neutral   good      bad       good      good
interaction_2:  good   bad   neutral   good   neutral   good      neutral   good      bad    bad       neutral   neutral   neutral   bad       bad       good
interaction_3:  good   bad   neutral   bad    good      neutral   bad       neutral   good   neutral   good      good      neutral   neutral   neutral   bad
interaction_4:  good   bad   bad       good   bad       bad       bad       bad       bad    good      good      good      neutral   good      neutral   good
prospectus:     1      0     0         0      0         0         0         0         1      1         1         1         1         1         0         1
"""

# 1. Create the data
data = pd.DataFrame({
    'interaction_1': ['good', 'bad', 'bad', 'bad', 'bad', 'good', 'good', 'neutral', 'good', 'good', 'bad', 'neutral', 'good', 'bad', 'good', 'good'],
    'interaction_2': ['good', 'bad', 'neutral', 'good', 'neutral', 'good', 'neutral', 'good', 'bad', 'bad', 'neutral', 'neutral', 'neutral', 'bad', 'bad', 'good'],
    'interaction_3': ['good', 'bad', 'neutral', 'bad', 'good', 'neutral', 'bad', 'neutral', 'good', 'neutral', 'good', 'good', 'neutral', 'neutral', 'neutral', 'bad'],
    'interaction_4': ['good', 'bad', 'bad', 'good', 'bad', 'bad', 'bad', 'bad', 'bad', 'good', 'good', 'good', 'neutral', 'good', 'neutral', 'good'],
    'prospectus': [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1]
})

# 2. Prepare the encoder to transform text into numbers (4 columns)
encoder = OrdinalEncoder(categories=[['bad', 'neutral', 'good']] * 4)

# f(x) = y, "x" are the parameters (interactions), "y" are the results (prospectus yes or no)
X = encoder.fit_transform(data[['interaction_1', 'interaction_2', 'interaction_3', 'interaction_4']])
y = data['prospectus']

# 3. Train the model
model = LogisticRegression()

# train based on x and y
model.fit(X, y)

# model.coef_ Coefficients (weights)
# model.intercept_ Intercept (biases)

# --- Function to predict probability ---
def predict_probability(interactions):
    """
    Receive a list of interactions, for example:
    ['good', 'bad', 'neutral', 'good']
    Returns the probability of prospecting (float between 0 and 1)
    """
    # Create DataFrame with the columns
    df = pd.DataFrame([interactions], columns=['interaction_1', 'interaction_2', 'interaction_3', 'interaction_4'])
    
    # Transform with the encoder
    X_novo = encoder.transform(df)
    
    # Predict probability of prospecting
    prob = model.predict_proba(X_novo)[0][1]
    return prob

def main():
    interactions = json.loads(sys.argv[1])
    probability = predict_probability(interactions)
    print(f'probability of prospecting: {probability:.2%}')

if __name__ == '__main__':
    main()


