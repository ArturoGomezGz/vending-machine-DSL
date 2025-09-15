from lexer import lexer

# ==============================
# Parser por descenso recursivo
# ==============================
class Parser:
    def __init__(self, tokens):
        # Inicializa el parser con la lista de tokens y la posición actual
        self.tokens = tokens
        self.pos = 0

    def current(self):
        # Retorna el token actual o EOF si se terminó la lista
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ("EOF", None)

    def match(self, expected_type=None, expected_value=None):
        """
        Verifica que el token actual coincida con el tipo y/o valor esperado.
        Si no coincide, lanza un error de sintaxis.
        Avanza la posición del parser.
        """
        tok_type, tok_val = self.current()
        if expected_type and tok_type != expected_type:
            raise SyntaxError(f"Se esperaba tipo {expected_type}, pero se encontró {tok_type} ({tok_val})")
        if expected_value and tok_val != expected_value:
            raise SyntaxError(f"Se esperaba valor {expected_value}, pero se encontró {tok_val}")
        self.pos += 1
        return tok_type, tok_val

    def parse_program(self):
        """
        Analiza el programa completo recorriendo todos los tokens y procesando cada sentencia.
        """
        while self.current()[0] != "EOF":
            self.parse_statement()
        print("Programa válido ✅")

    def parse_statement(self):
        """
        Analiza una sentencia individual según el tipo y valor del token actual.
        Llama a 'match' para verificar la estructura de cada instrucción soportada.
        """
        tok_type, tok_val = self.current()

        if tok_type == "COMMENT":
            self.match("COMMENT")
        elif tok_val == "INSERT":
            self.match("KEYWORD", "INSERT")
            self.match("NUM")
        elif tok_val == "BALANCE":
            self.match("KEYWORD", "BALANCE")
        elif tok_val == "SELECT":
            self.match("KEYWORD", "SELECT")
            self.match("SPACE")
        elif tok_val == "PRICE":
            self.match("KEYWORD", "PRICE")
        elif tok_val == "DISPENSE":
            self.match("KEYWORD", "DISPENSE")
        elif tok_val == "CHANGE":
            self.match("KEYWORD", "CHANGE")
        elif tok_val == "CANCEL":
            self.match("KEYWORD", "CANCEL")
        elif tok_val == "ADD_PRODUCT":
            self.match("KEYWORD", "ADD_PRODUCT")
            self.match("PRODUCT")
        elif tok_val == "REMOVE_PRODUCT":
            self.match("KEYWORD", "REMOVE_PRODUCT")
            self.match("PRODUCT")
        elif tok_val == "SET_PRICE":
            self.match("KEYWORD", "SET_PRICE")
            self.match("PRODUCT")
            self.match("NUM")
        elif tok_val == "SET_SPACE":
            self.match("KEYWORD", "SET_SPACE")
            self.match("SPACE")
            self.match("PRODUCT")
        elif tok_val == "SET_STOCK":
            self.match("KEYWORD", "SET_STOCK")
            self.match("SPACE")
            self.match("NUM")
        elif tok_val == "LIST_PRODUCTS":
            self.match("KEYWORD", "LIST_PRODUCTS")
        elif tok_val == "SET_CAPACITY":
            self.match("KEYWORD", "SET_CAPACITY")
            self.match("NUM")
        elif tok_val == "SET_CURRENCY":
            self.match("KEYWORD", "SET_CURRENCY")
            self.match("PRODUCT")
        elif tok_val == "STATUS":
            self.match("KEYWORD", "STATUS")
        elif tok_val == "RESET":
            self.match("KEYWORD", "RESET")
        else:

            raise SyntaxError(f"Sentencia desconocida en {tok_val}")


if __name__ == "__main__":
    import sys
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            script = f.read()
        tokens = lexer(script)
        parser = Parser(tokens)
        parser.parse_program()
    except FileNotFoundError:
        print(f"Archivo no encontrado: {filename}")
    except SyntaxError as e:
        print(f"Error de sintaxis: {e}")
