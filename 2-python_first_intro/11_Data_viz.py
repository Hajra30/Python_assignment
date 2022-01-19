# step_1 import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# step_2 set a theme
sns.set_theme(style="ticks", color_codes=True)

# step_3 import data set
kashti = sns.load_dataset("titanic")
#print(kashti)

#graph with two variables
p=sns.countplot(x="sex", data=kashti, hue="class")
p.set_title("count plot")
plt.show()

