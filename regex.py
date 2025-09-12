import re

# ==============================
# Regex del DSL
# ==============================

# Palabras reservadas
regex_keywords = re.compile(r"(INSERT|BALANCE|SELECT|PRICE|DISPENSE|CHANGE|CANCEL|"
                            r"ADD_PRODUCT|REMOVE_PRODUCT|SET_PRICE|SET_STOCK|"
                            r"LIST_PRODUCTS|SET_CAPACITY|SET_CURRENCY|STATUS|RESET)")

# Identificadores de productos (ej: COKE, WATER, CHIPS)
regex_identifier = re.compile(r"[A-Z][A-Z0-9_]*")

# Números (enteros y decimales) → primero enteros y después decimales
regex_number = re.compile(r"[0-9]+|[0-9]+\.[0-9]+")

# Comentarios (formato //** comentario **//)
regex_comment = re.compile(r"//\*\*.*\*\*//")

# ==============================
# Lexer
# ==============================
def lexer(script: str):
    tokens = []
    # Dividir el script en líneas
    for line in script.splitlines():
        line = line.strip()
        if not line:
            continue  # ignorar líneas vacías

        # Detectar comentarios
        if regex_comment.fullmatch(line):
            tokens.append(("COMMENT", line))
            continue

        # Dividir por espacios para analizar palabra por palabra
        for word in line.split():
            if regex_keywords.fullmatch(word):
                tokens.append(("KEYWORD", word))
            elif regex_number.fullmatch(word):
                tokens.append(("NUM", word))
            elif regex_identifier.fullmatch(word):
                tokens.append(("ID", word))
            else:
                tokens.append(("UNKNOWN", word))
    return tokens

# ==============================
# Ejemplo de uso
# ==============================
if __name__ == "__main__":
    # Leer el script desde el archivo 'reguex-input.txt'
    with open("reguex-input.txt", "r", encoding="utf-8") as f:
        script = f.read()

    result = lexer(script)
    for token in result:
        print(token)
