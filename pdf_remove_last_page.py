import sys
from pdfrw import PdfReader, PdfWriter

def remove_last_page(input_pdf, output_pdf):
    # Read the PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Add all pages except the last one to the writer
    for page in reader.pages[:-1]:
        writer.addpage(page)

    # Write the new PDF
    writer.write(output_pdf)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_last_page.py input.pdf output.pdf")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]

    remove_last_page(input_pdf, output_pdf)
    print(f"Saved new PDF without the last page as {output_pdf}")
