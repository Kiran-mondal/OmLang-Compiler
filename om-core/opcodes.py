# =====================================================================
# MODULE: om-core/opcodes.py
# =====================================================================
class OpCode:
    LOAD_CONST = 0x01
    STORE_VAR  = 0x02
    LOAD_VAR   = 0x03
    ADD        = 0x04
    SUB        = 0x05
    MUL        = 0x06
    DIV        = 0x07
    PRINT      = 0x08
    HALT       = 0x00
    
