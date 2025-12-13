# 🔤 NATO Phonetic Alphabet Converter 📻

A Python program that converts any word into its NATO phonetic alphabet representation using pandas.

***
<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/e/e0/FAA_Phonetic_and_Morse_Chart2.svg" alt="NATO Phonetic Alphabet Chart" width="500">
</p>

***
## ✨ Features

* **📖 Word to Phonetic Conversion:** Enter any word and get its NATO phonetic alphabet equivalent.
* **🔄 Recursive Input Handling:** If non-alphabetic characters are entered, the program prompts again.
* **📊 Pandas Integration:** Uses pandas to read and process the phonetic alphabet data from a CSV file.
* **🛡️ Error Handling:** Gracefully handles invalid input with user-friendly messages.

***

## 🛠️ Prerequisites

To run this program, you need:

* Python 3.x
* **pandas** library

Install pandas using pip:

```bash
pip install pandas
```

***

## 🚀 How to Run

1.  Ensure all project files (`main.py`, `nato_phonetic_alphabet.csv`) are saved in the same directory.
2.  Open your terminal or command prompt, navigate to the project directory, and run the main file:

    ```bash
    python main.py
    ```

3.  Enter a word when prompted, and receive the phonetic spelling!

***

## 💡 Example Usage

```
Enter a word: Python
['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']

Enter a word: Hello
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

***

## 📁 Project Files

| File | Description |
| :--- | :--- |
| `main.py` | The **main program** that reads the CSV file, creates a phonetic dictionary, and converts user input to phonetic code words. |
| `nato_phonetic_alphabet.csv` | A **CSV data file** containing the mapping of each letter (A-Z) to its corresponding NATO phonetic code word. |

***

## 🔤 NATO Phonetic Alphabet Reference

| Letter | Code Word | Letter | Code Word |
| :---: | :--- | :---: | :--- |
| A | Alfa | N | November |
| B | Bravo | O | Oscar |
| C | Charlie | P | Papa |
| D | Delta | Q | Quebec |
| E | Echo | R | Romeo |
| F | Foxtrot | S | Sierra |
| G | Golf | T | Tango |
| H | Hotel | U | Uniform |
| I | India | V | Victor |
| J | Juliet | W | Whiskey |
| K | Kilo | X | X-ray |
| L | Lima | Y | Yankee |
| M | Mike | Z | Zulu |
