import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("tweets_sentiment.csv")

# Count each sentiment type
sentiment_counts = df["Sentiment"].value_counts(normalize=True) * 100  # Convert to percentage

# Set Seaborn style
sns.set_style("darkgrid")
plt.figure(figsize=(8, 5))

# Create a stylish bar plot
ax = sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, 
                 palette={"Positive": "#4CAF50", "Negative": "#F44336", "Neutral": "#9E9E9E"})

# Add annotations
for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2, p.get_height()),
                ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

# Labels and title
plt.title("Sentiment Analysis of AI Image Tweets", fontsize=14, fontweight='bold')
plt.xlabel("Sentiment", fontsize=12)
plt.ylabel("Percentage (%)", fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

plt.show()