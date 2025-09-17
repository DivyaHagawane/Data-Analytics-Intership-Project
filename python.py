import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog, messagebox
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns

df = None  # global DataFrame
log_model, rf_model = None, None  # ML models
label_encoders = {}  # store encoders for categorical columns

# Load Excel
def load_file():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        try:
            df = pd.read_excel(file_path)
            messagebox.showinfo("Success", "Sports Data File Loaded Successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Cannot read file\n{e}")

# Clean data
def clean_data():
    global df
    if df is None:
        messagebox.showerror("Error", "Load a file first!")
        return
    before = df.shape[0]
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    after = df.shape[0]
    messagebox.showinfo("Cleaning Done", f"Removed {before - after} rows.")

# Analyze data
def analyze_data():
    global df
    if df is None:
        messagebox.showerror("Error", "Load a file first!")
        return
    try:
        total_players = df['Player_ID'].nunique()
        Wins = df['Wins'].sum()
        avg_score = df['Average_Score'].mean()
        Total_score = df['Total_Score'].mean()

        result.set(f"Total Players: {total_players}\n"
                   f"Win Players: {Wins}\n"
                   f"Avg Performance Score: {avg_score:.2f}\n"
                   f"Total_Score: {Total_score:.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Analysis failed\n{e}")

# Create charts
def create_charts():
    global df
    if df is None:
        messagebox.showerror("Error", "Load a file first!")
        return
    try:
        # Sport distribution
        df['Sport'].value_counts().plot(kind='bar', title="Sport Distribution")
        plt.xlabel("Sport (0=No, 1=Yes)")
        plt.ylabel("Count")
        plt.show()

        # City breakdown
        df['City'].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title("City Distribution")
        plt.ylabel("")
        plt.show()


    except Exception as e:
        messagebox.showerror("Error", f"Charts failed\n{e}")


# ---------------- GUI ----------------
root = Tk()
root.title("🏆 Sports Player Performance Prediction System")
root.geometry("600x480")

Button(root, text=" Load File", command=load_file, width=30).pack(pady=5)
Button(root, text=" Clean Data", command=clean_data, width=30).pack(pady=5)
Button(root, text=" Analyze Data", command=analyze_data, width=30).pack(pady=5)
Button(root, text=" Create Charts", command=create_charts, width=30).pack(pady=5)

result = StringVar()
Label(root, textvariable=result, bg="white", width=70, height=8, anchor="w", justify=LEFT).pack(pady=10)

root.mainloop()