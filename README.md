# INK CODE

by Tomás Illuminati

DEVELOPED IN PYTHON 3.11.0 64-bit
ENCODING: UTF-8
DATE: SEP 9 2023 

This module provides a function for coloring and formatting text in ANSI-compatible terminals.

## Usage

To colorize and format text, use the `ink_text` function. You can specify the text, color, and format.

### Available colors:

- 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
- 'new' (for bold)
- 'reset' (to reset formatting)

### Available formats:

- 'bold'
- 'faint'
- 'italic'
- 'blink'

If the specified color or format is not valid, the function will return the text without modification.

## Example

```python
# Ink text in red and make it bold
colored_text = ink_text("Hello, world!", "red", "bold")
print(colored_text)

# Ink text in green
green_text = ink_text("Success!", "green")
print(green_text)
