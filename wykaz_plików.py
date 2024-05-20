import pandas as pd
import os

# Pobierz listę plików w bieżącym katalogu
pliki = [plik for plik in os.listdir('.') if os.path.isfile(plik)]

# Stwórz DataFrame z nazwami plików bez rozszerzeń i pustymi nowymi nazwami
df = pd.DataFrame({
    'STARA_NAZWA': [os.path.splitext(plik)[0] for plik in pliki],
    'NOWA_NAZWA': ['' for _ in pliki]
})

# Zapisz DataFrame do pliku Excel
df.to_excel('zmiana.xlsx', index=False)

print("Plik Excel 'zmiana.xlsx' został stworzony.")
