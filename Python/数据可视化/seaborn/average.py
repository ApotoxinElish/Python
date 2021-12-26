import matplotlib.pyplot as plt


# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
fmri = sns.load_dataset("fmri")

# Create a visualization
sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", col="region",
    hue="event", style="event",
)


plt.show()
