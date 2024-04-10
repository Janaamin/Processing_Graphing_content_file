import re
from collections import Counter, defaultdict
import matplotlib.pyplot as plt


# Define a function to plot a graph from the list of items
def plot_results(items, title, xlabel, ylabel, callout_text):
    # Set size of the plot
    plt.figure(figsize=(15, 8))

    # Unzip items into separate lists for plotting
    words, frequencies = zip(*items)

    # Create a bar chart
    bars = plt.bar(words, frequencies, color='red')

    # Add title and labels to the plot
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Add frequency labels above each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval, int(yval), ha='center', va='bottom')

    # Highlight the item of interest with an annotation
    plt.annotate(callout_text, xy=(0, items[0][1]),
                 xytext=(0, max(frequencies) + max(frequencies) * 0.1),
                 ha='center')

    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()


# Open the text file and read its contents
with open('Frankenstein.txt', 'r', encoding='utf-8') as file:
    text = file.read().lower()

# Use regular expression to split text into words and punctuation
# Apostrophes are included in words, everything else is treated as separate
words = re.findall(r'\b\w+\'?\w*|\b\w+|\S', text)

# Create a Counter to count occurrences of each word or punctuation
word_count = Counter(words)

# Find the 50 most common words or punctuation marks
most_common_words = word_count.most_common(50)

# Plot the 50 most common words or punctuation
plot_results(most_common_words, '50 Most Common Words in Frankenstein', 'Words', 'Frequency',
             f'Most Frequent: {most_common_words[0][0]}')

# Create a defaultdict to store words by their lengths
length_words = defaultdict(list)
for word in word_count.keys():
    length_words[len(word)].append(word)

# Find the longest words, with a length-first sorting
top_longest_words = []
for length, words in sorted(length_words.items(), key=lambda item: item[0], reverse=True):
    for word in words:
        top_longest_words.append((word, word_count[word]))
        if len(top_longest_words) == 50:
            break
    if len(top_longest_words) == 50:
        break

# Plot the 50 longest words found in the book
plot_results(top_longest_words, '50 Longest Words in Frankenstein', 'Words', 'Frequency',
             f'Longest Word: {top_longest_words[0][0]}')