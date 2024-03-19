import fitz  # PyMuPDF
from PIL import Image

def pdf_to_jpg(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)
    
    for page_number in range(pdf_document.page_count):
        page = pdf_document.load_page(page_number)
        pix = page.get_pixmap()
        
        jpg_file_path = f"{output_folder}/page_{page_number + 1}.jpg"
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(jpg_file_path)
        
        print(f"Converted page {page_number + 1} to {jpg_file_path}")

    pdf_document.close()

if __name__ == "__main__":
    pdf_file_path = "C:\Users\raush\Downloads\Aadhaar_Raunak[1].pdf"  # Replace with your PDF file path
    output_folder_path = "C:\Users\raush\Downloads"  # Replace with your desired output folder path
    
    pdf_to_jpg(pdf_file_path, output_folder_path)
