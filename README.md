# 💼 Employee Salary Predictor

A modern, user-friendly web application that predicts **employee annual salary in Indian Rupees (₹)** using machine learning.  
Built with **Streamlit**, it uses demographic and professional inputs—including **years of experience**—to provide realistic salary estimates for:

- 🎯 HR analytics  
- 🎓 Career counseling  
- 👩‍💻 Personal decision-making

---

## 🌟 Features

- 🔢 **Input Fields**: Age, Years of Experience (2–30), Education Level, Occupation, Hours Worked per Week, and Gender  
- 🤖 **ML Backend**: Powered by a trained **Random Forest Regressor**  
- 💰 **Salary in INR**: Output is shown in Indian Rupees using real-world patterns  
- 🎨 **Beautiful UI**: Clear layout, colorful elements, and optional logo  
- ⚡ **Interactive & Fast**: Instantly predicts on new input  
- 🧩 **Simple Setup**: Works locally—no deployment or hosting needed  

---

## 📸 Example Output

> User enters their details using dropdowns, sliders, and radio buttons.  
> On clicking **“🔮 Predict Salary”**, the app returns something like:

```text
🎯 Predicted Salary  
₹ 800,000

📁 Project Structure

salary_predictor_india/
├── app.py                   # Streamlit app frontend
├── train_model.py           # Model training script
├── salary_model.pkl         # Saved machine learning model
├── data/
│   └── salary_data.csv      # Dataset
├── assets/
│   └── logo.png             # Optional logo
├── requirements.txt         # Python dependencies
└── .streamlit/
    └── config.toml          # Streamlit theming config


🗂️ Dataset Format

Location: data/salary_data.csv
The dataset must include these columns:

age
years_experience (Integer, range: 2–30)
education (e.g., HS-grad, Bachelors, Masters, Doctorate)
occupation (e.g., Tech-support, Exec-managerial, etc.)
hours-per-week
gender (Male/Female)
income (<=50K or >50K, mapped to INR bands internally)

✅ You can edit or expand this dataset to improve accuracy.

🛠️ Installation & Usage

1. Clone the Repository

git clone <repo-url>
cd salary_predictor_india

2. Install Python Dependencies
pip install -r requirements.txt

3. Prepare the Data

Modify data/salary_data.csv if needed
Ensure years_experience is within the 2–30 range

4. Train the Model
python train_model.py
➡️ This generates the salary_model.pkl file.

5. Run the Streamlit App

streamlit run app.py
Open the browser at the provided local URL.

🎨 Customization

🖼️ Replace assets/logo.png with your own branding
🎨 Modify .streamlit/config.toml to update UI theme
🧠 Tune train_model.py to try other ML models or add preprocessing

📝 Advanced Usage

➕ Add/Remove Features: Update columns in CSV and training script
📈 Map Salary Brackets: Replace income class with real salary values
☁️ Deploy: Host it on Streamlit Cloud or as an API with FastAPI

❓ FAQ
Q: Prediction seems off. What should I do?
A: Add more data samples, train with real salary values, or use advanced model tuning.

Q: Can I add more features like location or company size?
A: Yes! Just add new columns to the dataset and training pipeline.

📣 Credits
Built with ❤️ using:
Streamlit
scikit-learn
pandas


🚀 Ready to Explore Your Salary Potential?
Fire up the app and try it today!
