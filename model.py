import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# Colonnes du dataset NSL-KDD
columns = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes',
    'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot',
    'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell',
    'su_attempted', 'num_root', 'num_file_creations', 'num_shells',
    'num_access_files', 'num_outbound_cmds', 'is_host_login',
    'is_guest_login', 'count', 'srv_count', 'serror_rate',
    'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
    'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
    'dst_host_srv_count', 'dst_host_same_srv_rate',
    'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
    'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
    'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate', 'label', 'difficulty'
]

# Chargement des données
print("Chargement des données...")
train = pd.read_csv('KDDTrain+.txt', names=columns)
test = pd.read_csv('KDDTest+.txt', names=columns)

# Simplification des labels (Normal vs Attaque)
train['label'] = train['label'].apply(lambda x: 'normal' if x == 'normal' else 'attack')
test['label'] = test['label'].apply(lambda x: 'normal' if x == 'normal' else 'attack')

# Encodage des colonnes texte
le = LabelEncoder()
for col in ['protocol_type', 'service', 'flag']:
    train[col] = le.fit_transform(train[col])
    test[col] = le.transform(test[col])

# Préparation X et y
X_train = train.drop(['label', 'difficulty'], axis=1)
y_train = train['label']
X_test = test.drop(['label', 'difficulty'], axis=1)
y_test = test['label']

# Entraînement du modèle
print("Entraînement du modèle Random Forest...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Évaluation
print("Évaluation...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n✅ Accuracy: {accuracy * 100:.2f}%")
print("\n📊 Rapport de classification:")
print(classification_report(y_test, y_pred))

# Sauvegarde du modèle
with open('ids_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("\n✅ Modèle sauvegardé : ids_model.pkl")
