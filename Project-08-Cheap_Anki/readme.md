# 🎴 Flashy - Japanese Vocabulary Flashcards 🇯🇵

A Python flashcard application built with Tkinter to help you learn Japanese vocabulary using spaced repetition.

***
<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/1280px-Flag_of_Japan.svg.png" alt="Japanese Flag" width="300">
</p>

***
## ✨ Features

* **🎴 Interactive Flashcards:** Displays Japanese words on a card that flips to show the English translation.
* **⏱️ Auto-Flip Timer:** Cards automatically flip to reveal the answer after 15 seconds.
* **✅ Track Your Progress:** Mark words as "known" to remove them from the learning pile.
* **💾 Persistent Learning:** Saves your progress to a CSV file so you can continue where you left off.
* **🎨 Beautiful UI:** Clean, modern interface with custom card graphics and intuitive buttons.

***

## 🛠️ Prerequisites

To run this program, you need:

* Python 3.x
* **tkinter** (usually comes pre-installed with Python)
* **pandas** library

Install pandas using pip:

```bash
pip install pandas
```

***

## 🚀 How to Run

1.  Ensure all project files are saved in the same directory structure.
2.  Open your terminal or command prompt, navigate to the project directory, and run:

    ```bash
    python main.py
    ```

3.  A flashcard window will appear with a Japanese word. Try to remember the English meaning!
4.  Click ✅ if you knew the word, or ❌ to see another card.

***

## 💡 How It Works

1. **Study:** A Japanese word appears on the card front.
2. **Think:** You have 15 seconds to recall the English meaning.
3. **Reveal:** The card flips automatically to show the translation.
4. **Rate Yourself:**
   - Click ✅ (checkmark) if you knew it - the word is removed from your learning pile.
   - Click ❌ (cross) to skip and see another word.
5. **Progress Saved:** Your remaining words are saved to `word_to_learn.csv`.

***

## 📁 Project Files

| File | Description |
| :--- | :--- |
| `main.py` | The **main application** that handles the flashcard logic, UI, and user interactions. |
| `data/japanese.csv` | The **original word list** containing Japanese-English word pairs. |
| `data/french_words.csv` | An **alternative word list** for learning French vocabulary. |
| `data/word_to_learn.csv` | **Auto-generated file** storing words you still need to learn (created after first use). |
| `images/card_front.png` | The **front card design** (light green) for displaying the Japanese word. |
| `images/card_back.png` | The **back card design** (dark green) for showing the English translation. |
| `images/right.png` | The **checkmark button** icon for marking a word as known. |
| `images/wrong.png` | The **cross button** icon for skipping to the next card. |

***

## 🎮 Controls

| Button | Action |
| :---: | :--- |
| ✅ Green Checkmark | Mark word as **known** and remove from learning pile |
| ❌ Red Cross | **Skip** to the next word without removing |

***

## 🧠 Learning Tips

* **Be honest:** Only click ✅ when you truly know the word.
* **Daily practice:** Short, consistent sessions are more effective than long, occasional ones.
* **Reset progress:** Delete `word_to_learn.csv` to start fresh with all words.
