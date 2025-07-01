# import joblib

# # Load Model & Vectorizer
# model = joblib.load("waf_model.pkl")
# vectorizer = joblib.load("vectorizer.pkl")

# # Test Inputs
# test_queries = [
#     "<script>alert(1)</script>",  # XSS
#     "' OR '1'='1' --",  # SQL Injection
#     "Hello World",  # Safe
#     "<img src='x' onerror='alert(1)'>",  # XSS
#     "../etc/passwd",  # Path Traversal
# ]

# # Convert input to ML format
# input_vectors = vectorizer.transform(test_queries)

# # Predict
# predictions = model.predict(input_vectors)

# # Print Results
# print("\n=== Model Test Results ===\n")
# for query, result in zip(test_queries, predictions):
#     print(f"Query: {query} -> Prediction: {result}")

import joblib

model = joblib.load('waf_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def classify_request(req):
    vec = vectorizer.transform([req])
    return model.predict(vec)[0]

# Test
sample = "curl http://malicious.com"
print(f"Prediction: {classify_request(sample)}")
