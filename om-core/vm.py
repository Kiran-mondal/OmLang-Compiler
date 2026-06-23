# =====================================================================
# MODULE: om-core/vm.py
# =====================================================================
import sys
try: from .opcodes import OpCode
except: from opcodes import OpCode

class OmVirtualMachine:
    def init(self, bytecode, constants):
        self.bytecode = bytecode; self.constants = constants
        self.stack = []; self.registers = {}; self.pc = 0

    def run(self):
        while self.pc < len(self.bytecode):
            op = self.bytecode[self.pc]
            
            if op == OpCode.HALT: break
            
            elif op == OpCode.LOAD_CONST:
                self.pc += 1
                self.stack.append(self.constants[self.bytecode[self.pc]])
            elif op == OpCode.STORE_VAR:
                self.pc += 1
                self.registers[self.bytecode[self.pc]] = self.stack.pop()
            elif op == OpCode.LOAD_VAR:
                self.pc += 1
                var_name = self.bytecode[self.pc]
                if var_name in self.registers: self.stack.append(self.registers[var_name])
                else: print(f"VM Error: Undefined '{var_name}'"); sys.exit(1)
            elif op == OpCode.INPUT:
                self.pc += 1
                user_val = input("> ")
                try: self.stack.append(float(user_val) if '.' in user_val else int(user_val))
                except ValueError: self.stack.append(user_val)
                
            # Math & Strings
            elif op == OpCode.ADD:
                b = self.stack.pop(); a = self.stack.pop()
                # If they are strings, Python concats them automatically!
                if isinstance(a, str) or isinstance(b, str): self.stack.append(str(a) + str(b))
                else: self.stack.append(a + b)
            elif op == OpCode.SUB: b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a - b)
            elif op == OpCode.MUL: b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a * b)
            elif op == OpCode.DIV: b = self.stack.pop(); a = self.stack.pop(); self.stack.append(a / b)
            
            # Logic Comparisons
            elif op == OpCode.CMP_EQ: b = self.stack.pop(); a = self.stack.pop(); self.stack.append(1 if a == b else 0)
            elif op == OpCode.CMP_LT: b = self.stack.pop(); a = self.stack.pop(); self.stack.append(1 if a < b else 0)
            elif op == OpCode.CMP_GT: b = self.stack.pop(); a = self.stack.pop(); self.stack.append(1 if a > b else 0)
            
            # Jumping / Looping
            elif op == OpCode.JUMP_FALSE:
                self.pc += 1
                target = self.bytecode[self.pc]
                condition = self.stack.pop()
                if condition == 0: 
                    self.pc = target
                    continue
            elif op == OpCode.JUMP:
                self.pc += 1
                self.pc = self.bytecode[self.pc]
                continue
                
            elif op == OpCode.PRINT:
                print(f"[OM VM OUTPUT]: {self.stack.pop()}")
                
            # Default Instruction Step
            if op not in (OpCode.LOAD_CONST, OpCode.STORE_VAR, OpCode.LOAD_VAR, OpCode.JUMP_FALSE, OpCode.JUMP, OpCode.INPUT):
                self.pc += 1