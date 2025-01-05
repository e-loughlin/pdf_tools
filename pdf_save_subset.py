import argparse

from PyPDF2 import PdfReader, PdfWriter


def save_subset_pages(input_pdf, output_pdf, start, end=None):
    # Read the PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    num_pages = len(reader.pages)

    # Adjust for -1 to represent the last page
    if start == -1:
        start = num_pages - 1
    if end is None or end == -1:
        end = num_pages

    # Add selected pages to the writer
    for page_num in range(start, end):
        writer.add_page(reader.pages[page_num])

    # Write the new PDF
    with open(output_pdf, "wb") as f_out:
        writer.write(f_out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Save a subset of pages from a PDF.")
    parser.add_argument("input_pdf", help="Path to the input PDF file.")
    parser.add_argument("output_pdf", help="Path to save the output PDF file.")
    parser.add_argument(
        "--start",
        type=int,
        required=True,
        help="Start page index (0-based). Use -1 for the last page.",
    )
    parser.add_argument(
        "--end",
        type=int,
        default=None,
        help="End page index (0-based). Use -1 for the last page or leave blank to go to the end.",
    )

    args = parser.parse_args()

    save_subset_pages(args.input_pdf, args.output_pdf, args.start, args.end)
    print(
        f"Saved new PDF with pages from {args.start} to {args.end} as {args.output_pdf}"
    )
