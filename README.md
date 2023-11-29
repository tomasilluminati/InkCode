# ink_text - ANSI Text Colorizer and Formatter

`ink_text` is a Python function that colorizes and formats text for ANSI-compatible terminals. It provides a simple way to enhance the appearance of text by adding color and formatting options.

## Usage

```python
from ink_text import ink_text

text = "Hello, world!"
color = "green"
format = "bold"

result = ink_text(text, color, format)
print(result)
```

This example will print the text "Hello, world!" in bold green.

## Parameters

- `text` (str): The text to be colorized and formatted.
- `color` (str): The desired text color. Available colors are black, red, green, yellow, blue, magenta, cyan, and white.
- `format` (str, optional): The desired text format. Available formats are bold, faint, italic, underline, blink, reverse, crossed_out, double_underline, framed, encircled, overlined, and reset_all. Defaults to None.

## Return Value

The function returns a string containing the colorized and formatted text.

## Examples

```python
# Colorize text in red
red_text = ink_text("Error!", "red")
print(red_text)

# Format text with underline and color it blue
blue_underline_text = ink_text("Important", "blue", "underline")
print(blue_underline_text)
```

## Notes

- This function uses ANSI escape codes to apply color and formatting. It may not work properly in environments that do not support ANSI escape codes.

Feel free to use and modify this function to suit your needs. If you encounter any issues or have suggestions for improvement, please let us know.

**Note**: Make sure to handle exceptions appropriately when using this function to prevent unexpected behavior.
