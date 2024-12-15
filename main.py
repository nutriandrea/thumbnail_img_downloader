import os
from PyPDF2 import PdfReader
from PIL import Image
from pdf2image import convert_from_path

def extract_first_page_as_png(pdf_folder, output_folder):
    # Crea la cartella di output se non esiste
    os.makedirs(output_folder, exist_ok=True)

    # Scorri tutti i file nella cartella dei PDF
    for file_name in os.listdir(pdf_folder):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, file_name)
            output_png_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.png")

            try:
                # Converte la prima pagina del PDF in un'immagine PNG
                images = convert_from_path(pdf_path, first_page=1, last_page=1)
                if images:
                    images[0].save(output_png_path, 'PNG')
                    print(f"Prima pagina estratta e salvata: {output_png_path}")
                else:
                    print(f"Impossibile estrarre la prima pagina da: {pdf_path}")
            except Exception as e:
                print(f"Errore durante l'elaborazione di {file_name}: {e}")

# Configura le cartelle
pdf_folder = "/Users/andreacacioppo/Downloads/wetransfer_pan-1-19_2024-12-12_0932"  # Sostituisci con il percorso della cartella dei PDF
output_folder = "/Users/andreacacioppo/Downloads/wetransfer_pan-1-19_2024-12-12_0932/png"  # Sostituisci con il percorso della cartella di output

extract_first_page_as_png(pdf_folder, output_folder)
