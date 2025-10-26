import sys
import markdown

def markdown_content(input_file, output_file):
  with open(input_file, "r", encoding="utf-8") as inputfile:
    text = inputfile.read()
    html = markdown.markdown(text)

  with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write(html)

if __name__ == "__main__":
  if len(sys.argv) != 4:
        print("Usage: python3 file_converter.py markdown <input_file> <output_file>")
        sys.exit(1)

  _, command, input_file, output_file = sys.argv

  if command == "markdown":
    markdown_content(input_file, output_file)

  else:
    print("Unknown command:", command)
    print("Usage: python3 file_converter.py markdown <input_file> <output_file>")
    sys.exit(1)
