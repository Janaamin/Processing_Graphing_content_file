import re
from collections import Counter, defaultdict
import matplotlib.pyplot as plt


# Function to plot the results
def plot_results(items, title, xlabel, ylabel, callout_text):
    plt.figure(figsize=(15, 8))
    words, frequencies = zip(*items)
    bars = plt.bar(words, frequencies, color='red')

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval, int(yval), ha='center', va='bottom')

    plt.annotate(callout_text, xy=(0, items[0][1]),
                 xytext=(0, max(frequencies) + max(frequencies) * 0.1),
                 ha='center')

    plt.tight_layout()
    plt.show()


# Read the contents of the file
with open('Frankenstein.txt', 'r', encoding='utf-8') as file:
    text = file.read().lower()

# Use regular expression to find all words and punctuation marks
# Apostrophes are part of words, but other punctuation are separated
words = re.findall(r'\b\w+\'?\w*|\b\w+|\S', text)

# Count each word in the text
word_count = Counter(words)

# Select the 50 most common words
most_common_words = word_count.most_common(50)

# Plot the 50 most used words
plot_results(most_common_words, '50 Most Common Words in Frankenstein', 'Words', 'Frequency',
             f'Most Frequent: {most_common_words[0][0]}')

# Use a defaultdict to store words by length to find the longest
length_words = defaultdict(list)
for word in word_count.keys():  # Use word_count to avoid duplicates
    length_words[len(word)].append(word)

# Get the 50 longest unique words sorted by length
longest_unique_words = sorted(length_words.items(), key=lambda x: x[0], reverse=True)
top_longest_words = []
for length, words in longest_unique_words:
    for word in words:
        top_longest_words.append((word, word_count[word]))
        if len(top_longest_words) == 50:
            break
    if len(top_longest_words) == 50:
        break

# Sort the top 50 longest words by frequency (secondary) and length (primary)
top_longest_words = sorted(top_longest_words, key=lambda x: (-len(x[0]), -x[1]))

# Plot the 50 longest words
plot_results(top_longest_words, '50 Longest Words in Frankenstein', 'Words', 'Frequency',
             f'Longest Word: {top_longest_words[0][0]}')