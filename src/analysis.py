import pandas as pd
import matplotlib.pyplot as plt
import os

data = pd.read_csv("../data/hashtags.csv")

data["date"] = pd.to_datetime(data["date"])

data["total_engagement"] = data["likes"] + data["shares"] + data["comments"]

hashtag_summary = data.groupby("hashtag")["total_engagement"].sum()

print("Hashtag Performance:")
print(hashtag_summary)

os.makedirs("../images", exist_ok=True)

plt.figure()
hashtag_summary.plot(kind="bar")
plt.title("Total Engagement by Hashtag")
plt.xlabel("Hashtag")
plt.ylabel("Total Engagement")

plt.savefig("../images/hashtag_engagement.png")
plt.show()

print("Graph saved in images folder!")