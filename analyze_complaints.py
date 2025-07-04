import pandas as pd
import openai
import os
from typing import List, Dict, Any
import json
from datetime import datetime
import time

class ComplaintAnalyzer:
    def __init__(self, api_key: str):
        """Initialize the analyzer with OpenAI API key"""
        self.client = openai.OpenAI(api_key=api_key)
        
    def read_excel_file(self, file_path: str) -> pd.DataFrame:
        """Read Excel file and return DataFrame"""
        try:
            df = pd.read_excel(file_path)
            print(f"Archivo {file_path} leído exitosamente. Columnas: {list(df.columns)}")
            print(f"Número de filas: {len(df)}")
            return df
        except Exception as e:
            print(f"Error al leer {file_path}: {e}")
            return pd.DataFrame()
    
    def analyze_conversation(self, conversation_text: str) -> Dict[str, Any]:
        """Analyze a single conversation using OpenAI API"""
        prompt = """
        Analiza la siguiente conversación y determina si contiene quejas sobre dispositivos.
        
        Instrucciones:
        1. Identifica si hay quejas sobre dispositivos (computadoras, teléfonos, tablets, impresoras, etc.)
        2. Clasifica el tipo de dispositivo mencionado
        3. Evalúa la gravedad de la queja (baja, media, alta)
        4. Extrae palabras clave relevantes
        
        Responde en formato JSON con la siguiente estructura:
        {
            "es_queja_dispositivo": true/false,
            "tipo_dispositivo": "string o null",
            "gravedad": "baja/media/alta o null",
            "palabras_clave": ["lista", "de", "palabras"],
            "resumen": "breve descripción de la queja"
        }
        
        Conversación a analizar:
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un analista experto en identificar quejas sobre dispositivos tecnológicos."},
                    {"role": "user", "content": prompt + conversation_text}
                ],
                temperature=0.1,
                max_tokens=500
            )
            
            result = response.choices[0].message.content
            return json.loads(result)
            
        except Exception as e:
            print(f"Error en análisis de OpenAI: {e}")
            return {
                "es_queja_dispositivo": False,
                "tipo_dispositivo": None,
                "gravedad": None,
                "palabras_clave": [],
                "resumen": "Error en análisis"
            }
    
    def process_file(self, file_path: str, max_conversations: int = None) -> List[Dict[str, Any]]:
        """Process all conversations in an Excel file"""
        df = self.read_excel_file(file_path)
        
        if df.empty:
            return []
        
        results = []
        
        # Limitar el número de conversaciones si se especifica
        if max_conversations:
            df = df.head(max_conversations)
        
        print(f"Procesando {len(df)} conversaciones...")
        
        for index, row in df.iterrows():
            print(f"Analizando conversación {index + 1}/{len(df)}")
            
            # Buscar columnas que puedan contener texto de conversación
            conversation_text = ""
            for col in df.columns:
                if isinstance(row[col], str) and len(str(row[col])) > 50:
                    conversation_text += str(row[col]) + " "
            
            if not conversation_text.strip():
                continue
            
            # Analizar la conversación
            analysis = self.analyze_conversation(conversation_text[:2000])  # Limitar a 2000 caracteres
            
            # Agregar información del archivo y fila
            result = {
                "archivo": file_path,
                "fila": index + 1,
                "texto_conversacion": conversation_text[:500] + "..." if len(conversation_text) > 500 else conversation_text,
                **analysis
            }
            
            results.append(result)
            
            # Pausa para evitar límites de rate
            time.sleep(0.5)
        
        return results
    
    def generate_report(self, results: List[Dict[str, Any]], output_file: str = None):
        """Generate a comprehensive report of the analysis"""
        if not results:
            print("No hay resultados para generar reporte")
            return
        
        # Filtrar solo quejas de dispositivos
        device_complaints = [r for r in results if r.get("es_queja_dispositivo", False)]
        
        # Estadísticas generales
        total_conversations = len(results)
        total_device_complaints = len(device_complaints)
        
        # Análisis por tipo de dispositivo
        device_types = {}
        severity_counts = {"baja": 0, "media": 0, "alta": 0}
        
        for complaint in device_complaints:
            device_type = complaint.get("tipo_dispositivo", "No especificado")
            device_types[device_type] = device_types.get(device_type, 0) + 1
            
            severity = complaint.get("gravedad", "No especificada")
            if severity in severity_counts:
                severity_counts[severity] += 1
        
        # Generar reporte
        report = {
            "fecha_analisis": datetime.now().isoformat(),
            "resumen": {
                "total_conversaciones": total_conversations,
                "quejas_dispositivos": total_device_complaints,
                "porcentaje_quejas": round((total_device_complaints / total_conversations) * 100, 2) if total_conversations > 0 else 0
            },
            "tipos_dispositivos": device_types,
            "gravedad_quejas": severity_counts,
            "quejas_detalladas": device_complaints
        }
        
        # Guardar reporte
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            print(f"Reporte guardado en: {output_file}")
        
        # Mostrar resumen en consola
        print("\n" + "="*50)
        print("REPORTE DE ANÁLISIS DE QUEJAS")
        print("="*50)
        print(f"Total de conversaciones analizadas: {total_conversations}")
        print(f"Quejas sobre dispositivos encontradas: {total_device_complaints}")
        print(f"Porcentaje de quejas: {report['resumen']['porcentaje_quejas']}%")
        
        if device_types:
            print("\nTipos de dispositivos más mencionados:")
            for device, count in sorted(device_types.items(), key=lambda x: x[1], reverse=True):
                print(f"  - {device}: {count}")
        
        if any(severity_counts.values()):
            print("\nDistribución por gravedad:")
            for severity, count in severity_counts.items():
                if count > 0:
                    print(f"  - {severity}: {count}")
        
        return report

def main():
    # Configurar API key de OpenAI
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: Debes configurar la variable de entorno OPENAI_API_KEY")
        print("Ejemplo: export OPENAI_API_KEY='tu-api-key-aqui'")
        return
    
    # Inicializar analizador
    analyzer = ComplaintAnalyzer(api_key)
    
    # Archivos a procesar
    files = ["Casos 2022.xlsx", "Casos 2023.xlsx"]
    
    all_results = []
    
    # Procesar cada archivo
    for file_path in files:
        if os.path.exists(file_path):
            print(f"\nProcesando archivo: {file_path}")
            results = analyzer.process_file(file_path, max_conversations=50)  # Limitar a 50 conversaciones por archivo
            all_results.extend(results)
        else:
            print(f"Archivo no encontrado: {file_path}")
    
    # Generar reporte
    if all_results:
        analyzer.generate_report(all_results, "reporte_quejas_dispositivos.json")
    else:
        print("No se encontraron resultados para analizar")

if __name__ == "__main__":
    main() 