#=========================================================================
def main():                                                     #   Status          #   Info & Usage
    import tiny_compiler                                        # working           # Import Package
    lexer = tiny_compiler.LEXER.Lexer("test.py")                # working           # Initialize Lexer Instance
    tokens = lexer.tokenize()                                   # working           # Use Lexer Instance to get ur Tokens (@methods and triple " missing need to fix soon™)
    #parser = tiny_compiler.PARSER.Parser(tokens)               # broken            # Initialize Parser Instance with ur Tokens
    #ast = parser.parse()    	                                # broken            # Create AST Tree for further Use in Emitter or Instacer // or IR for VM 
if __name__ == "__main__":
    main()
#=========================================================================
# @2025 EvieLyra™ + Casbian™
# #Python --> Anything Compiler#
# - Lexer
#       - complete Python Syntax
#       - regex to Token workflow
#       - Info Prints
#       - Debug Prints
# - Parser
#       - completely broken for NOW