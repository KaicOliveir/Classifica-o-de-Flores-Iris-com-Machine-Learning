import tensorflow as tf
import pandas as pd
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris = load_iris()

X = iris.data
y = iris.target

df = pd.DataFrame(X, columns=iris.feature_names)

df["especie"] = y

print(df.head())
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_treino = scaler.fit_transform(X_treino)

X_teste = scaler.transform(X_teste)

modelo = tf.keras.Sequential([
    tf.keras.Input(shape=(4,)),

    tf.keras.layers.Dense(
        16,
        activation="relu"
    ),

    tf.keras.layers.Dense(
        8,
        activation="relu"
    ),

    tf.keras.layers.Dense(
        3,
        activation="softmax"
    )
])

modelo.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
historico = modelo.fit(
    X_treino,
    y_treino,
    epochs=100,
    batch_size=16,
    validation_split=0.2,
    verbose=1
)

perda, precisao = modelo.evaluate(
    X_teste,
    y_teste,
    verbose=0
)

print(f"Perda no teste: {perda:.4f}")
print(f"Precisão no teste: {precisao * 100:.2f}%")

nova_flor = np.array([
    [5.1, 3.5, 1.4, 0.2]
])

nova_flor_normalizada = scaler.transform(nova_flor)

previsao = modelo.predict(
    nova_flor_normalizada,
    verbose=0
)

classe_prevista = np.argmax(previsao[0])

print("Espécie prevista:", iris.target_names[classe_prevista])

print("Probabilidades:", previsao[0])