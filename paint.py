ForegroundGPallet = {
    'hard': '\x1b[38;2;29;32;33m',
    'medium': '\x1b[38;2;40;40;40m',
    'soft': '\x1b[38;2;50;48;47m',
    'default': '\x1b[38;2;235;219;178m',
    'black': '\x1b[38;2;40;40;40m',
    'dGrey': '\x1b[38;2;146;131;116m',
    'dRed': '\x1b[38;2;204;36;29m',
    'red': '\x1b[38;2;251;73;52m',
    'dGreen': '\x1b[38;2;152;151;26m',
    'green': '\x1b[38;2;184;187;38m',
    'dYellow': '\x1b[38;2;215;153;33m',
    'yellow': '\x1b[38;2;250;189;47m',
    'dBlue': '\x1b[38;2;69;133;136m',
    'blue': '\x1b[38;2;131;165;152m',
    'dMagenta': '\x1b[38;2;177;98;134m',
    'magenta': '\x1b[38;2;211;134;155m',
    'dCyan': '\x1b[38;2;104;157;106m',
    'cyan': '\x1b[38;2;142;192;124m',
    'grey': '\x1b[38;2;168;153;132m',
    'white': '\x1b[38;2;235;219;178m',
}
BackgroundGPallet = {
    '-hard': '\x1b[48;2;29;32;33m',
    '-medium': '\x1b[48;2;40;40;40m',
    '-soft': '\x1b[48;2;50;48;47m',
    '-default': '\x1b[48;2;235;219;178m',
    '-black': '\x1b[48;2;40;40;40m',
    '-dGrey': '\x1b[48;2;146;131;116m',
    '-dRed': '\x1b[48;2;204;36;29m',
    '-red': '\x1b[48;2;251;73;52m',
    '-dGreen': '\x1b[48;2;152;151;26m',
    '-green': '\x1b[48;2;184;187;38m',
    '-dYellow': '\x1b[48;2;215;153;33m',
    '-yellow': '\x1b[48;2;250;189;47m',
    '-dBlue': '\x1b[48;2;69;133;136m',
    '-blue': '\x1b[48;2;131;165;152m',
    '-dMagenta': '\x1b[48;2;177;98;134m',
    '-magenta': '\x1b[48;2;211;134;155m',
    '-dCyan': '\x1b[48;2;104;157;106m',
    '-cyan': '\x1b[48;2;142;192;124m',
    '-grey': '\x1b[48;2;168;153;132m',
    '-white': '\x1b[48;2;235;219;178m',
}
Styles = {
    'reset': '\x1b[0m',
    'bold': '\x1b[1m',
    'underlined': '\x1b[4m',
    'reversed': '\x1b[7m',
}

def stylize(string):
    for style in Styles:
        string = string.replace(f"[{style}]", Styles[style])
    return string

def paint(string, rgb, foreground = True, end = True):
    r, g, b = rgb
    type_ = 38 if foreground else 48
    return '\x1b' + f'[{type_};2;{r};{g};{b}m{string}' + (Styles['reset'] if end else "")

def cprint(string):
    from re import findall

    regex      = "\[\s*?\-?\s*?\d+\s*?,\s*?\d+\s*?,\s*?\d+\s*?\]"
    occurences = findall(regex, string)

    for occurence in occurences:
        type_   = False if findall("\-" , occurence) else True
        r, g, b = findall("\d+", occurence)

        string = string.replace(occurence, paint("", (int(r), int(g), int(b)), type_, False))

    for color in ForegroundGPallet:
        string = string.replace(f"[{color}]", ForegroundGPallet[color])

    for color in BackgroundGPallet:
        string = string.replace(f"[{color}]", BackgroundGPallet[color])

    print(stylize(string) + Styles['reset'])
