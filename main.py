from lexer import lexer
from parser import Parser

# ==============================
# Ejemplo de uso
# ==============================
if __name__ == "__main__":
    try:
        with open("input.txt", encoding="utf-8") as f:
            script = f.read()
            tokens = lexer(script)          # Paso 1: análisis léxico
            parser = Parser(tokens)         # Paso 2: análisis sintáctico
            parser.parse_program()          # Validación
    except FileNotFoundError:
        print("Error: no se encontró el archivo input.txt")
    except SyntaxError as e:
        print(f"Error de sintaxis: {e}")
