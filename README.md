# Spam Email Classification using NLP and Machine Learning

## Overview
This project focuses on building a machine learning model to classify emails as spam or not spam (ham) using Natural Language Processing (NLP) techniques. The solution is deployed using Streamlit, enabling users to interact with the classification model via a user-friendly interface.

## Features
- Preprocessing email text data using NLP techniques.
- Training a machine learning model for spam detection.
- Interactive web app for real-time email classification.

## Demo
[**Live App on Streamlit**](https://hamorspam.streamlit.app/)

## Dataset
The model is trained on a publicly available spam email dataset. The dataset includes:
- **Spam Emails**: Emails labeled as spam.
- **Ham Emails**: Legitimate emails.

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Libraries**:
  - `scikit-learn` for machine learning.
  - `pandas` and `numpy` for data manipulation.
  - `Streamlit` for building the interactive app.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/vaishnavikhairnar3018/Spam-Email-Classification-using-NLP-and-Machine-Learning.git
   cd Spam-Email-Classification-using-NLP-and-Machine-Learning
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run spamDetector.py
   ```

## File Structure
```
.
├── spamDetector.py        # Main Streamlit app script
├── requirements.txt       # Dependencies for the project
├── spam.pkl               # Pre-trained machine learning model
├── vectorizer.pkl         # Fitted vectorizer for text transformation
├── README.md              # Project documentation
```

## Usage
1. Run the Streamlit app as described above.
2. Enter email text into the input box on the web app.
3. View the classification result (Spam or Ham).

## Example Output
Input:
```
Congratulations! You have won a $1000 gift card. Claim now.
```
Output:
```
Spam
```

## Future Enhancements
- Add support for additional datasets to improve accuracy.
- Integrate advanced NLP techniques such as word embeddings.
- Deploy the app on other platforms for wider accessibility.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Developed by [Vaishnavi Khairnar](https://github.com/vaishnavikhairnar3018)


