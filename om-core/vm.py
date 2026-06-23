# =====================================================================
# MODULE: om-core/vm.py
# =====================================================================
import sys
try:
    from .opcodes import OpCode
except (ImportError, ValueError):
    from opcodes import OpCode

class OmVirtualMachine:
    def __init__(self, bytecode, constants):
        self.bytecode = bytecode
        self.constants = constants
        self.stack = []
        self.registers = {}
        self.pc = 0

    def run(self):
        while self.pc < len(self.bytecode):
            op = self.bytecode[self.pc]
            
            if op == OpCode.HALT:
                break
            elif op == OpCode.LOAD_CONST:
                self.pc += 1
                const_idx = self.bytecode[self.pc]
                self.stack.append(self.constants[const_idx])
            elif op == OpCode.STORE_VAR:
                self.pc += 1
                var_name = self.bytecode[self.pc]
                val = self.stack.pop()
                self.registers[var_name] = val
            elif op == OpCode.LOAD_VAR:
                self.pc += 1
                var_name = self.bytecode[self.pc]
                if var_name in self.registers:
                    self.stack.append(self.registers[var_name])
                else:
                    print(f"VM Runtime Error: Undefined variable '{var_name}'")
                    sys.exit(1)
            elif op == OpCode.ADD:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
            elif op == OpCode.SUB:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)
            elif op == OpCode.MUL:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a * b)
            elif op == OpCode.DIV:
                b = self.stack.pop()
                a = self.stack.pop()
                if b == 0:
                    print("VM Runtime Error: Division by Zero.")
                    sys.exit(1)
                self.stack.append(a / b)
            elif op == OpCode.PRINT:
                val = self.stack.pop()
                print(f"[OM VM OUTPUT]: {val}")
                
            self.pc += 1
            
