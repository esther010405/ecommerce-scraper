from scraper import get_products
from pathlib import Path
import pandas as pd

output = Path("outputs")
output.mkdir(exist_ok=True)

data = get_products()

df = pd.DataFrame(data)

df.to_excel(
    output / "products.xlsx",
    index=False
)

print("Fichier créé avec succès !")