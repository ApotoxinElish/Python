import matplotlib.pyplot as plt


# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.displot(data=tips, x="total_bill", col="time", kde=True)


plt.show()
