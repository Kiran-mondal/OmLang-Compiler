# =====================================================================
# MODULE: vm.py (VIRTUAL MACHINE MACHINE-CODE RUNTIME PROCESSOR)
# =====================================================================
# Note: In a multi-file layout, you would do:
# from opcodes import OpCode

class OmVirtualMachine:
    def init(self, bytecode, constants):
        self.bytecode = bytecode
        self.constants = constants
        self.stack = []       # Pure evaluation data stack (Last-In, First-Out)
        self.registers = {}   # Isolated internal memory registers for user variables
        self.pc = 0           # Program Counter (Instruction Pointer index)

    def run(self):
        """Main internal processor execution loop."""
        while self.pc < len(self.bytecode):
            op = self.bytecode[self.pc]
            
            if op == OpCode.HALT:
                break
                
            elif op == OpCode.LOAD_CONST:
                self.pc += 1
                const_idx = self.bytecode[self.pc]
                # Fetch target constant value from pool and push onto stack
                self.stack.append(self.constants[const_idx])
                
            elif op == OpCode.STORE_VAR:
                self.pc += 1
                var_name = self.bytecode[self.pc]
                # Allocate variable data register inside isolated internal state
                val = self.stack.pop()
                self.registers[var_name] = val
                
            elif op == OpCode.LOAD_VAR:
                self.pc += 1
                var_name = self.bytecode[self.pc]
                # Look up variable data and push value onto runtime evaluation stack
                if var_name in self.registers:
                    self.stack.append(self.registers[var_name])
                else:
                    print(f"VM Runtime Error: Attempted to reference undefined variable register '{var_name}'")
                    import sys; sys.exit(1)
                
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
                    print("VM Runtime Error: Scientific Math Exception - Division by Zero.")
                    import sys; sys.exit(1)
                self.stack.append(a / b)
                
            elif op == OpCode.PRINT:
                val = self.stack.pop()
                print(f"[OM VM OUTPUT]: {val}")
                
            # Tick the hardware instruction index clock step forward
            self.pc += 1