
# Needs some updates to include all of Pythons Syntax soon™
# FIXES LOL BROKENER THEN I THAUGHT AGAIN HOURS WASTED HERE = 16

def main():
    import tiny_compiler                                # Import Package
    lexer = tiny_compiler.LEXER.Lexer("test.py")        # Initialize Lexer Instance  for Python
    tokens = lexer.tokenize()                           # Use Lexer Instance to get ur Tokens (@methods and triple " missing need to fix soon™)
    parser = tiny_compiler.PARSER.Parser(tokens)        # Initialize Parser Instance with ur Tokens
    ast = parser.parse()    	                        # Create AST Tree for further Use in Emitter or Instacer // or IR for VM 



if __name__ == "__main__":
    main()