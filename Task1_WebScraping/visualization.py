import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("books.csv")

# Count ratings
rating_counts = df["Rating"].value_counts()

# Create bar chart
plt.figure(figsize=(8,5))

plt.bar(rating_counts.index, rating_counts.values)

# Labels
plt.title("Book Ratings Distribution")
plt.xlabel("Ratings")
plt.ylabel("Number of Books")

# Show chart
plt.show()