import argparse
import os
import subprocess

def get_file_size(file_path):
    """Return the file size in kilobytes (KB)."""
    return os.path.getsize(file_path) / 1024

def map_percentage_to_preset(percentage):
    """
    Map a compression percentage to a Ghostscript preset.

    Args:
        percentage (int): Compression percentage (0-100).

    Returns:
        str: Corresponding Ghostscript preset.
    """
    if percentage <= 25:
        return "/screen"
    elif percentage <= 50:
        return "/ebook"
    elif percentage <= 75:
        return "/printer"
    else:
        return "/prepress"

def compress_pdf(input_file, output_file, compression_percentage):
    """
    Compress a PDF file using Ghostscript with a percentage-based quality setting.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path to the output compressed PDF file.
        compression_percentage (int): Compression percentage (0-100).
    """
    preset = map_percentage_to_preset(compression_percentage)

    try:
        # Get and display input file size
        input_size = get_file_size(input_file)
        print(f"Input file size: {input_size:.2f} KB")

        # Ghostscript command
        gs_command = [
            "ghostscript",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS={preset}",
            "-q",
            "-o", output_file,
            input_file,
        ]

        # Execute Ghostscript
        subprocess.run(gs_command, check=True)

        # Get and display output file size
        output_size = get_file_size(output_file)
        print(f"Output file size: {output_size:.2f} KB")
        print(f"Compression complete. Output saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Ghostscript failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Compress PDF files using Ghostscript with percentage quality.")
    parser.add_argument("input", help="Path to the input PDF file.")
    parser.add_argument("output", help="Path to the output compressed PDF file.")
    parser.add_argument(
        "--percentage",
        type=int,
        default=50,
        choices=range(0, 101),
        help="Compression percentage (0-100, default is 50). Lower percentages yield higher compression.",
    )

    args = parser.parse_args()
    compress_pdf(args.input, args.output, args.percentage)

if __name__ == "__main__":
    main()
