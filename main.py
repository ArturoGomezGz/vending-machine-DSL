from lexer import lexer
from parser import Parser

# ==============================
# Ejemplo de uso
# ==============================
if __name__ == "__main__":
    import sys
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    try:
        with open(filename, encoding="utf-8") as f:
            script = f.read()
            tokens = lexer(script)          # Paso 1: análisis léxico
            parser = Parser(tokens)         # Paso 2: análisis sintáctico
            parser.parse_program()          # Validación
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo {filename}")
    except SyntaxError as e:
        print(f"Error de sintaxis: {e}")
