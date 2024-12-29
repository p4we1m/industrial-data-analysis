from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pandas as pd

# Wczytaj dane
df = pd.read_csv("../data/synthetic_machine_data.csv")
features = ["temperature", "vibration", "pressure"]
X = df[features]
y = df["failure"]

# Podział na zbiory
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Trening modelu
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Ocena modelu
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
