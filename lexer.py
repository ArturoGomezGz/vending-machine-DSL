import re

# ==============
# Regex del DSL 
# ==============

# Palabras reservadas
regex_keywords = re.compile(
    r"(INSERT|BALANCE|SELECT|PRICE|DISPENSE|CHANGE|CANCEL|"
    r"ADD_PRODUCT|REMOVE_PRODUCT|SET_PRICE|SET_STOCK|LIST_PRODUCTS|"
    r"SET_SPACE|SET_CAPACITY|SET_CURRENCY|STATUS|RESET)"
)

# Identificadores de productos (ej: COFFEE, CHIPS, WATER)
regex_product = re.compile(r"[A-Z][A-Z0-9_]*")

# Identificadores de espacios físicos (ej: A4, B9, C12)
regex_space = re.compile(r"[A-Z][0-9]+")

# Números (enteros y decimales)
regex_number = re.compile(r"[0-9]+|[0-9]+\.[0-9]+")

# Comentarios (líneas que empiezan con //** y terminan con **//)
regex_comment = re.compile(r"//\*\*.*\*\*//")

# ==============================
# Lexer
# ==============================
def lexer(script: str):
    tokens = []
    for line in script.splitlines():
        line = line.strip()
        if not line:
            continue

        # Comentarios
        if regex_comment.fullmatch(line):
            tokens.append(("COMMENT", line))
            continue

        # Analizar palabra por palabra
        for word in line.split():
            if regex_keywords.fullmatch(word):
                tokens.append(("KEYWORD", word))
            elif regex_number.fullmatch(word):
                tokens.append(("NUM", word))
            elif regex_space.fullmatch(word):
                tokens.append(("SPACE", word))
            elif regex_product.fullmatch(word):
                tokens.append(("PRODUCT", word))
            else:
                tokens.append(("UNKNOWN", word))
    return tokens


if __name__ == "__main__":
    import sys
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            script = f.read()
        tokens = lexer(script)
        for token in tokens:
            print(token)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {filename}")
