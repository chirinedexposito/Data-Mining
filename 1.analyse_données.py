
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des fichiers
df = pd.read_csv("/mnt/data/df.csv")
kaggle = pd.read_csv("/mnt/data/kaggle.csv")

# Informations générales sur les DataFrames
print("\nInformations sur le fichier df:")
print(df.info())
print("\nInformations sur le fichier kaggle:")
print(kaggle.info())

# Somme des deux DataFrames
df_aggregated = pd.concat([df, kaggle], ignore_index=True)
print("\nDimensions du DataFrame agrégé:", df_aggregated.shape)

# Analyse statistique
def describe_dataframe(df, title):
    print(f"\nRésumé statistique pour {title}:\n")
    print(df.describe(include='all'))

describe_dataframe(df, "df")
describe_dataframe(kaggle, "kaggle")
describe_dataframe(df_aggregated, "DataFrame agrégé")

# Visualisation des distributions
numerical_columns = df_aggregated.select_dtypes(include=['float64', 'int64']).columns
for col in numerical_columns:
    plt.figure(figsize=(12, 6))
    sns.histplot(df_aggregated[col], kde=True, stat='density')
    plt.title(f"Distribution de {col}")
    plt.xlabel(col)
    plt.ylabel("Densité")
    plt.show()

# Matrice de corrélation
plt.figure(figsize=(10, 8))
corr_matrix = df_aggregated.corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Matrice de corrélation (DataFrame agrégé)")
plt.show()

# Analyse des valeurs de la variable Exited
if 'Exited' in df_aggregated.columns:
    for col in numerical_columns:
        if col != 'Exited':
            plt.figure(figsize=(12, 6))
            sns.boxplot(x='Exited', y=col, data=df_aggregated, palette='coolwarm', showfliers=False)
            plt.title(f"Valeurs de {col} en fonction de Exited")
            plt.xlabel("Exited")
            plt.ylabel(col)
            plt.show()

    categorical_columns = df_aggregated.select_dtypes(include=['object', 'category']).columns
    for col in categorical_columns:
        if col != 'Exited':
            plt.figure(figsize=(12, 6))
            sns.countplot(x=col, hue='Exited', data=df_aggregated, palette='viridis')
            plt.title(f"Répartition de Exited par {col}")
            plt.xlabel(col)
            plt.ylabel("Count")
            plt.xticks(rotation=45)
            plt.show()

# Valeurs manquantes
def valeurs_manquantes(df, titre):
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if not missing.empty:
        print(f"\nValeurs manquantes pour {titre}:\n{missing}")

valeurs_manquantes(df, "df")
valeurs_manquantes(kaggle, "kaggle")
valeurs_manquantes(df_aggregated, "DataFrame agrégé")

# Analyse groupée de la variable Exited
if 'Exited' in df_aggregated.columns:
    grouped_data = df_aggregated.groupby('Exited').mean()
    print("\nMoyennes des variables numériques par Exited:")
    print(grouped_data)

    plt.figure(figsize=(14, 8))
    grouped_data.T.plot(kind='bar')
    plt.title("Moyenne des variables par groupe Exited")
    plt.xlabel("Variables")
    plt.ylabel("Valeurs moyennes")
    plt.xticks(rotation=45)
    plt.legend(title="Exited", loc='upper right')
    plt.tight_layout()
    plt.show()

# Distribution des variables catégoriques
categorical_columns = df_aggregated.select_dtypes(include=['object', 'category']).columns
for col in categorical_columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(x=col, data=df_aggregated, palette='pastel')
    plt.title(f"Distribution de {col} dans le DataFrame agrégé")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

# Analyse de corrélation spécifique
if 'Exited' in df_aggregated.columns:
    for col in numerical_columns:
        if col != 'Exited':
            correlation = df_aggregated[['Exited', col]].corr().iloc[0, 1]
            print(f"Corrélation entre Exited et {col}: {correlation:.2f}")

# Comparaison des variables par groupes multiples
if 'Geography' in df_aggregated.columns and 'Gender' in df_aggregated.columns:
    plt.figure(figsize=(14, 7))
    sns.countplot(x='Geography', hue='Gender', data=df_aggregated, palette='muted')
    plt.title("Distribution par Geography et Gender")
    plt.xlabel("Geography")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

if 'Geography' in df_aggregated.columns and 'Exited' in df_aggregated.columns:
    plt.figure(figsize=(14, 7))
    sns.countplot(x='Geography', hue='Exited', data=df_aggregated, palette='viridis')
    plt.title("Répartition de Exited par Geography")
    plt.xlabel("Geography")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()

# Exploration par groupes croisés de variables
if 'Exited' in df_aggregated.columns and 'Gender' in df_aggregated.columns:
    grouped_cross = df_aggregated.groupby(['Gender', 'Exited']).size().unstack(fill_value=0)
    print("\nRépartition croisée par Genre et Exited:")
    print(grouped_cross)

    grouped_cross.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='coolwarm')
    plt.title("Répartition croisée par Genre et Exited")
    plt.xlabel("Genre")
    plt.ylabel("Count")
    plt.legend(title="Exited")
    plt.show()

if 'Exited' in df_aggregated.columns and 'Geography' in df_aggregated.columns:
    grouped_geo = df_aggregated.groupby(['Geography', 'Exited']).size().unstack(fill_value=0)
    print("\nRépartition croisée par Geography et Exited:")
    print(grouped_geo)

    grouped_geo.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='viridis')
    plt.title("Répartition croisée par Geography et Exited")
    plt.xlabel("Geography")
    plt.ylabel("Count")
    plt.legend(title="Exited")
    plt.show()
