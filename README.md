# bookbot

BookBot is a simple Python program that analyzes a text file and reports:

- The total number of words in the document.
- The frequency of each alphabetical character, sorted from most to least common.

## 📦 Requirements

- Python 3.6+
- A plain-text file (e.g., `frankenstein.txt`) to analyze.

## 🛠 Installation

Clone this repository or download the files to your local machine:

```bash
git clone https://github.com/devbruniverse/bookbot
cd bookbot
```

Make sure your text file is accessible on your filesystem.

## 🚀 Usage

Run the program from the command line:

```bash
python3 main.py <path_to_book>
```

**Example:**

```bash
python3 main.py books/frankenstein.txt
```

## 📄 Example Output

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
```

## 📂 Project Structure

```text
bookbot/
│
├── main.py       # Entry point, handles printing the report
├── stats.py      # Functions for reading text, counting words, and counting/sorting characters
├── books/
│   └── frankenstein.txt   # Example text file
└── README.md     # This file
```

## ✨ Features

- Counts **all words** in the given file.
- Counts and sorts **alphabetical characters only** by frequency (case-insensitive).
- Skips punctuation, numbers, and other non-letter characters in character counts.


BookBot is a [Boot.dev](https://www.boot.dev) project!