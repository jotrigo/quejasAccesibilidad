import pandas as pd
import os

def explore_excel_file(file_path: str):
    """Explorar la estructura de un archivo Excel"""
    if not os.path.exists(file_path):
        print(f"Archivo no encontrado: {file_path}")
        return
    
    print(f"\n{'='*60}")
    print(f"EXPLORANDO: {file_path}")
    print(f"{'='*60}")
    
    try:
        # Leer el archivo
        df = pd.read_excel(file_path)
        
        print(f"Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
        print(f"\nColumnas disponibles:")
        for i, col in enumerate(df.columns, 1):
            print(f"  {i}. {col}")
        
        print(f"\nPrimeras 3 filas:")
        print(df.head(3).to_string())
        
        print(f"\nTipos de datos:")
        print(df.dtypes)
        
        print(f"\nInformación básica:")
        print(df.info())
        
        # Buscar columnas con texto largo (posibles conversaciones)
        text_columns = []
        for col in df.columns:
            if df[col].dtype == 'object':
                # Verificar si hay texto largo
                max_length = df[col].astype(str).str.len().max()
                if max_length > 100:
                    text_columns.append((col, max_length))
        
        if text_columns:
            print(f"\nColumnas con texto largo (posibles conversaciones):")
            for col, max_len in sorted(text_columns, key=lambda x: x[1], reverse=True):
                print(f"  - {col}: máximo {max_len} caracteres")
        
        # Mostrar algunas muestras de texto largo
        if text_columns:
            print(f"\nMuestras de texto de la columna más larga:")
            longest_col = text_columns[0][0]
            samples = df[longest_col].dropna().head(2)
            for i, sample in enumerate(samples, 1):
                print(f"\nMuestra {i}:")
                print(f"'{str(sample)[:200]}...'")
        
    except Exception as e:
        print(f"Error al leer {file_path}: {e}")

def main():
    files = ["Casos 2022.xlsx", "Casos 2023.xlsx"]
    
    for file_path in files:
        explore_excel_file(file_path)

if __name__ == "__main__":
    main() 