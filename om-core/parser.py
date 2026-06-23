# =====================================================================
# MODULE: om-core/parser.py
# =====================================================================
try:
    from .lexer import TokenType
except (ImportError, ValueError):
    from lexer import TokenType

# ... (Keep the rest of your AST nodes and OmParser class code exactly the same) ...