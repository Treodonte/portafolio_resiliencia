import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. CONFIGURACIÓN Y CARGA DE DATOS
# ==========================================
# Configurar estilo visual profesional
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'sans-serif'

print("Cargando datos...")
# Asegúrate de que el archivo se llame exactamente 'rs.csv'
df = pd.read_csv("rs.csv")

# ==========================================
# 2. PROCESAMIENTO DE DATOS
# ==========================================
# Renombrar columna para facilitar el trabajo
df = df.rename(columns={"Actualmente:": "grupo"})

# Separar los datos en dos grupos
grupo_estudio = df[df["grupo"] == "Estudio"]["PUNTAJE"]
grupo_trabajo = df[df["grupo"] == "Trabajo y estudio"]["PUNTAJE"]

# ==========================================
# 3. ESTADÍSTICA DESCRIPTIVA
# ==========================================
print("\n--- RESULTADOS ---")
print(f"Grupo Estudio (n={len(grupo_estudio)}): Media = {grupo_estudio.mean():.2f}")
print(f"Grupo Trabajo+Estudio (n={len(grupo_trabajo)}): Media = {grupo_trabajo.mean():.2f}")

# Nota sobre prueba inferencial (prueba de U de Mann-Whitney hecha en JASP por practicidad y confiabilidad)
print("\n--- PRUEBA INFERENCIAL (JASP) ---")
print("Prueba U de Mann-Whitney:")
print("U = 523.5, p = 0.396")
print("Interpretación: No hay diferencia significativa (p > 0.05).")

# ==========================================
# 4. VISUALIZACIÓN (BOXPLOT)
# ==========================================
print("\nGenerando gráfico...")

plt.figure(figsize=(10, 6))

# Crear el Boxplot
# palette=["#4C72B0", "#55A868"] pone colores
sns.boxplot(x="grupo", y="PUNTAJE", data=df, palette=["#4C72B0", "#55A868"], width=0.5)

# Añadir los puntos individuales (Stripplot) para ver la distribución real
sns.stripplot(x="grupo", y="PUNTAJE", data=df, color=".25", size=3, alpha=0.6)

# Títulos y etiquetas
plt.title('Comparación de Resiliencia (RS-14) por Grupo', fontsize=16, fontweight='bold')
plt.xlabel('Condición del Estudiante', fontsize=12)
plt.ylabel('Puntaje Total RS-14', fontsize=12)

# Añadir anotaciones de las medias en el gráfico
means = df.groupby('grupo')['PUNTAJE'].mean()
for i, group in enumerate(df['grupo'].unique()):
    plt.text(i, means[group] + 2, f'Media: {means[group]:.1f}', 
             horizontalalignment='center', size='medium', color='black', weight='semibold')

# Ajustar diseño
plt.tight_layout()

# Guardar la imagen en alta calidad
plt.savefig('grafico_resiliencia.png', dpi=300, bbox_inches='tight')
print("Gráfico guardado exitosamente como 'grafico_resiliencia.png'")

# Para mostrar el gráfico en pantalla.
plt.show()
