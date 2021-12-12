# %% [markdown]
# # **Data Exploration**

# %%
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown]
# ## Load data

# %%
train_df = pd.read_csv('../data/raw/train.csv')
train_df.head()

# %%
fig = plt.figure()
ax = plt.axes()


