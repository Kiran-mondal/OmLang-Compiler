# =====================================================================
# MODULE: om-core/opcodes.py
# =====================================================================
class OpCode:
    LOAD_CONST = 0x01   # Load a constant value onto the data stack
    STORE_VAR  = 0x02   # Pop value from stack and store in variable register
    LOAD_VAR   = 0x03   # Load variable value onto the data stack
    ADD        = 0x04   # Pop two values, add them, push result
    SUB        = 0x05   # Pop two values, subtract them, push result
    MUL        = 0x06   # Pop two values, multiply them, push result
    DIV        = 0x07   # Pop two values, divide them, push result
    PRINT      = 0x08   # Pop value and print to native stdout
    HALT       = 0x00   # Safely stop execution of the virtual CPU