# 🎤 Kanye Quotes - Inspirational Wisdom Generator 💭

A fun Python GUI application that displays random Kanye West quotes at the click of a button!

***
<p align="center">
    <img src="https://thestrive.co/wp-content/uploads/2022/01/inspirational-kanye-west-quotes.jpg" alt="Kanye West" width="300" height="400">
</p>

***
## ✨ Features

* **🎲 Random Quotes:** Fetches random Kanye West quotes from the Kanye REST API.
* **🖼️ Custom GUI:** Beautiful Tkinter interface with custom background and button images.
* **🔄 One-Click Refresh:** Simply click the Kanye button to get a new inspirational quote.
* **🌐 API Integration:** Real-time quotes fetched from `https://api.kanye.rest`.

***

## 🛠️ Prerequisites

To run this program, you need:

* Python 3.x
* **requests** library
* **tkinter** (usually comes pre-installed with Python)

Install requests using pip:

```bash
pip install requests
```

***

## 🚀 How to Run

1. Navigate to the project directory in your terminal:

   ```bash
   cd Project-10-Kenya-Quotes/kenya_quotes
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. Click the Kanye button to generate new quotes!

***

## 💡 How It Works

1. **Initialize GUI:** Creates a Tkinter window with custom styling.
2. **Load Assets:** Loads background image and Kanye button image.
3. **Fetch Quote:** Makes a GET request to the Kanye REST API.
4. **Display Quote:** Updates the canvas text with the fetched quote.
5. **User Interaction:** Clicking the button triggers a new API call and displays a fresh quote.

***

## 📁 Project Files

| File | Description |
| :--- | :--- |
| `main.py` | The **main application** that handles the GUI and API calls. |
| `background.png` | **Background image** for the quote display canvas. |
| `kanye.png` | **Button image** - clicking this fetches a new quote. |

***

## 🔧 Customization Ideas

| Enhancement | Description |
| :--- | :--- |
| **Save Favorites** | Add a button to save your favorite quotes to a file |
| **Copy to Clipboard** | Implement copy functionality for easy sharing |
| **Quote History** | Keep track of previously displayed quotes |
| **Different APIs** | Swap the API for other quote sources |

***

## ⚠️ Important Notes

* **Internet Required:** The app needs an active internet connection to fetch quotes.
* **API Dependency:** The app relies on `https://api.kanye.rest` being available.
* **Image Files:** Ensure `background.png` and `kanye.png` are in the same directory as `main.py`.

***

## 🎯 Use Cases

* **Daily Motivation:** Start your day with some Kanye wisdom!
* **Learning:** Great project for understanding API calls and Tkinter basics.
* **Fun:** Share hilarious and thought-provoking quotes with friends.
