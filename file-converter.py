import sys
import markdown

def markdown_content(input_file, output_file):
  with open(input_file, "r", encoding="utf-8") as inputfile:
    text = inputfile.read()
    html = markdown.markdown(text)

  with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write(html)

if __name__ == "__main__":
  _, command, input_file, output_file = sys.argv

  if command == "markdown":
    markdown_content(input_file, output_file)

  else:
    print("Usage: python3 file_converter.py <input_file> <output_tile>")
