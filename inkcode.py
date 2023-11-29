"""
-----------------------
|| INK CODE     V1.0 ||
-----------------------

by Tomás Illuminati

DEVELOPED IN PYTHON 3.11.0 64-bit
ENCODING: UTF-8
DATE: SEP 9 2023

This module provides a function for coloring and formatting text in ANSI-compatible terminals.

Usage:
    To colorize and format text, use the `ink_text` function. You can specify the text, color, and format.
    Available colors:
        - 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'
        - 'new' (for bold)
        - 'reset' (to reset formatting)

    Available formats:
        - 'bold'
        - 'faint'
        - 'italic'
        - 'blink'

    If the specified color or format is not valid, the function will return the text without modification.

Example:
    # Ink text in red and make it bold
    colored_text = ink_text("Hello, world!", "red", "bold")
    print(colored_text)

    # Ink text in green
    green_text = ink_text("Success!", "green")
    print(green_text)
"""

def ink_text(text, color, format=None):
    """
    Colorizes and formats text for ANSI-compatible terminals.

    Args:
        text (str): The text to be colorized and formatted.
        color (str): The desired text color.
        format (str, optional): The desired text format. Defaults to None.

    Returns:
        str: The colorized and formatted text.
    """
    color = color.lower()
    if format != None:
        format = format.lower()

    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'new': '\033[1m',
        'reset': '\033[0m'
    }

    formats = {
    'bold': '\033[1m',
    'faint': '\033[2m',
    'italic': '\033[3m',
    'underline': '\033[4m',
    'blink': '\033[5m',
    'reverse': '\033[7m',
    'crossed_out': '\033[9m',
    'double_underline': '\033[21m',  # Intensifica la línea subrayada
    'framed': '\033[51m',
    'encircled': '\033[52m',
    'overlined': '\033[53m',
    'reset_all': '\033[0m',  # Restablece todos los estilos a los valores predeterminados
}

    try:
        if format != None:
            if color in colors:
                if format in formats:
                    return f"{colors[color]}{formats[format]}{text}{colors['reset']}"
                else:
                    return text
        elif format == None:
            if color in colors:
                return f"{colors[color]}{text}{colors['reset']}"
            else:
                return text
        else:
            return text
    except:
        print(ink_text("Error: Wrong command use", "red", "bold"))
