import pandas as pd
import numpy as np

def creer_caracteristiques(df, groupes_principaux, groupes_secondaires, tous_exits):
    df['EstSenior'] = df['Age'].apply(lambda x: 1 if x >= 60 else 0)
    df['Actif_par_CarteCredit'] = df['PossedeCarteCredit'] * df['EstMembreActif']
    df['Produits_par_Anciennete'] = df['Anciennete'] / (df['NombreProduits'] + 1)
    df['CategorieAge'] = np.round(df['Age'] / 20).astype('int').astype('category')

    df = df.merge(groupes_principaux, how='left', on=['CustomerId', 'Surname', 'Geographie', 'Genre'])
    df = df.merge(groupes_secondaires, how='left', on=['CustomerId', 'Surname', 'Age', 'Genre'])
    df = df.merge(tous_exits, how='left')

    if 'Exited' in df.columns:
        for lag in range(1, 4):
            df[f'Exit_lag{lag}'] = df['Exited'].shift(lag)
        for lead in range(1, 4):
            df[f'Exit_lead{lead}'] = df['Exited'].shift(-lead)

    if 'Solde' in df.columns:
        df['Balance_lag_diff1'] = df['Solde'] - df['Solde'].shift(1)
        df['Balance_lead_diff1'] = df['Solde'] - df['Solde'].shift(-1)

    return df

from pretraitement_des_donnees import charger_donnees_pretraitees

chemin_dossier = "./Donnees/"
train, test = charger_donnees_pretraitees(chemin_dossier)

groupes_principaux = pd.DataFrame()
groupes_secondaires = pd.DataFrame()
tous_exits = pd.DataFrame()

train = creer_caracteristiques(train, groupes_principaux, groupes_secondaires, tous_exits)
test = creer_caracteristiques(test, groupes_principaux, groupes_secondaires, tous_exits)

if 'Solde' in train.columns and 'SalaireEstime' in train.columns:
    train['RatioSoldeSalaire'] = train['Solde'] / (train['SalaireEstime'] + 1)
    test['RatioSoldeSalaire'] = test['Solde'] / (test['SalaireEstime'] + 1)

if 'NombreProduits' in train.columns:
    train['TotalProduitsActifs'] = train['NombreProduits'] * train['EstMembreActif']
    test['TotalProduitsActifs'] = test['NombreProduits'] * test['EstMembreActif']

colonnes_a_supprimer = ['NumeroLigne', 'CustomerId', 'Surname']
train.drop(columns=[col for col in colonnes_a_supprimer if col in train.columns], inplace=True)
test.drop(columns=[col for col in colonnes_a_supprimer if col in test.columns], inplace=True)

train.to_csv(chemin_dossier + "train_caracteristiques.csv", index=False)
test.to_csv(chemin_dossier + "test_caracteristiques.csv", index=False)
