import matplotlib.pyplot as plt


# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")


plt.show()
