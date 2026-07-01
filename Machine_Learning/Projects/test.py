import pickle
import numpy as np

pipe = pickle.load( open("Machine_Learning\\Models\\pipe.pkl", 'rb'))

test_inp = np.array([1, 'female', 38.0, 1.0 , 0.0, 71.2833, 'C'], dtype = object).reshape(1,7)

pred = pipe.predict(test_inp)

for p in pred:
    print(f"\nAccording to the prediction model \n {p} -> {'Died' if p == 0 else 'Survived'}\n")

# Test samples
# 0, 'male', 22.0, 1.0, 0.0, 7.25, 'S'          - DIED
# 1, 'female', 38.0, 1.0 , 0.0, 71.2833, 'C'    - SURVIVED
