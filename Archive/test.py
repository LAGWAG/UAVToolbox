from sklearn.manifold import MDS
import pandas as pd

mds=MDS(random_state=0)

# Create a 3x3 matrix
data = [[0, 100, 100],
        [100, 0, 100],
        [100, 100, 0]]

# Create a DataFrame from the matrix
matrix_df = pd.DataFrame(data)
scaled_df=mds.fit_transform(matrix_df)

print(scaled_df)