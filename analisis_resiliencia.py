import pandas as pd

# Cargar datos
df = pd.read_csv("rs.csv")

# Separar grupos
grupo_estudio = df[df["Actualmente:"] == "Estudio"]["PUNTAJE"]
grupo_trabajo = df[df["Actualmente:"] == "Trabajo y estudio"]["PUNTAJE"]

# Mostrar medias
print("Medias por grupo:")
print(f"Estudio:          {grupo_estudio.mean():.2f}")
print(f"Trabajo y estudio: {grupo_trabajo.mean():.2f}")

# Reportar resultado desde JASP (tu informe)
print("\nPrueba U de Mann-Whitney (realizada en JASP):")
print("U = 523.5, p = 0.396")
print("→ No hay diferencia significativa entre grupos (p > 0.05).")