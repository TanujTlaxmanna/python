import numpy as np
import pandas as pd

np.random.seed(23)

mu_vec1 = np.array([0,0,0])
cov_mat1 = np.array([[1,0,0], [0,1,0], [0,0,1]])
class1_sample = np.random.multivariate_normal(mu_vec1, cov_mat1, 20)

df = pd.DataFrame(class1_sample, columns=['feature1', 'feature2', 'feature3'])
df['target'] = 1

mu_vec2 = np.array([1,1,1])
cov_mat2 = np.array([[1,0,0], [0,1,0], [0,0,1]])
class2_sample = np.random.multivariate_normal(mu_vec2, cov_mat2, 20)

df1 = pd.DataFrame(class2_sample, columns=['feature1', 'feature2', 'feature3'])
df1['target'] = 0


df = pd.concat([df, df1], ignore_index=True)

print(df.head())


import plotly.express as px
# y_train_trf = y_train_astype(str)

fig = px.scatter_3d(
    df,
    x='feature1',
    y='feature2',
    z='feature3',
    color=df['target'].astype(str)
)

fig.update_traces(
    marker=dict(
        size=12,
        line=dict(
            width=2,
            color='DarkSlateGrey'
        )
    ),
    selector=dict(mode='markers')
)

fig.show()


# STEP 1 - APPLY STANDARD SCALING

from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()

df.iloc[:, 0:3] = scalar.fit_transform(df.iloc[:, 0:3])

covariance_matrix = np.cov(df.iloc[:, 0:3], df.iloc[:, 1], df.iloc[:, 2])
print('Covariance Matrix : \n', covariance_matrix)


eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
print(eigen_values)


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
import plotly.express as px

# ---------------- Arrow3D Class ---------------- #
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        return np.min(zs3d)

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(
            xs3d, ys3d, zs3d, self.axes.get_proj()
        )
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        super().draw(renderer)

# ---------------- Plot Eigenvectors ---------------- #

fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    df['feature1'],
    df['feature2'],
    df['feature3'],
    color='blue',
    alpha=0.4,
    s=60
)

mean = df[['feature1', 'feature2', 'feature3']].mean().values

ax.scatter(
    mean[0], mean[1], mean[2],
    color='red',
    s=150
)

# Draw eigenvectors
for v in eigen_vectors.T:
    arrow = Arrow3D(
        [mean[0], mean[0] + v[0]],
        [mean[1], mean[1] + v[1]],
        [mean[2], mean[2] + v[2]],
        mutation_scale=20,
        lw=3,
        arrowstyle="-|>",
        color="red"
    )
    ax.add_artist(arrow)

ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.set_zlabel("Feature 3")

plt.title("Eigenvectors")
plt.show()

# ---------------- PCA Projection ---------------- #

pc = eigen_vectors[:, :2]

transformed_df = np.dot(df.iloc[:, 0:3], pc)

new_df = pd.DataFrame(transformed_df, columns=["PC1", "PC2"])
new_df["target"] = df["target"].astype(str)

fig = px.scatter(
    new_df,
    x="PC1",
    y="PC2",
    color="target",
    color_discrete_sequence=px.colors.qualitative.G10,
)

fig.update_traces(
    marker=dict(
        size=12,
        line=dict(width=2, color="DarkSlateGrey")
    )
)

fig.show()