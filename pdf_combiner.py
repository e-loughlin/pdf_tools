import argparse
import sys
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter


def combine_pdfs(files, output_pdf):
    writer = PdfWriter()
    for file in files:
        reader = PdfReader(file)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_pdf, "wb") as f_out:
        writer.write(f_out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combine multiple PDF files.")
    parser.add_argument("output_pdf", help="Name of the output combined PDF file.")
    parser.add_argument(
        "input_pdfs",
        nargs="*",
        help="List of PDF files to combine, if not using --all.",
    )
    parser.add_argument(
        "--all",
        metavar="DIRECTORY",
        help="Combine all PDFs in the specified directory.",
    )

    args = parser.parse_args()

    if args.all:
        # Get all PDF files in the specified directory
        target_dir = Path(args.all)
        if not target_dir.is_dir():
            print(f"Error: {args.all} is not a valid directory.")
            sys.exit(1)

        pdf_files = sorted([str(p) for p in target_dir.glob("*.pdf")])
        if not pdf_files:
            print(f"No PDF files found in the directory: {args.all}")
            sys.exit(1)
    else:
        # Use the provided list of PDF files
        pdf_files = args.input_pdfs
        if len(pdf_files) < 2:
            print(
                "Please specify at least two PDFs to combine or use the --all option with a directory."
            )
            sys.exit(1)

    combine_pdfs(pdf_files, args.output_pdf)
    print(f"Combined PDFs saved as {args.output_pdf}")
