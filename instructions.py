# This is a generated file.

def NOP_00(cpu):
	# NOP	(Misc/control instructions)
	cpu.PC += 1
	pass
	return 4

def LD_01(cpu, v):
	# LD BC,d16	(16bit load/store/move instructions)
	cpu.PC += 3
	cpu.B = v >> 8
	cpu.C = v & 0xFF
	return 12

def LD_02(cpu):
	# LD (BC),A	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.memory.write_byte((cpu.B << 8) + cpu.C, cpu.A)
	return 8

def INC_03(cpu):
	# INC BC	(16bit arithmetic/logical instructions)
	cpu.PC += 1
	t = ((cpu.B << 8) + cpu.C) + 1
	t &= 0xFFFF
	cpu.B = t >> 8
	cpu.C = t & 0xFF
	return 8

def INC_04(cpu):
	# INC B	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.B + 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.B & 0x0F) + 1) > 0x0F
	t &= 0xFF
	cpu.B = t
	return 4

def DEC_05(cpu):
	# DEC B	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.B - 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.B & 0x0F) - 1) < 0
	t &= 0xFF
	cpu.B = t
	return 4

def LD_06(cpu, v):
	# LD B,d8	(8bit load/store/move instructions)
	cpu.PC += 2
	cpu.B = v
	return 8

def RLCA_07(cpu):
	# RLCA	(8bit rotations/shifts and bit instructions)
	cpu.PC += 1
	t = (cpu.A << 1) + (cpu.A >> 7)
	cpu.FLAG_Z = 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def LD_08(cpu, v):
	# LD (a16),SP	(16bit load/store/move instructions)
	cpu.PC += 3
	cpu.memory.write_byte(v, cpu.SP & 0x00FF)   # Low Byte
	cpu.memory.write_byte(v + 1, (cpu.SP & 0xFF00) >> 8) # High Byte
	return 20

def ADD_09(cpu):
	# ADD HL,BC	(16bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.HL + ((cpu.B << 8) + cpu.C)
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.HL & 0x0FFF) + (((cpu.B << 8) + cpu.C) & 0x0FFF)) > 0x0FFF
	cpu.FLAG_C = t > 0xFFFF
	t &= 0xFFFF
	cpu.HL = t
	return 8

def LD_0A(cpu):
	# LD A,(BC)	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = cpu.memory.read_byte(((cpu.B << 8) + cpu.C))
	return 8

def DEC_0B(cpu):
	# DEC BC	(16bit arithmetic/logical instructions)
	cpu.PC += 1
	t = ((cpu.B << 8) + cpu.C) - 1
	t &= 0xFFFF
	cpu.B = t >> 8
	cpu.C = t & 0xFF
	return 8

def INC_0C(cpu):
	# INC C	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.C + 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.C & 0x0F) + 1) > 0x0F
	t &= 0xFF
	cpu.C = t
	return 4

def DEC_0D(cpu):
	# DEC C	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.C - 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.C & 0x0F) - 1) < 0
	t &= 0xFF
	cpu.C = t
	return 4

def LD_0E(cpu, v):
	# LD C,d8	(8bit load/store/move instructions)
	cpu.PC += 2
	cpu.C = v
	return 8

def RRCA_0F(cpu):
	# RRCA	(8bit rotations/shifts and bit instructions)
	cpu.PC += 1
	t = (cpu.A >> 1) + ((cpu.A & 1) << 7) + ((cpu.A & 1) << 8)
	cpu.FLAG_Z = 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def STOP_10(cpu, v):
	# STOP 0	(Misc/control instructions)
	cpu.PC += 2
	# TODO: Implement it
	pass
	return 4

def LD_11(cpu, v):
	# LD DE,d16	(16bit load/store/move instructions)
	cpu.PC += 3
	cpu.D = v >> 8
	cpu.E = v & 0xFF
	return 12

def LD_12(cpu):
	# LD (DE),A	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.memory.write_byte((cpu.D << 8) + cpu.E, cpu.A)
	return 8

def INC_13(cpu):
	# INC DE	(16bit arithmetic/logical instructions)
	cpu.PC += 1
	t = ((cpu.D << 8) + cpu.E) + 1
	t &= 0xFFFF
	cpu.D = t >> 8
	cpu.E = t & 0xFF
	return 8

def INC_14(cpu):
	# INC D	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.D + 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.D & 0x0F) + 1) > 0x0F
	t &= 0xFF
	cpu.D = t
	return 4

def DEC_15(cpu):
	# DEC D	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.D - 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.D & 0x0F) - 1) < 0
	t &= 0xFF
	cpu.D = t
	return 4

def LD_16(cpu, v):
	# LD D,d8	(8bit load/store/move instructions)
	cpu.PC += 2
	cpu.D = v
	return 8

def RLA_17(cpu):
	# RLA	(8bit rotations/shifts and bit instructions)
	cpu.PC += 1
	t = (cpu.A << 1) + cpu.FLAG_C
	cpu.FLAG_Z = 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def JR_18(cpu, v):
	# JR r8	(Jumps/calls)
	cpu.PC += 2
	cpu.PC = (cpu.PC + ((v ^ 0x80) - 0x80)) & 0xFFFF
	return 12

def ADD_19(cpu):
	# ADD HL,DE	(16bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.HL + ((cpu.D << 8) + cpu.E)
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.HL & 0x0FFF) + (((cpu.D << 8) + cpu.E) & 0x0FFF)) > 0x0FFF
	cpu.FLAG_C = t > 0xFFFF
	t &= 0xFFFF
	cpu.HL = t
	return 8

def LD_1A(cpu):
	# LD A,(DE)	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = cpu.memory.read_byte(((cpu.D << 8) + cpu.E))
	return 8

def DEC_1B(cpu):
	# DEC DE	(16bit arithmetic/logical instructions)
	cpu.PC += 1
	t = ((cpu.D << 8) + cpu.E) - 1
	t &= 0xFFFF
	cpu.D = t >> 8
	cpu.E = t & 0xFF
	return 8

def INC_1C(cpu):
	# INC E	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.E + 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.E & 0x0F) + 1) > 0x0F
	t &= 0xFF
	cpu.E = t
	return 4

def DEC_1D(cpu):
	# DEC E	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.E - 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.E & 0x0F) - 1) < 0
	t &= 0xFF
	cpu.E = t
	return 4

def LD_1E(cpu, v):
	# LD E,d8	(8bit load/store/move instructions)
	cpu.PC += 2
	cpu.E = v
	return 8

def RRA_1F(cpu):
	# RRA	(8bit rotations/shifts and bit instructions)
	cpu.PC += 1
	t = (cpu.A >> 1) + (cpu.FLAG_C << 7) + ((cpu.A & 1) << 8)
	cpu.FLAG_Z = 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def JR_20(cpu, v):
	# JR NZ,r8	(Jumps/calls)
	cpu.PC += 2
	if not cpu.FLAG_Z:
		cpu.PC = (cpu.PC + ((v ^ 0x80) - 0x80)) & 0xFFFF
		return 12
	else:
		return 8

def LD_21(cpu, v):
	# LD HL,d16	(16bit load/store/move instructions)
	cpu.PC += 3
	cpu.HL = v
	return 12

def LD_22(cpu):
	# LD (HL+),A	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.memory.write_byte(cpu.HL, cpu.A & 0xFF)
	cpu.HL += 1
	return 8

def INC_23(cpu):
	# INC HL	(16bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.HL + 1
	t &= 0xFFFF
	cpu.HL = t
	return 8

def INC_24(cpu):
	# INC H	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = (cpu.HL >> 8) + 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = (((cpu.HL >> 8) & 0x0F) + 1) > 0x0F
	t &= 0xFF
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 4

def DEC_25(cpu):
	# DEC H	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = (cpu.HL >> 8) - 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = (((cpu.HL >> 8) & 0x0F) - 1) < 0
	t &= 0xFF
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 4

def LD_26(cpu, v):
	# LD H,d8	(8bit load/store/move instructions)
	cpu.PC += 2
	cpu.HL = (cpu.HL & 0x00FF) | (v << 8)
	return 8

def DAA_27(cpu):
	# DAA	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A
	if cpu.FLAG_H or (t & 0x0F) > 0x09:
		t += -0x06 if cpu.FLAG_N else +0x06
	if cpu.FLAG_C or (t >> 4) > 0x09:
		t += -0x60 if cpu.FLAG_N else +0x60
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = cpu.FLAG_C | t > 0xFF
	cpu.A = t & 0xFF
	return 4

def JR_28(cpu, v):
	# JR Z,r8	(Jumps/calls)
	cpu.PC += 2
	if cpu.FLAG_Z:
		cpu.PC = (cpu.PC + ((v ^ 0x80) - 0x80)) & 0xFFFF
		return 12
	else:
		return 8

def ADD_29(cpu):
	# ADD HL,HL	(16bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.HL + cpu.HL
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.HL & 0x0FFF) + (cpu.HL & 0x0FFF)) > 0x0FFF
	cpu.FLAG_C = t > 0xFFFF
	t &= 0xFFFF
	cpu.HL = t
	return 8

def LD_2A(cpu):
	# LD A,(HL+)	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = cpu.memory.read_byte(cpu.HL)
	cpu.HL += 1
	return 8

def DEC_2B(cpu):
	# DEC HL	(16bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.HL - 1
	t &= 0xFFFF
	cpu.HL = t
	return 8

def INC_2C(cpu):
	# INC L	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = (cpu.HL & 0x00FF) + 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = (((cpu.HL & 0x00FF) & 0x0F) + 1) > 0x0F
	t &= 0xFF
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 4

def DEC_2D(cpu):
	# DEC L	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = (cpu.HL & 0x00FF) - 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = (((cpu.HL & 0x00FF) & 0x0F) - 1) < 0
	t &= 0xFF
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 4

def LD_2E(cpu, v):
	# LD L,d8	(8bit load/store/move instructions)
	cpu.PC += 2
	cpu.HL = (cpu.HL & 0xFF00) | (v & 0xFF)
	return 8

def CPL_2F(cpu):
	# CPL	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	cpu.A =  0xFF ^ cpu.A
	cpu.FLAG_N = 1
	cpu.FLAG_H = 1
	return 4

def JR_30(cpu, v):
	# JR NC,r8	(Jumps/calls)
	cpu.PC += 2
	if not cpu.FLAG_C:
		cpu.PC = (cpu.PC + ((v ^ 0x80) - 0x80)) & 0xFFFF
		return 12
	else:
		return 8

def LD_31(cpu, v):
	# LD SP,d16	(16bit load/store/move instructions)
	cpu.PC += 3
	cpu.SP = v
	return 12

def LD_32(cpu):
	# LD (HL-),A	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.memory.write_byte(cpu.HL, cpu.A & 0xFF)
	cpu.HL -= 1
	return 8

def INC_33(cpu):
	# INC SP	(16bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.SP + 1
	t &= 0xFFFF
	cpu.SP = t
	return 8

def INC_34(cpu):
	# INC (HL)	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.memory.read_byte(cpu.HL) + 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.memory.read_byte(cpu.HL) & 0x0F) + 1) > 0x0F
	t &= 0xFF
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 12

def DEC_35(cpu):
	# DEC (HL)	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.memory.read_byte(cpu.HL) - 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.memory.read_byte(cpu.HL) & 0x0F) - 1) < 0
	t &= 0xFF
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 12

def LD_36(cpu, v):
	# LD (HL),d8	(8bit load/store/move instructions)
	cpu.PC += 2
	cpu.memory.write_byte(cpu.HL, v & 0xFF)
	return 12

def SCF_37(cpu):
	# SCF	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 1
	return 4

def JR_38(cpu, v):
	# JR C,r8	(Jumps/calls)
	cpu.PC += 2
	if cpu.FLAG_C:
		cpu.PC = (cpu.PC + ((v ^ 0x80) - 0x80)) & 0xFFFF
		return 12
	else:
		return 8

def ADD_39(cpu):
	# ADD HL,SP	(16bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.HL + cpu.SP
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.HL & 0x0FFF) + (cpu.SP & 0x0FFF)) > 0x0FFF
	cpu.FLAG_C = t > 0xFFFF
	t &= 0xFFFF
	cpu.HL = t
	return 8

def LD_3A(cpu):
	# LD A,(HL-)	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = cpu.memory.read_byte(cpu.HL)
	cpu.HL -= 1
	return 8

def DEC_3B(cpu):
	# DEC SP	(16bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.SP - 1
	t &= 0xFFFF
	cpu.SP = t
	return 8

def INC_3C(cpu):
	# INC A	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + 1) > 0x0F
	t &= 0xFF
	cpu.A = t
	return 4

def DEC_3D(cpu):
	# DEC A	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - 1
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - 1) < 0
	t &= 0xFF
	cpu.A = t
	return 4

def LD_3E(cpu, v):
	# LD A,d8	(8bit load/store/move instructions)
	cpu.PC += 2
	cpu.A = v
	return 8

def CCF_3F(cpu):
	# CCF	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = not cpu.FLAG_C
	return 4

def LD_40(cpu):
	# LD B,B	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.B = cpu.B
	return 4

def LD_41(cpu):
	# LD B,C	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.B = cpu.C
	return 4

def LD_42(cpu):
	# LD B,D	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.B = cpu.D
	return 4

def LD_43(cpu):
	# LD B,E	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.B = cpu.E
	return 4

def LD_44(cpu):
	# LD B,H	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.B = (cpu.HL >> 8)
	return 4

def LD_45(cpu):
	# LD B,L	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.B = (cpu.HL & 0x00FF)
	return 4

def LD_46(cpu):
	# LD B,(HL)	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.B = cpu.memory.read_byte(cpu.HL)
	return 8

def LD_47(cpu):
	# LD B,A	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.B = cpu.A
	return 4

def LD_48(cpu):
	# LD C,B	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.C = cpu.B
	return 4

def LD_49(cpu):
	# LD C,C	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.C = cpu.C
	return 4

def LD_4A(cpu):
	# LD C,D	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.C = cpu.D
	return 4

def LD_4B(cpu):
	# LD C,E	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.C = cpu.E
	return 4

def LD_4C(cpu):
	# LD C,H	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.C = (cpu.HL >> 8)
	return 4

def LD_4D(cpu):
	# LD C,L	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.C = (cpu.HL & 0x00FF)
	return 4

def LD_4E(cpu):
	# LD C,(HL)	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.C = cpu.memory.read_byte(cpu.HL)
	return 8

def LD_4F(cpu):
	# LD C,A	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.C = cpu.A
	return 4

def LD_50(cpu):
	# LD D,B	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.D = cpu.B
	return 4

def LD_51(cpu):
	# LD D,C	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.D = cpu.C
	return 4

def LD_52(cpu):
	# LD D,D	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.D = cpu.D
	return 4

def LD_53(cpu):
	# LD D,E	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.D = cpu.E
	return 4

def LD_54(cpu):
	# LD D,H	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.D = (cpu.HL >> 8)
	return 4

def LD_55(cpu):
	# LD D,L	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.D = (cpu.HL & 0x00FF)
	return 4

def LD_56(cpu):
	# LD D,(HL)	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.D = cpu.memory.read_byte(cpu.HL)
	return 8

def LD_57(cpu):
	# LD D,A	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.D = cpu.A
	return 4

def LD_58(cpu):
	# LD E,B	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.E = cpu.B
	return 4

def LD_59(cpu):
	# LD E,C	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.E = cpu.C
	return 4

def LD_5A(cpu):
	# LD E,D	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.E = cpu.D
	return 4

def LD_5B(cpu):
	# LD E,E	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.E = cpu.E
	return 4

def LD_5C(cpu):
	# LD E,H	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.E = (cpu.HL >> 8)
	return 4

def LD_5D(cpu):
	# LD E,L	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.E = (cpu.HL & 0x00FF)
	return 4

def LD_5E(cpu):
	# LD E,(HL)	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.E = cpu.memory.read_byte(cpu.HL)
	return 8

def LD_5F(cpu):
	# LD E,A	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.E = cpu.A
	return 4

def LD_60(cpu):
	# LD H,B	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0x00FF) | (cpu.B << 8)
	return 4

def LD_61(cpu):
	# LD H,C	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0x00FF) | (cpu.C << 8)
	return 4

def LD_62(cpu):
	# LD H,D	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0x00FF) | (cpu.D << 8)
	return 4

def LD_63(cpu):
	# LD H,E	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0x00FF) | (cpu.E << 8)
	return 4

def LD_64(cpu):
	# LD H,H	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0x00FF) | ((cpu.HL >> 8) << 8)
	return 4

def LD_65(cpu):
	# LD H,L	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0x00FF) | ((cpu.HL & 0x00FF) << 8)
	return 4

def LD_66(cpu):
	# LD H,(HL)	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0x00FF) | (cpu.memory.read_byte(cpu.HL) << 8)
	return 8

def LD_67(cpu):
	# LD H,A	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0x00FF) | (cpu.A << 8)
	return 4

def LD_68(cpu):
	# LD L,B	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0xFF00) | (cpu.B & 0xFF)
	return 4

def LD_69(cpu):
	# LD L,C	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0xFF00) | (cpu.C & 0xFF)
	return 4

def LD_6A(cpu):
	# LD L,D	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0xFF00) | (cpu.D & 0xFF)
	return 4

def LD_6B(cpu):
	# LD L,E	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0xFF00) | (cpu.E & 0xFF)
	return 4

def LD_6C(cpu):
	# LD L,H	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0xFF00) | ((cpu.HL >> 8) & 0xFF)
	return 4

def LD_6D(cpu):
	# LD L,L	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0xFF00) | ((cpu.HL & 0x00FF) & 0xFF)
	return 4

def LD_6E(cpu):
	# LD L,(HL)	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0xFF00) | (cpu.memory.read_byte(cpu.HL) & 0xFF)
	return 8

def LD_6F(cpu):
	# LD L,A	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0xFF00) | (cpu.A & 0xFF)
	return 4

def LD_70(cpu):
	# LD (HL),B	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.memory.write_byte(cpu.HL, cpu.B & 0xFF)
	return 8

def LD_71(cpu):
	# LD (HL),C	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.memory.write_byte(cpu.HL, cpu.C & 0xFF)
	return 8

def LD_72(cpu):
	# LD (HL),D	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.memory.write_byte(cpu.HL, cpu.D & 0xFF)
	return 8

def LD_73(cpu):
	# LD (HL),E	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.memory.write_byte(cpu.HL, cpu.E & 0xFF)
	return 8

def LD_74(cpu):
	# LD (HL),H	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.memory.write_byte(cpu.HL, (cpu.HL >> 8) & 0xFF)
	return 8

def LD_75(cpu):
	# LD (HL),L	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.memory.write_byte(cpu.HL, (cpu.HL & 0x00FF) & 0xFF)
	return 8

def HALT_76(cpu):
	# HALT	(Misc/control instructions)
	cpu.PC += 1
	# TODO: Implement it
	pass
	return 4

def LD_77(cpu):
	# LD (HL),A	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.memory.write_byte(cpu.HL, cpu.A & 0xFF)
	return 8

def LD_78(cpu):
	# LD A,B	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = cpu.B
	return 4

def LD_79(cpu):
	# LD A,C	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = cpu.C
	return 4

def LD_7A(cpu):
	# LD A,D	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = cpu.D
	return 4

def LD_7B(cpu):
	# LD A,E	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = cpu.E
	return 4

def LD_7C(cpu):
	# LD A,H	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = (cpu.HL >> 8)
	return 4

def LD_7D(cpu):
	# LD A,L	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = (cpu.HL & 0x00FF)
	return 4

def LD_7E(cpu):
	# LD A,(HL)	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = cpu.memory.read_byte(cpu.HL)
	return 8

def LD_7F(cpu):
	# LD A,A	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = cpu.A
	return 4

def ADD_80(cpu):
	# ADD A,B	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + cpu.B
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (cpu.B & 0x0F)) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def ADD_81(cpu):
	# ADD A,C	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + cpu.C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (cpu.C & 0x0F)) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def ADD_82(cpu):
	# ADD A,D	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + cpu.D
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (cpu.D & 0x0F)) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def ADD_83(cpu):
	# ADD A,E	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + cpu.E
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (cpu.E & 0x0F)) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def ADD_84(cpu):
	# ADD A,H	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + (cpu.HL >> 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + ((cpu.HL >> 8) & 0x0F)) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def ADD_85(cpu):
	# ADD A,L	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + (cpu.HL & 0x00FF)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + ((cpu.HL & 0x00FF) & 0x0F)) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def ADD_86(cpu):
	# ADD A,(HL)	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + cpu.memory.read_byte(cpu.HL)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (cpu.memory.read_byte(cpu.HL) & 0x0F)) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 8

def ADD_87(cpu):
	# ADD A,A	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + cpu.A
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (cpu.A & 0x0F)) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def ADC_88(cpu):
	# ADC A,B	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + cpu.B + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (cpu.B & 0x0F) + cpu.FLAG_C) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def ADC_89(cpu):
	# ADC A,C	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + cpu.C + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (cpu.C & 0x0F) + cpu.FLAG_C) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def ADC_8A(cpu):
	# ADC A,D	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + cpu.D + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (cpu.D & 0x0F) + cpu.FLAG_C) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def ADC_8B(cpu):
	# ADC A,E	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + cpu.E + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (cpu.E & 0x0F) + cpu.FLAG_C) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def ADC_8C(cpu):
	# ADC A,H	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + (cpu.HL >> 8) + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + ((cpu.HL >> 8) & 0x0F) + cpu.FLAG_C) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def ADC_8D(cpu):
	# ADC A,L	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + (cpu.HL & 0x00FF) + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + ((cpu.HL & 0x00FF) & 0x0F) + cpu.FLAG_C) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def ADC_8E(cpu):
	# ADC A,(HL)	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + cpu.memory.read_byte(cpu.HL) + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (cpu.memory.read_byte(cpu.HL) & 0x0F) + cpu.FLAG_C) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 8

def ADC_8F(cpu):
	# ADC A,A	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A + cpu.A + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (cpu.A & 0x0F) + cpu.FLAG_C) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 4

def SUB_90(cpu):
	# SUB B	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.B
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.B & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def SUB_91(cpu):
	# SUB C	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.C & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def SUB_92(cpu):
	# SUB D	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.D
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.D & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def SUB_93(cpu):
	# SUB E	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.E
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.E & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def SUB_94(cpu):
	# SUB H	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - (cpu.HL >> 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - ((cpu.HL >> 8) & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def SUB_95(cpu):
	# SUB L	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - (cpu.HL & 0x00FF)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - ((cpu.HL & 0x00FF) & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def SUB_96(cpu):
	# SUB (HL)	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.memory.read_byte(cpu.HL)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.memory.read_byte(cpu.HL) & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 8

def SUB_97(cpu):
	# SUB A	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.A
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.A & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def SBC_98(cpu):
	# SBC A,B	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.B - cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.B & 0x0F) - cpu.FLAG_C) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def SBC_99(cpu):
	# SBC A,C	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.C - cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.C & 0x0F) - cpu.FLAG_C) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def SBC_9A(cpu):
	# SBC A,D	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.D - cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.D & 0x0F) - cpu.FLAG_C) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def SBC_9B(cpu):
	# SBC A,E	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.E - cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.E & 0x0F) - cpu.FLAG_C) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def SBC_9C(cpu):
	# SBC A,H	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - (cpu.HL >> 8) - cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - ((cpu.HL >> 8) & 0x0F) - cpu.FLAG_C) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def SBC_9D(cpu):
	# SBC A,L	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - (cpu.HL & 0x00FF) - cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - ((cpu.HL & 0x00FF) & 0x0F) - cpu.FLAG_C) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def SBC_9E(cpu):
	# SBC A,(HL)	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.memory.read_byte(cpu.HL) - cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.memory.read_byte(cpu.HL) & 0x0F) - cpu.FLAG_C) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 8

def SBC_9F(cpu):
	# SBC A,A	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.A - cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.A & 0x0F) - cpu.FLAG_C) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 4

def AND_A0(cpu):
	# AND B	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A & cpu.B
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def AND_A1(cpu):
	# AND C	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A & cpu.C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def AND_A2(cpu):
	# AND D	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A & cpu.D
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def AND_A3(cpu):
	# AND E	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A & cpu.E
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def AND_A4(cpu):
	# AND H	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A & (cpu.HL >> 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def AND_A5(cpu):
	# AND L	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A & (cpu.HL & 0x00FF)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def AND_A6(cpu):
	# AND (HL)	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A & cpu.memory.read_byte(cpu.HL)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 8

def AND_A7(cpu):
	# AND A	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A & cpu.A
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def XOR_A8(cpu):
	# XOR B	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A ^ cpu.B
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def XOR_A9(cpu):
	# XOR C	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A ^ cpu.C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def XOR_AA(cpu):
	# XOR D	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A ^ cpu.D
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def XOR_AB(cpu):
	# XOR E	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A ^ cpu.E
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def XOR_AC(cpu):
	# XOR H	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A ^ (cpu.HL >> 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def XOR_AD(cpu):
	# XOR L	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A ^ (cpu.HL & 0x00FF)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def XOR_AE(cpu):
	# XOR (HL)	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A ^ cpu.memory.read_byte(cpu.HL)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 8

def XOR_AF(cpu):
	# XOR A	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A ^ cpu.A
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def OR_B0(cpu):
	# OR B	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A | cpu.B
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def OR_B1(cpu):
	# OR C	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A | cpu.C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def OR_B2(cpu):
	# OR D	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A | cpu.D
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def OR_B3(cpu):
	# OR E	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A | cpu.E
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def OR_B4(cpu):
	# OR H	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A | (cpu.HL >> 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def OR_B5(cpu):
	# OR L	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A | (cpu.HL & 0x00FF)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def OR_B6(cpu):
	# OR (HL)	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A | cpu.memory.read_byte(cpu.HL)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 8

def OR_B7(cpu):
	# OR A	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A | cpu.A
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 4

def CP_B8(cpu):
	# CP B	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.B
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.B & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	return 4

def CP_B9(cpu):
	# CP C	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.C & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	return 4

def CP_BA(cpu):
	# CP D	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.D
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.D & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	return 4

def CP_BB(cpu):
	# CP E	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.E
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.E & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	return 4

def CP_BC(cpu):
	# CP H	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - (cpu.HL >> 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - ((cpu.HL >> 8) & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	return 4

def CP_BD(cpu):
	# CP L	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - (cpu.HL & 0x00FF)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - ((cpu.HL & 0x00FF) & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	return 4

def CP_BE(cpu):
	# CP (HL)	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.memory.read_byte(cpu.HL)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.memory.read_byte(cpu.HL) & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	return 8

def CP_BF(cpu):
	# CP A	(8bit arithmetic/logical instructions)
	cpu.PC += 1
	t = cpu.A - cpu.A
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (cpu.A & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	return 4

def RET_C0(cpu):
	# RET NZ	(Jumps/calls)
	cpu.PC += 1
	if not cpu.FLAG_Z:
		cpu.PC = (cpu.memory.read_byte(cpu.SP + 1) << 8) | cpu.memory.read_byte(cpu.SP)
		cpu.SP += 2
		return 20
	else:
		return 8

def POP_C1(cpu):
	# POP BC	(16bit load/store/move instructions)
	cpu.PC += 1
	cpu.B = cpu.memory.read_byte(cpu.SP + 1)
	cpu.C = cpu.memory.read_byte(cpu.SP)
	cpu.SP += 2
	return 12

def JP_C2(cpu, v):
	# JP NZ,a16	(Jumps/calls)
	cpu.PC += 3
	if not cpu.FLAG_Z:
		cpu.PC = v
		return 16
	else:
		return 12

def JP_C3(cpu, v):
	# JP a16	(Jumps/calls)
	cpu.PC += 3
	cpu.PC = v
	return 16

def CALL_C4(cpu, v):
	# CALL NZ,a16	(Jumps/calls)
	cpu.PC += 3
	if not cpu.FLAG_Z:
		cpu.SP -= 2
		cpu.memory.write_byte(cpu.SP + 1, cpu.PC >> 8)
		cpu.memory.write_byte(cpu.SP, cpu.PC & 0xFF)
		cpu.PC = v
		return 24
	else:
		return 12

def PUSH_C5(cpu):
	# PUSH BC	(16bit load/store/move instructions)
	cpu.PC += 1
	cpu.SP -= 2
	cpu.memory.write_byte(cpu.SP + 1, cpu.B)
	cpu.memory.write_byte(cpu.SP, cpu.C)
	return 16

def ADD_C6(cpu, v):
	# ADD A,d8	(8bit arithmetic/logical instructions)
	cpu.PC += 2
	t = cpu.A + v
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (v & 0x0F)) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 8

def RST_C7(cpu):
	# RST 00H	(Jumps/calls)
	cpu.PC += 1
	cpu.SP -= 2
	cpu.memory.write_byte(cpu.SP + 1, cpu.PC >> 8)
	cpu.memory.write_byte(cpu.SP, cpu.PC & 0xFF)
	cpu.PC = 0
	return 16

def RET_C8(cpu):
	# RET Z	(Jumps/calls)
	cpu.PC += 1
	if cpu.FLAG_Z:
		cpu.PC = (cpu.memory.read_byte(cpu.SP + 1) << 8) | cpu.memory.read_byte(cpu.SP)
		cpu.SP += 2
		return 20
	else:
		return 8

def RET_C9(cpu):
	# RET	(Jumps/calls)
	cpu.PC += 1
	cpu.PC = (cpu.memory.read_byte(cpu.SP + 1) << 8) | cpu.memory.read_byte(cpu.SP)
	cpu.SP += 2
	return 16

def JP_CA(cpu, v):
	# JP Z,a16	(Jumps/calls)
	cpu.PC += 3
	if cpu.FLAG_Z:
		cpu.PC = v
		return 16
	else:
		return 12

def PREFIX_CB(cpu, v):
	# PREFIX CB	(Misc/control instructions)
	cpu.PC += 2
	raise Exception("Not Used")
	return 8

def CALL_CC(cpu, v):
	# CALL Z,a16	(Jumps/calls)
	cpu.PC += 3
	if cpu.FLAG_Z:
		cpu.SP -= 2
		cpu.memory.write_byte(cpu.SP + 1, cpu.PC >> 8)
		cpu.memory.write_byte(cpu.SP, cpu.PC & 0xFF)
		cpu.PC = v
		return 24
	else:
		return 12

def CALL_CD(cpu, v):
	# CALL a16	(Jumps/calls)
	cpu.PC += 3
	cpu.SP -= 2
	cpu.memory.write_byte(cpu.SP + 1, cpu.PC >> 8)
	cpu.memory.write_byte(cpu.SP, cpu.PC & 0xFF)
	cpu.PC = v
	return 24

def ADC_CE(cpu, v):
	# ADC A,d8	(8bit arithmetic/logical instructions)
	cpu.PC += 2
	t = cpu.A + v + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.A & 0x0F) + (v & 0x0F) + cpu.FLAG_C) > 0x0F
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 8

def RST_CF(cpu):
	# RST 08H	(Jumps/calls)
	cpu.PC += 1
	cpu.SP -= 2
	cpu.memory.write_byte(cpu.SP + 1, cpu.PC >> 8)
	cpu.memory.write_byte(cpu.SP, cpu.PC & 0xFF)
	cpu.PC = 8
	return 16

def RET_D0(cpu):
	# RET NC	(Jumps/calls)
	cpu.PC += 1
	if not cpu.FLAG_C:
		cpu.PC = (cpu.memory.read_byte(cpu.SP + 1) << 8) | cpu.memory.read_byte(cpu.SP)
		cpu.SP += 2
		return 20
	else:
		return 8

def POP_D1(cpu):
	# POP DE	(16bit load/store/move instructions)
	cpu.PC += 1
	cpu.D = cpu.memory.read_byte(cpu.SP + 1)
	cpu.E = cpu.memory.read_byte(cpu.SP)
	cpu.SP += 2
	return 12

def JP_D2(cpu, v):
	# JP NC,a16	(Jumps/calls)
	cpu.PC += 3
	if not cpu.FLAG_C:
		cpu.PC = v
		return 16
	else:
		return 12

def CALL_D4(cpu, v):
	# CALL NC,a16	(Jumps/calls)
	cpu.PC += 3
	if not cpu.FLAG_C:
		cpu.SP -= 2
		cpu.memory.write_byte(cpu.SP + 1, cpu.PC >> 8)
		cpu.memory.write_byte(cpu.SP, cpu.PC & 0xFF)
		cpu.PC = v
		return 24
	else:
		return 12

def PUSH_D5(cpu):
	# PUSH DE	(16bit load/store/move instructions)
	cpu.PC += 1
	cpu.SP -= 2
	cpu.memory.write_byte(cpu.SP + 1, cpu.D)
	cpu.memory.write_byte(cpu.SP, cpu.E)
	return 16

def SUB_D6(cpu, v):
	# SUB d8	(8bit arithmetic/logical instructions)
	cpu.PC += 2
	t = cpu.A - v
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (v & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 8

def RST_D7(cpu):
	# RST 10H	(Jumps/calls)
	cpu.PC += 1
	cpu.SP -= 2
	cpu.memory.write_byte(cpu.SP + 1, cpu.PC >> 8)
	cpu.memory.write_byte(cpu.SP, cpu.PC & 0xFF)
	cpu.PC = 16
	return 16

def RET_D8(cpu):
	# RET C	(Jumps/calls)
	cpu.PC += 1
	if cpu.FLAG_C:
		cpu.PC = (cpu.memory.read_byte(cpu.SP + 1) << 8) | cpu.memory.read_byte(cpu.SP)
		cpu.SP += 2
		return 20
	else:
		return 8

def RETI_D9(cpu):
	# RETI	(Jumps/calls)
	cpu.PC += 1
	cpu.ime = True
	cpu.PC = (cpu.memory.read_byte(cpu.SP + 1) << 8) | cpu.memory.read_byte(cpu.SP)
	cpu.SP += 2
	return 16

def JP_DA(cpu, v):
	# JP C,a16	(Jumps/calls)
	cpu.PC += 3
	if cpu.FLAG_C:
		cpu.PC = v
		return 16
	else:
		return 12

def CALL_DC(cpu, v):
	# CALL C,a16	(Jumps/calls)
	cpu.PC += 3
	if cpu.FLAG_C:
		cpu.SP -= 2
		cpu.memory.write_byte(cpu.SP + 1, cpu.PC >> 8)
		cpu.memory.write_byte(cpu.SP, cpu.PC & 0xFF)
		cpu.PC = v
		return 24
	else:
		return 12

def SBC_DE(cpu, v):
	# SBC A,d8	(8bit arithmetic/logical instructions)
	cpu.PC += 2
	t = cpu.A - v - cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (v & 0x0F) - cpu.FLAG_C) < 0
	cpu.FLAG_C = t < 0
	t &= 0xFF
	cpu.A = t
	return 8

def RST_DF(cpu):
	# RST 18H	(Jumps/calls)
	cpu.PC += 1
	cpu.SP -= 2
	cpu.memory.write_byte(cpu.SP + 1, cpu.PC >> 8)
	cpu.memory.write_byte(cpu.SP, cpu.PC & 0xFF)
	cpu.PC = 24
	return 16

def LDH_E0(cpu, v):
	# LDH (a8),A	(8bit load/store/move instructions)
	cpu.PC += 2
	cpu.memory.write_byte(0xFF00 + v, cpu.A & 0xFF)
	return 12

def POP_E1(cpu):
	# POP HL	(16bit load/store/move instructions)
	cpu.PC += 1
	cpu.HL = (cpu.HL & 0x00FF) | (cpu.memory.read_byte(cpu.SP + 1) << 8)
	cpu.HL = (cpu.HL & 0xFF00) | (cpu.memory.read_byte(cpu.SP) & 0xFF)
	cpu.SP += 2
	return 12

def LD_E2(cpu):
	# LD (C),A	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.memory.write_byte(0xFF00 + cpu.C, cpu.A & 0xFF)
	return 8

def PUSH_E5(cpu):
	# PUSH HL	(16bit load/store/move instructions)
	cpu.PC += 1
	cpu.SP -= 2
	cpu.memory.write_byte(cpu.SP + 1, (cpu.HL >> 8))
	cpu.memory.write_byte(cpu.SP, (cpu.HL & 0x00FF))
	return 16

def AND_E6(cpu, v):
	# AND d8	(8bit arithmetic/logical instructions)
	cpu.PC += 2
	t = cpu.A & v
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 8

def RST_E7(cpu):
	# RST 20H	(Jumps/calls)
	cpu.PC += 1
	cpu.SP -= 2
	cpu.memory.write_byte(cpu.SP + 1, cpu.PC >> 8)
	cpu.memory.write_byte(cpu.SP, cpu.PC & 0xFF)
	cpu.PC = 32
	return 16

def ADD_E8(cpu, v):
	# ADD SP,r8	(16bit arithmetic/logical instructions)
	cpu.PC += 2
	t = cpu.SP + ((v ^ 0x80) - 0x80)
	cpu.FLAG_Z = 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.SP & 0x0F) + (v & 0x0F)) > 0xF
	cpu.FLAG_C = ((cpu.SP & 0xFF) + v) > 0xFF
	t &= 0xFFFF
	cpu.SP = t
	return 16

def JP_E9(cpu):
	# JP HL	(Jumps/calls)
	cpu.PC += 1
	cpu.PC = cpu.HL
	return 4

def LD_EA(cpu, v):
	# LD (a16),A	(8bit load/store/move instructions)
	cpu.PC += 3
	cpu.memory.write_byte(v, cpu.A)
	return 16

def XOR_EE(cpu, v):
	# XOR d8	(8bit arithmetic/logical instructions)
	cpu.PC += 2
	t = cpu.A ^ v
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 8

def RST_EF(cpu):
	# RST 28H	(Jumps/calls)
	cpu.PC += 1
	cpu.SP -= 2
	cpu.memory.write_byte(cpu.SP + 1, cpu.PC >> 8)
	cpu.memory.write_byte(cpu.SP, cpu.PC & 0xFF)
	cpu.PC = 40
	return 16

def LDH_F0(cpu, v):
	# LDH A,(a8)	(8bit load/store/move instructions)
	cpu.PC += 2
	cpu.A = cpu.memory.read_byte(0xFF00 + v)
	return 12

def POP_F1(cpu):
	# POP AF	(16bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = cpu.memory.read_byte(cpu.SP + 1)
	cpu.FLAG_Z = (cpu.memory.read_byte(cpu.SP) >> 7) & 0b1
	cpu.FLAG_N = (cpu.memory.read_byte(cpu.SP) >> 6) & 0b1
	cpu.FLAG_H = (cpu.memory.read_byte(cpu.SP) >> 5) & 0b1
	cpu.FLAG_C = (cpu.memory.read_byte(cpu.SP) >> 4) & 0b1
	cpu.SP += 2
	return 12

def LD_F2(cpu):
	# LD A,(C)	(8bit load/store/move instructions)
	cpu.PC += 1
	cpu.A = cpu.memory.read_byte(0xFF00 + cpu.C)
	return 8

def DI_F3(cpu):
	# DI	(Misc/control instructions)
	cpu.PC += 1
	# Disable Interrupts
	cpu.ime = False
	return 4

def PUSH_F5(cpu):
	# PUSH AF	(16bit load/store/move instructions)
	cpu.PC += 1
	cpu.SP -= 2
	cpu.memory.write_byte(cpu.SP + 1, cpu.A)
	cpu.memory.write_byte(cpu.SP, ((cpu.FLAG_Z << 7) + (cpu.FLAG_N << 6) + (cpu.FLAG_H << 5) + (cpu.FLAG_C << 4)))
	return 16

def OR_F6(cpu, v):
	# OR d8	(8bit arithmetic/logical instructions)
	cpu.PC += 2
	t = cpu.A | v
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 8

def RST_F7(cpu):
	# RST 30H	(Jumps/calls)
	cpu.PC += 1
	cpu.SP -= 2
	cpu.memory.write_byte(cpu.SP + 1, cpu.PC >> 8)
	cpu.memory.write_byte(cpu.SP, cpu.PC & 0xFF)
	cpu.PC = 48
	return 16

def LD_F8(cpu, v):
	# LD HL,SP+r8	(16bit load/store/move instructions)
	cpu.PC += 2
	cpu.HL = ((cpu.SP + ((v ^ 0x80) - 0x80)) & 0xFFFF)
	cpu.FLAG_Z = 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = ((cpu.SP & 0x0F) + (v & 0x0F)) > 0xF
	cpu.FLAG_C = ((cpu.SP & 0xFF) + v) > 0xFF
	return 12

def LD_F9(cpu):
	# LD SP,HL	(16bit load/store/move instructions)
	cpu.PC += 1
	cpu.SP = cpu.HL
	return 8

def LD_FA(cpu, v):
	# LD A,(a16)	(8bit load/store/move instructions)
	cpu.PC += 3
	cpu.A = cpu.memory.read_byte(v)
	return 16

def EI_FB(cpu):
	# EI	(Misc/control instructions)
	cpu.PC += 1
	# Enable Interrupts
	cpu.ime = True
	return 4

def CP_FE(cpu, v):
	# CP d8	(8bit arithmetic/logical instructions)
	cpu.PC += 2
	t = cpu.A - v
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 1
	cpu.FLAG_H = ((cpu.A & 0x0F) - (v & 0x0F)) < 0
	cpu.FLAG_C = t < 0
	return 8

def RST_FF(cpu):
	# RST 38H	(Jumps/calls)
	cpu.PC += 1
	cpu.SP -= 2
	cpu.memory.write_byte(cpu.SP + 1, cpu.PC >> 8)
	cpu.memory.write_byte(cpu.SP, cpu.PC & 0xFF)
	cpu.PC = 56
	return 16

def RLC_CB00(cpu):
	# RLC B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.B << 1) + (cpu.B >> 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.B = t
	return 8

def RLC_CB01(cpu):
	# RLC C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.C << 1) + (cpu.C >> 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.C = t
	return 8

def RLC_CB02(cpu):
	# RLC D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.D << 1) + (cpu.D >> 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.D = t
	return 8

def RLC_CB03(cpu):
	# RLC E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.E << 1) + (cpu.E >> 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.E = t
	return 8

def RLC_CB04(cpu):
	# RLC H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL >> 8) << 1) + ((cpu.HL >> 8) >> 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def RLC_CB05(cpu):
	# RLC L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL & 0x00FF) << 1) + ((cpu.HL & 0x00FF) >> 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def RLC_CB06(cpu):
	# RLC (HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.memory.read_byte(cpu.HL) << 1) + (cpu.memory.read_byte(cpu.HL) >> 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def RLC_CB07(cpu):
	# RLC A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.A << 1) + (cpu.A >> 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 8

def RRC_CB08(cpu):
	# RRC B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.B >> 1) + ((cpu.B & 1) << 7) + ((cpu.B & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.B = t
	return 8

def RRC_CB09(cpu):
	# RRC C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.C >> 1) + ((cpu.C & 1) << 7) + ((cpu.C & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.C = t
	return 8

def RRC_CB0A(cpu):
	# RRC D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.D >> 1) + ((cpu.D & 1) << 7) + ((cpu.D & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.D = t
	return 8

def RRC_CB0B(cpu):
	# RRC E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.E >> 1) + ((cpu.E & 1) << 7) + ((cpu.E & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.E = t
	return 8

def RRC_CB0C(cpu):
	# RRC H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL >> 8) >> 1) + (((cpu.HL >> 8) & 1) << 7) + (((cpu.HL >> 8) & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def RRC_CB0D(cpu):
	# RRC L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL & 0x00FF) >> 1) + (((cpu.HL & 0x00FF) & 1) << 7) + (((cpu.HL & 0x00FF) & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def RRC_CB0E(cpu):
	# RRC (HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.memory.read_byte(cpu.HL) >> 1) + ((cpu.memory.read_byte(cpu.HL) & 1) << 7) + ((cpu.memory.read_byte(cpu.HL) & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def RRC_CB0F(cpu):
	# RRC A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.A >> 1) + ((cpu.A & 1) << 7) + ((cpu.A & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 8

def RL_CB10(cpu):
	# RL B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.B << 1) + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.B = t
	return 8

def RL_CB11(cpu):
	# RL C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.C << 1) + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.C = t
	return 8

def RL_CB12(cpu):
	# RL D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.D << 1) + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.D = t
	return 8

def RL_CB13(cpu):
	# RL E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.E << 1) + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.E = t
	return 8

def RL_CB14(cpu):
	# RL H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL >> 8) << 1) + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def RL_CB15(cpu):
	# RL L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL & 0x00FF) << 1) + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def RL_CB16(cpu):
	# RL (HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.memory.read_byte(cpu.HL) << 1) + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def RL_CB17(cpu):
	# RL A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.A << 1) + cpu.FLAG_C
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 8

def RR_CB18(cpu):
	# RR B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.B >> 1) + (cpu.FLAG_C << 7) + ((cpu.B & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.B = t
	return 8

def RR_CB19(cpu):
	# RR C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.C >> 1) + (cpu.FLAG_C << 7) + ((cpu.C & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.C = t
	return 8

def RR_CB1A(cpu):
	# RR D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.D >> 1) + (cpu.FLAG_C << 7) + ((cpu.D & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.D = t
	return 8

def RR_CB1B(cpu):
	# RR E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.E >> 1) + (cpu.FLAG_C << 7) + ((cpu.E & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.E = t
	return 8

def RR_CB1C(cpu):
	# RR H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL >> 8) >> 1) + (cpu.FLAG_C << 7) + (((cpu.HL >> 8) & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def RR_CB1D(cpu):
	# RR L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL & 0x00FF) >> 1) + (cpu.FLAG_C << 7) + (((cpu.HL & 0x00FF) & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def RR_CB1E(cpu):
	# RR (HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.memory.read_byte(cpu.HL) >> 1) + (cpu.FLAG_C << 7) + ((cpu.memory.read_byte(cpu.HL) & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def RR_CB1F(cpu):
	# RR A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.A >> 1) + (cpu.FLAG_C << 7) + ((cpu.A & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 8

def SLA_CB20(cpu):
	# SLA B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.B << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.B = t
	return 8

def SLA_CB21(cpu):
	# SLA C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.C << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.C = t
	return 8

def SLA_CB22(cpu):
	# SLA D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.D << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.D = t
	return 8

def SLA_CB23(cpu):
	# SLA E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.E << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.E = t
	return 8

def SLA_CB24(cpu):
	# SLA H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL >> 8) << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def SLA_CB25(cpu):
	# SLA L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL & 0x00FF) << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def SLA_CB26(cpu):
	# SLA (HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.memory.read_byte(cpu.HL) << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def SLA_CB27(cpu):
	# SLA A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.A << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 8

def SRA_CB28(cpu):
	# SRA B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.B >> 1) + (cpu.B & 0x80) + ((cpu.B & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.B = t
	return 8

def SRA_CB29(cpu):
	# SRA C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.C >> 1) + (cpu.C & 0x80) + ((cpu.C & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.C = t
	return 8

def SRA_CB2A(cpu):
	# SRA D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.D >> 1) + (cpu.D & 0x80) + ((cpu.D & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.D = t
	return 8

def SRA_CB2B(cpu):
	# SRA E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.E >> 1) + (cpu.E & 0x80) + ((cpu.E & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.E = t
	return 8

def SRA_CB2C(cpu):
	# SRA H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL >> 8) >> 1) + ((cpu.HL >> 8) & 0x80) + (((cpu.HL >> 8) & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def SRA_CB2D(cpu):
	# SRA L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL & 0x00FF) >> 1) + ((cpu.HL & 0x00FF) & 0x80) + (((cpu.HL & 0x00FF) & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def SRA_CB2E(cpu):
	# SRA (HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.memory.read_byte(cpu.HL) >> 1) + (cpu.memory.read_byte(cpu.HL) & 0x80) + ((cpu.memory.read_byte(cpu.HL) & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def SRA_CB2F(cpu):
	# SRA A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.A >> 1) + (cpu.A & 0x80) + ((cpu.A & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 8

def SWAP_CB30(cpu):
	# SWAP B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.B & 0x0F) << 4) | ((cpu.B & 0xF0) >> 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.B = t
	return 8

def SWAP_CB31(cpu):
	# SWAP C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.C & 0x0F) << 4) | ((cpu.C & 0xF0) >> 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.C = t
	return 8

def SWAP_CB32(cpu):
	# SWAP D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.D & 0x0F) << 4) | ((cpu.D & 0xF0) >> 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.D = t
	return 8

def SWAP_CB33(cpu):
	# SWAP E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.E & 0x0F) << 4) | ((cpu.E & 0xF0) >> 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.E = t
	return 8

def SWAP_CB34(cpu):
	# SWAP H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (((cpu.HL >> 8) & 0x0F) << 4) | (((cpu.HL >> 8) & 0xF0) >> 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def SWAP_CB35(cpu):
	# SWAP L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (((cpu.HL & 0x00FF) & 0x0F) << 4) | (((cpu.HL & 0x00FF) & 0xF0) >> 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def SWAP_CB36(cpu):
	# SWAP (HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.memory.read_byte(cpu.HL) & 0x0F) << 4) | ((cpu.memory.read_byte(cpu.HL) & 0xF0) >> 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def SWAP_CB37(cpu):
	# SWAP A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.A & 0x0F) << 4) | ((cpu.A & 0xF0) >> 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = 0
	t &= 0xFF
	cpu.A = t
	return 8

def SRL_CB38(cpu):
	# SRL B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.B >> 1)  + ((cpu.B & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.B = t
	return 8

def SRL_CB39(cpu):
	# SRL C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.C >> 1)  + ((cpu.C & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.C = t
	return 8

def SRL_CB3A(cpu):
	# SRL D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.D >> 1)  + ((cpu.D & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.D = t
	return 8

def SRL_CB3B(cpu):
	# SRL E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.E >> 1)  + ((cpu.E & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.E = t
	return 8

def SRL_CB3C(cpu):
	# SRL H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL >> 8) >> 1)  + (((cpu.HL >> 8) & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def SRL_CB3D(cpu):
	# SRL L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = ((cpu.HL & 0x00FF) >> 1)  + (((cpu.HL & 0x00FF) & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def SRL_CB3E(cpu):
	# SRL (HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.memory.read_byte(cpu.HL) >> 1)  + ((cpu.memory.read_byte(cpu.HL) & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def SRL_CB3F(cpu):
	# SRL A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.A >> 1)  + ((cpu.A & 1) << 8)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 0
	cpu.FLAG_C = t > 0xFF
	t &= 0xFF
	cpu.A = t
	return 8

def BIT_CB40(cpu):
	# BIT 0,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & (1 << 0)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB41(cpu):
	# BIT 0,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & (1 << 0)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB42(cpu):
	# BIT 0,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & (1 << 0)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB43(cpu):
	# BIT 0,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & (1 << 0)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB44(cpu):
	# BIT 0,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & (1 << 0)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB45(cpu):
	# BIT 0,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & (1 << 0)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB46(cpu):
	# BIT 0,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & (1 << 0)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 16

def BIT_CB47(cpu):
	# BIT 0,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & (1 << 0)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB48(cpu):
	# BIT 1,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & (1 << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB49(cpu):
	# BIT 1,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & (1 << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB4A(cpu):
	# BIT 1,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & (1 << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB4B(cpu):
	# BIT 1,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & (1 << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB4C(cpu):
	# BIT 1,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & (1 << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB4D(cpu):
	# BIT 1,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & (1 << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB4E(cpu):
	# BIT 1,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & (1 << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 16

def BIT_CB4F(cpu):
	# BIT 1,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & (1 << 1)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB50(cpu):
	# BIT 2,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & (1 << 2)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB51(cpu):
	# BIT 2,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & (1 << 2)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB52(cpu):
	# BIT 2,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & (1 << 2)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB53(cpu):
	# BIT 2,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & (1 << 2)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB54(cpu):
	# BIT 2,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & (1 << 2)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB55(cpu):
	# BIT 2,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & (1 << 2)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB56(cpu):
	# BIT 2,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & (1 << 2)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 16

def BIT_CB57(cpu):
	# BIT 2,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & (1 << 2)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB58(cpu):
	# BIT 3,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & (1 << 3)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB59(cpu):
	# BIT 3,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & (1 << 3)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB5A(cpu):
	# BIT 3,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & (1 << 3)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB5B(cpu):
	# BIT 3,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & (1 << 3)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB5C(cpu):
	# BIT 3,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & (1 << 3)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB5D(cpu):
	# BIT 3,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & (1 << 3)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB5E(cpu):
	# BIT 3,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & (1 << 3)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 16

def BIT_CB5F(cpu):
	# BIT 3,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & (1 << 3)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB60(cpu):
	# BIT 4,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & (1 << 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB61(cpu):
	# BIT 4,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & (1 << 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB62(cpu):
	# BIT 4,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & (1 << 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB63(cpu):
	# BIT 4,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & (1 << 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB64(cpu):
	# BIT 4,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & (1 << 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB65(cpu):
	# BIT 4,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & (1 << 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB66(cpu):
	# BIT 4,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & (1 << 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 16

def BIT_CB67(cpu):
	# BIT 4,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & (1 << 4)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB68(cpu):
	# BIT 5,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & (1 << 5)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB69(cpu):
	# BIT 5,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & (1 << 5)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB6A(cpu):
	# BIT 5,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & (1 << 5)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB6B(cpu):
	# BIT 5,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & (1 << 5)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB6C(cpu):
	# BIT 5,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & (1 << 5)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB6D(cpu):
	# BIT 5,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & (1 << 5)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB6E(cpu):
	# BIT 5,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & (1 << 5)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 16

def BIT_CB6F(cpu):
	# BIT 5,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & (1 << 5)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB70(cpu):
	# BIT 6,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & (1 << 6)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB71(cpu):
	# BIT 6,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & (1 << 6)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB72(cpu):
	# BIT 6,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & (1 << 6)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB73(cpu):
	# BIT 6,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & (1 << 6)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB74(cpu):
	# BIT 6,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & (1 << 6)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB75(cpu):
	# BIT 6,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & (1 << 6)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB76(cpu):
	# BIT 6,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & (1 << 6)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 16

def BIT_CB77(cpu):
	# BIT 6,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & (1 << 6)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB78(cpu):
	# BIT 7,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & (1 << 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB79(cpu):
	# BIT 7,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & (1 << 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB7A(cpu):
	# BIT 7,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & (1 << 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB7B(cpu):
	# BIT 7,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & (1 << 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB7C(cpu):
	# BIT 7,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & (1 << 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB7D(cpu):
	# BIT 7,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & (1 << 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def BIT_CB7E(cpu):
	# BIT 7,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & (1 << 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 16

def BIT_CB7F(cpu):
	# BIT 7,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & (1 << 7)
	cpu.FLAG_Z = t & 0xFF == 0
	cpu.FLAG_N = 0
	cpu.FLAG_H = 1
	return 8

def RES_CB80(cpu):
	# RES 0,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & ~(1 << 0)
	cpu.B = t
	return 8

def RES_CB81(cpu):
	# RES 0,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & ~(1 << 0)
	cpu.C = t
	return 8

def RES_CB82(cpu):
	# RES 0,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & ~(1 << 0)
	cpu.D = t
	return 8

def RES_CB83(cpu):
	# RES 0,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & ~(1 << 0)
	cpu.E = t
	return 8

def RES_CB84(cpu):
	# RES 0,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & ~(1 << 0)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def RES_CB85(cpu):
	# RES 0,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & ~(1 << 0)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def RES_CB86(cpu):
	# RES 0,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & ~(1 << 0)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def RES_CB87(cpu):
	# RES 0,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & ~(1 << 0)
	cpu.A = t
	return 8

def RES_CB88(cpu):
	# RES 1,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & ~(1 << 1)
	cpu.B = t
	return 8

def RES_CB89(cpu):
	# RES 1,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & ~(1 << 1)
	cpu.C = t
	return 8

def RES_CB8A(cpu):
	# RES 1,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & ~(1 << 1)
	cpu.D = t
	return 8

def RES_CB8B(cpu):
	# RES 1,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & ~(1 << 1)
	cpu.E = t
	return 8

def RES_CB8C(cpu):
	# RES 1,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & ~(1 << 1)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def RES_CB8D(cpu):
	# RES 1,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & ~(1 << 1)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def RES_CB8E(cpu):
	# RES 1,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & ~(1 << 1)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def RES_CB8F(cpu):
	# RES 1,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & ~(1 << 1)
	cpu.A = t
	return 8

def RES_CB90(cpu):
	# RES 2,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & ~(1 << 2)
	cpu.B = t
	return 8

def RES_CB91(cpu):
	# RES 2,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & ~(1 << 2)
	cpu.C = t
	return 8

def RES_CB92(cpu):
	# RES 2,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & ~(1 << 2)
	cpu.D = t
	return 8

def RES_CB93(cpu):
	# RES 2,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & ~(1 << 2)
	cpu.E = t
	return 8

def RES_CB94(cpu):
	# RES 2,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & ~(1 << 2)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def RES_CB95(cpu):
	# RES 2,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & ~(1 << 2)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def RES_CB96(cpu):
	# RES 2,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & ~(1 << 2)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def RES_CB97(cpu):
	# RES 2,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & ~(1 << 2)
	cpu.A = t
	return 8

def RES_CB98(cpu):
	# RES 3,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & ~(1 << 3)
	cpu.B = t
	return 8

def RES_CB99(cpu):
	# RES 3,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & ~(1 << 3)
	cpu.C = t
	return 8

def RES_CB9A(cpu):
	# RES 3,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & ~(1 << 3)
	cpu.D = t
	return 8

def RES_CB9B(cpu):
	# RES 3,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & ~(1 << 3)
	cpu.E = t
	return 8

def RES_CB9C(cpu):
	# RES 3,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & ~(1 << 3)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def RES_CB9D(cpu):
	# RES 3,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & ~(1 << 3)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def RES_CB9E(cpu):
	# RES 3,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & ~(1 << 3)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def RES_CB9F(cpu):
	# RES 3,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & ~(1 << 3)
	cpu.A = t
	return 8

def RES_CBA0(cpu):
	# RES 4,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & ~(1 << 4)
	cpu.B = t
	return 8

def RES_CBA1(cpu):
	# RES 4,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & ~(1 << 4)
	cpu.C = t
	return 8

def RES_CBA2(cpu):
	# RES 4,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & ~(1 << 4)
	cpu.D = t
	return 8

def RES_CBA3(cpu):
	# RES 4,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & ~(1 << 4)
	cpu.E = t
	return 8

def RES_CBA4(cpu):
	# RES 4,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & ~(1 << 4)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def RES_CBA5(cpu):
	# RES 4,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & ~(1 << 4)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def RES_CBA6(cpu):
	# RES 4,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & ~(1 << 4)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def RES_CBA7(cpu):
	# RES 4,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & ~(1 << 4)
	cpu.A = t
	return 8

def RES_CBA8(cpu):
	# RES 5,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & ~(1 << 5)
	cpu.B = t
	return 8

def RES_CBA9(cpu):
	# RES 5,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & ~(1 << 5)
	cpu.C = t
	return 8

def RES_CBAA(cpu):
	# RES 5,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & ~(1 << 5)
	cpu.D = t
	return 8

def RES_CBAB(cpu):
	# RES 5,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & ~(1 << 5)
	cpu.E = t
	return 8

def RES_CBAC(cpu):
	# RES 5,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & ~(1 << 5)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def RES_CBAD(cpu):
	# RES 5,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & ~(1 << 5)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def RES_CBAE(cpu):
	# RES 5,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & ~(1 << 5)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def RES_CBAF(cpu):
	# RES 5,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & ~(1 << 5)
	cpu.A = t
	return 8

def RES_CBB0(cpu):
	# RES 6,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & ~(1 << 6)
	cpu.B = t
	return 8

def RES_CBB1(cpu):
	# RES 6,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & ~(1 << 6)
	cpu.C = t
	return 8

def RES_CBB2(cpu):
	# RES 6,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & ~(1 << 6)
	cpu.D = t
	return 8

def RES_CBB3(cpu):
	# RES 6,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & ~(1 << 6)
	cpu.E = t
	return 8

def RES_CBB4(cpu):
	# RES 6,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & ~(1 << 6)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def RES_CBB5(cpu):
	# RES 6,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & ~(1 << 6)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def RES_CBB6(cpu):
	# RES 6,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & ~(1 << 6)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def RES_CBB7(cpu):
	# RES 6,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & ~(1 << 6)
	cpu.A = t
	return 8

def RES_CBB8(cpu):
	# RES 7,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B & ~(1 << 7)
	cpu.B = t
	return 8

def RES_CBB9(cpu):
	# RES 7,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C & ~(1 << 7)
	cpu.C = t
	return 8

def RES_CBBA(cpu):
	# RES 7,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D & ~(1 << 7)
	cpu.D = t
	return 8

def RES_CBBB(cpu):
	# RES 7,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E & ~(1 << 7)
	cpu.E = t
	return 8

def RES_CBBC(cpu):
	# RES 7,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) & ~(1 << 7)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def RES_CBBD(cpu):
	# RES 7,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) & ~(1 << 7)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def RES_CBBE(cpu):
	# RES 7,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) & ~(1 << 7)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def RES_CBBF(cpu):
	# RES 7,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A & ~(1 << 7)
	cpu.A = t
	return 8

def SET_CBC0(cpu):
	# SET 0,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B | (1 << 0)
	cpu.B = t
	return 8

def SET_CBC1(cpu):
	# SET 0,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C | (1 << 0)
	cpu.C = t
	return 8

def SET_CBC2(cpu):
	# SET 0,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D | (1 << 0)
	cpu.D = t
	return 8

def SET_CBC3(cpu):
	# SET 0,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E | (1 << 0)
	cpu.E = t
	return 8

def SET_CBC4(cpu):
	# SET 0,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) | (1 << 0)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def SET_CBC5(cpu):
	# SET 0,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) | (1 << 0)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def SET_CBC6(cpu):
	# SET 0,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) | (1 << 0)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def SET_CBC7(cpu):
	# SET 0,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A | (1 << 0)
	cpu.A = t
	return 8

def SET_CBC8(cpu):
	# SET 1,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B | (1 << 1)
	cpu.B = t
	return 8

def SET_CBC9(cpu):
	# SET 1,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C | (1 << 1)
	cpu.C = t
	return 8

def SET_CBCA(cpu):
	# SET 1,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D | (1 << 1)
	cpu.D = t
	return 8

def SET_CBCB(cpu):
	# SET 1,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E | (1 << 1)
	cpu.E = t
	return 8

def SET_CBCC(cpu):
	# SET 1,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) | (1 << 1)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def SET_CBCD(cpu):
	# SET 1,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) | (1 << 1)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def SET_CBCE(cpu):
	# SET 1,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) | (1 << 1)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def SET_CBCF(cpu):
	# SET 1,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A | (1 << 1)
	cpu.A = t
	return 8

def SET_CBD0(cpu):
	# SET 2,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B | (1 << 2)
	cpu.B = t
	return 8

def SET_CBD1(cpu):
	# SET 2,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C | (1 << 2)
	cpu.C = t
	return 8

def SET_CBD2(cpu):
	# SET 2,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D | (1 << 2)
	cpu.D = t
	return 8

def SET_CBD3(cpu):
	# SET 2,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E | (1 << 2)
	cpu.E = t
	return 8

def SET_CBD4(cpu):
	# SET 2,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) | (1 << 2)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def SET_CBD5(cpu):
	# SET 2,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) | (1 << 2)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def SET_CBD6(cpu):
	# SET 2,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) | (1 << 2)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def SET_CBD7(cpu):
	# SET 2,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A | (1 << 2)
	cpu.A = t
	return 8

def SET_CBD8(cpu):
	# SET 3,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B | (1 << 3)
	cpu.B = t
	return 8

def SET_CBD9(cpu):
	# SET 3,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C | (1 << 3)
	cpu.C = t
	return 8

def SET_CBDA(cpu):
	# SET 3,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D | (1 << 3)
	cpu.D = t
	return 8

def SET_CBDB(cpu):
	# SET 3,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E | (1 << 3)
	cpu.E = t
	return 8

def SET_CBDC(cpu):
	# SET 3,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) | (1 << 3)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def SET_CBDD(cpu):
	# SET 3,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) | (1 << 3)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def SET_CBDE(cpu):
	# SET 3,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) | (1 << 3)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def SET_CBDF(cpu):
	# SET 3,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A | (1 << 3)
	cpu.A = t
	return 8

def SET_CBE0(cpu):
	# SET 4,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B | (1 << 4)
	cpu.B = t
	return 8

def SET_CBE1(cpu):
	# SET 4,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C | (1 << 4)
	cpu.C = t
	return 8

def SET_CBE2(cpu):
	# SET 4,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D | (1 << 4)
	cpu.D = t
	return 8

def SET_CBE3(cpu):
	# SET 4,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E | (1 << 4)
	cpu.E = t
	return 8

def SET_CBE4(cpu):
	# SET 4,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) | (1 << 4)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def SET_CBE5(cpu):
	# SET 4,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) | (1 << 4)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def SET_CBE6(cpu):
	# SET 4,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) | (1 << 4)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def SET_CBE7(cpu):
	# SET 4,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A | (1 << 4)
	cpu.A = t
	return 8

def SET_CBE8(cpu):
	# SET 5,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B | (1 << 5)
	cpu.B = t
	return 8

def SET_CBE9(cpu):
	# SET 5,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C | (1 << 5)
	cpu.C = t
	return 8

def SET_CBEA(cpu):
	# SET 5,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D | (1 << 5)
	cpu.D = t
	return 8

def SET_CBEB(cpu):
	# SET 5,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E | (1 << 5)
	cpu.E = t
	return 8

def SET_CBEC(cpu):
	# SET 5,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) | (1 << 5)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def SET_CBED(cpu):
	# SET 5,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) | (1 << 5)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def SET_CBEE(cpu):
	# SET 5,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) | (1 << 5)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def SET_CBEF(cpu):
	# SET 5,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A | (1 << 5)
	cpu.A = t
	return 8

def SET_CBF0(cpu):
	# SET 6,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B | (1 << 6)
	cpu.B = t
	return 8

def SET_CBF1(cpu):
	# SET 6,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C | (1 << 6)
	cpu.C = t
	return 8

def SET_CBF2(cpu):
	# SET 6,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D | (1 << 6)
	cpu.D = t
	return 8

def SET_CBF3(cpu):
	# SET 6,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E | (1 << 6)
	cpu.E = t
	return 8

def SET_CBF4(cpu):
	# SET 6,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) | (1 << 6)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def SET_CBF5(cpu):
	# SET 6,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) | (1 << 6)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def SET_CBF6(cpu):
	# SET 6,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) | (1 << 6)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def SET_CBF7(cpu):
	# SET 6,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A | (1 << 6)
	cpu.A = t
	return 8

def SET_CBF8(cpu):
	# SET 7,B	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.B | (1 << 7)
	cpu.B = t
	return 8

def SET_CBF9(cpu):
	# SET 7,C	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.C | (1 << 7)
	cpu.C = t
	return 8

def SET_CBFA(cpu):
	# SET 7,D	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.D | (1 << 7)
	cpu.D = t
	return 8

def SET_CBFB(cpu):
	# SET 7,E	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.E | (1 << 7)
	cpu.E = t
	return 8

def SET_CBFC(cpu):
	# SET 7,H	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL >> 8) | (1 << 7)
	cpu.HL = (cpu.HL & 0x00FF) | (t << 8)
	return 8

def SET_CBFD(cpu):
	# SET 7,L	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = (cpu.HL & 0x00FF) | (1 << 7)
	cpu.HL = (cpu.HL & 0xFF00) | (t & 0xFF)
	return 8

def SET_CBFE(cpu):
	# SET 7,(HL)	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.memory.read_byte(cpu.HL) | (1 << 7)
	cpu.memory.write_byte(cpu.HL, t & 0xFF)
	return 16

def SET_CBFF(cpu):
	# SET 7,A	(8bit rotations/shifts and bit instructions)
	cpu.PC += 2
	t = cpu.A | (1 << 7)
	cpu.A = t
	return 8

def execute_opcode(cpu, opcode):
	if opcode == 0x00:
		return NOP_00(cpu)
	elif opcode == 0x01:
		return LD_01(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x02:
		return LD_02(cpu)
	elif opcode == 0x03:
		return INC_03(cpu)
	elif opcode == 0x04:
		return INC_04(cpu)
	elif opcode == 0x05:
		return DEC_05(cpu)
	elif opcode == 0x06:
		return LD_06(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x07:
		return RLCA_07(cpu)
	elif opcode == 0x08:
		return LD_08(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x09:
		return ADD_09(cpu)
	elif opcode == 0x0A:
		return LD_0A(cpu)
	elif opcode == 0x0B:
		return DEC_0B(cpu)
	elif opcode == 0x0C:
		return INC_0C(cpu)
	elif opcode == 0x0D:
		return DEC_0D(cpu)
	elif opcode == 0x0E:
		return LD_0E(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x0F:
		return RRCA_0F(cpu)
	elif opcode == 0x10:
		return STOP_10(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x11:
		return LD_11(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x12:
		return LD_12(cpu)
	elif opcode == 0x13:
		return INC_13(cpu)
	elif opcode == 0x14:
		return INC_14(cpu)
	elif opcode == 0x15:
		return DEC_15(cpu)
	elif opcode == 0x16:
		return LD_16(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x17:
		return RLA_17(cpu)
	elif opcode == 0x18:
		return JR_18(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x19:
		return ADD_19(cpu)
	elif opcode == 0x1A:
		return LD_1A(cpu)
	elif opcode == 0x1B:
		return DEC_1B(cpu)
	elif opcode == 0x1C:
		return INC_1C(cpu)
	elif opcode == 0x1D:
		return DEC_1D(cpu)
	elif opcode == 0x1E:
		return LD_1E(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x1F:
		return RRA_1F(cpu)
	elif opcode == 0x20:
		return JR_20(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x21:
		return LD_21(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x22:
		return LD_22(cpu)
	elif opcode == 0x23:
		return INC_23(cpu)
	elif opcode == 0x24:
		return INC_24(cpu)
	elif opcode == 0x25:
		return DEC_25(cpu)
	elif opcode == 0x26:
		return LD_26(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x27:
		return DAA_27(cpu)
	elif opcode == 0x28:
		return JR_28(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x29:
		return ADD_29(cpu)
	elif opcode == 0x2A:
		return LD_2A(cpu)
	elif opcode == 0x2B:
		return DEC_2B(cpu)
	elif opcode == 0x2C:
		return INC_2C(cpu)
	elif opcode == 0x2D:
		return DEC_2D(cpu)
	elif opcode == 0x2E:
		return LD_2E(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x2F:
		return CPL_2F(cpu)
	elif opcode == 0x30:
		return JR_30(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x31:
		return LD_31(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x32:
		return LD_32(cpu)
	elif opcode == 0x33:
		return INC_33(cpu)
	elif opcode == 0x34:
		return INC_34(cpu)
	elif opcode == 0x35:
		return DEC_35(cpu)
	elif opcode == 0x36:
		return LD_36(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x37:
		return SCF_37(cpu)
	elif opcode == 0x38:
		return JR_38(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x39:
		return ADD_39(cpu)
	elif opcode == 0x3A:
		return LD_3A(cpu)
	elif opcode == 0x3B:
		return DEC_3B(cpu)
	elif opcode == 0x3C:
		return INC_3C(cpu)
	elif opcode == 0x3D:
		return DEC_3D(cpu)
	elif opcode == 0x3E:
		return LD_3E(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0x3F:
		return CCF_3F(cpu)
	elif opcode == 0x40:
		return LD_40(cpu)
	elif opcode == 0x41:
		return LD_41(cpu)
	elif opcode == 0x42:
		return LD_42(cpu)
	elif opcode == 0x43:
		return LD_43(cpu)
	elif opcode == 0x44:
		return LD_44(cpu)
	elif opcode == 0x45:
		return LD_45(cpu)
	elif opcode == 0x46:
		return LD_46(cpu)
	elif opcode == 0x47:
		return LD_47(cpu)
	elif opcode == 0x48:
		return LD_48(cpu)
	elif opcode == 0x49:
		return LD_49(cpu)
	elif opcode == 0x4A:
		return LD_4A(cpu)
	elif opcode == 0x4B:
		return LD_4B(cpu)
	elif opcode == 0x4C:
		return LD_4C(cpu)
	elif opcode == 0x4D:
		return LD_4D(cpu)
	elif opcode == 0x4E:
		return LD_4E(cpu)
	elif opcode == 0x4F:
		return LD_4F(cpu)
	elif opcode == 0x50:
		return LD_50(cpu)
	elif opcode == 0x51:
		return LD_51(cpu)
	elif opcode == 0x52:
		return LD_52(cpu)
	elif opcode == 0x53:
		return LD_53(cpu)
	elif opcode == 0x54:
		return LD_54(cpu)
	elif opcode == 0x55:
		return LD_55(cpu)
	elif opcode == 0x56:
		return LD_56(cpu)
	elif opcode == 0x57:
		return LD_57(cpu)
	elif opcode == 0x58:
		return LD_58(cpu)
	elif opcode == 0x59:
		return LD_59(cpu)
	elif opcode == 0x5A:
		return LD_5A(cpu)
	elif opcode == 0x5B:
		return LD_5B(cpu)
	elif opcode == 0x5C:
		return LD_5C(cpu)
	elif opcode == 0x5D:
		return LD_5D(cpu)
	elif opcode == 0x5E:
		return LD_5E(cpu)
	elif opcode == 0x5F:
		return LD_5F(cpu)
	elif opcode == 0x60:
		return LD_60(cpu)
	elif opcode == 0x61:
		return LD_61(cpu)
	elif opcode == 0x62:
		return LD_62(cpu)
	elif opcode == 0x63:
		return LD_63(cpu)
	elif opcode == 0x64:
		return LD_64(cpu)
	elif opcode == 0x65:
		return LD_65(cpu)
	elif opcode == 0x66:
		return LD_66(cpu)
	elif opcode == 0x67:
		return LD_67(cpu)
	elif opcode == 0x68:
		return LD_68(cpu)
	elif opcode == 0x69:
		return LD_69(cpu)
	elif opcode == 0x6A:
		return LD_6A(cpu)
	elif opcode == 0x6B:
		return LD_6B(cpu)
	elif opcode == 0x6C:
		return LD_6C(cpu)
	elif opcode == 0x6D:
		return LD_6D(cpu)
	elif opcode == 0x6E:
		return LD_6E(cpu)
	elif opcode == 0x6F:
		return LD_6F(cpu)
	elif opcode == 0x70:
		return LD_70(cpu)
	elif opcode == 0x71:
		return LD_71(cpu)
	elif opcode == 0x72:
		return LD_72(cpu)
	elif opcode == 0x73:
		return LD_73(cpu)
	elif opcode == 0x74:
		return LD_74(cpu)
	elif opcode == 0x75:
		return LD_75(cpu)
	elif opcode == 0x76:
		return HALT_76(cpu)
	elif opcode == 0x77:
		return LD_77(cpu)
	elif opcode == 0x78:
		return LD_78(cpu)
	elif opcode == 0x79:
		return LD_79(cpu)
	elif opcode == 0x7A:
		return LD_7A(cpu)
	elif opcode == 0x7B:
		return LD_7B(cpu)
	elif opcode == 0x7C:
		return LD_7C(cpu)
	elif opcode == 0x7D:
		return LD_7D(cpu)
	elif opcode == 0x7E:
		return LD_7E(cpu)
	elif opcode == 0x7F:
		return LD_7F(cpu)
	elif opcode == 0x80:
		return ADD_80(cpu)
	elif opcode == 0x81:
		return ADD_81(cpu)
	elif opcode == 0x82:
		return ADD_82(cpu)
	elif opcode == 0x83:
		return ADD_83(cpu)
	elif opcode == 0x84:
		return ADD_84(cpu)
	elif opcode == 0x85:
		return ADD_85(cpu)
	elif opcode == 0x86:
		return ADD_86(cpu)
	elif opcode == 0x87:
		return ADD_87(cpu)
	elif opcode == 0x88:
		return ADC_88(cpu)
	elif opcode == 0x89:
		return ADC_89(cpu)
	elif opcode == 0x8A:
		return ADC_8A(cpu)
	elif opcode == 0x8B:
		return ADC_8B(cpu)
	elif opcode == 0x8C:
		return ADC_8C(cpu)
	elif opcode == 0x8D:
		return ADC_8D(cpu)
	elif opcode == 0x8E:
		return ADC_8E(cpu)
	elif opcode == 0x8F:
		return ADC_8F(cpu)
	elif opcode == 0x90:
		return SUB_90(cpu)
	elif opcode == 0x91:
		return SUB_91(cpu)
	elif opcode == 0x92:
		return SUB_92(cpu)
	elif opcode == 0x93:
		return SUB_93(cpu)
	elif opcode == 0x94:
		return SUB_94(cpu)
	elif opcode == 0x95:
		return SUB_95(cpu)
	elif opcode == 0x96:
		return SUB_96(cpu)
	elif opcode == 0x97:
		return SUB_97(cpu)
	elif opcode == 0x98:
		return SBC_98(cpu)
	elif opcode == 0x99:
		return SBC_99(cpu)
	elif opcode == 0x9A:
		return SBC_9A(cpu)
	elif opcode == 0x9B:
		return SBC_9B(cpu)
	elif opcode == 0x9C:
		return SBC_9C(cpu)
	elif opcode == 0x9D:
		return SBC_9D(cpu)
	elif opcode == 0x9E:
		return SBC_9E(cpu)
	elif opcode == 0x9F:
		return SBC_9F(cpu)
	elif opcode == 0xA0:
		return AND_A0(cpu)
	elif opcode == 0xA1:
		return AND_A1(cpu)
	elif opcode == 0xA2:
		return AND_A2(cpu)
	elif opcode == 0xA3:
		return AND_A3(cpu)
	elif opcode == 0xA4:
		return AND_A4(cpu)
	elif opcode == 0xA5:
		return AND_A5(cpu)
	elif opcode == 0xA6:
		return AND_A6(cpu)
	elif opcode == 0xA7:
		return AND_A7(cpu)
	elif opcode == 0xA8:
		return XOR_A8(cpu)
	elif opcode == 0xA9:
		return XOR_A9(cpu)
	elif opcode == 0xAA:
		return XOR_AA(cpu)
	elif opcode == 0xAB:
		return XOR_AB(cpu)
	elif opcode == 0xAC:
		return XOR_AC(cpu)
	elif opcode == 0xAD:
		return XOR_AD(cpu)
	elif opcode == 0xAE:
		return XOR_AE(cpu)
	elif opcode == 0xAF:
		return XOR_AF(cpu)
	elif opcode == 0xB0:
		return OR_B0(cpu)
	elif opcode == 0xB1:
		return OR_B1(cpu)
	elif opcode == 0xB2:
		return OR_B2(cpu)
	elif opcode == 0xB3:
		return OR_B3(cpu)
	elif opcode == 0xB4:
		return OR_B4(cpu)
	elif opcode == 0xB5:
		return OR_B5(cpu)
	elif opcode == 0xB6:
		return OR_B6(cpu)
	elif opcode == 0xB7:
		return OR_B7(cpu)
	elif opcode == 0xB8:
		return CP_B8(cpu)
	elif opcode == 0xB9:
		return CP_B9(cpu)
	elif opcode == 0xBA:
		return CP_BA(cpu)
	elif opcode == 0xBB:
		return CP_BB(cpu)
	elif opcode == 0xBC:
		return CP_BC(cpu)
	elif opcode == 0xBD:
		return CP_BD(cpu)
	elif opcode == 0xBE:
		return CP_BE(cpu)
	elif opcode == 0xBF:
		return CP_BF(cpu)
	elif opcode == 0xC0:
		return RET_C0(cpu)
	elif opcode == 0xC1:
		return POP_C1(cpu)
	elif opcode == 0xC2:
		return JP_C2(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xC3:
		return JP_C3(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xC4:
		return CALL_C4(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xC5:
		return PUSH_C5(cpu)
	elif opcode == 0xC6:
		return ADD_C6(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xC7:
		return RST_C7(cpu)
	elif opcode == 0xC8:
		return RET_C8(cpu)
	elif opcode == 0xC9:
		return RET_C9(cpu)
	elif opcode == 0xCA:
		return JP_CA(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xCB:
		return PREFIX_CB(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xCC:
		return CALL_CC(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xCD:
		return CALL_CD(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xCE:
		return ADC_CE(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xCF:
		return RST_CF(cpu)
	elif opcode == 0xD0:
		return RET_D0(cpu)
	elif opcode == 0xD1:
		return POP_D1(cpu)
	elif opcode == 0xD2:
		return JP_D2(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xD4:
		return CALL_D4(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xD5:
		return PUSH_D5(cpu)
	elif opcode == 0xD6:
		return SUB_D6(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xD7:
		return RST_D7(cpu)
	elif opcode == 0xD8:
		return RET_D8(cpu)
	elif opcode == 0xD9:
		return RETI_D9(cpu)
	elif opcode == 0xDA:
		return JP_DA(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xDC:
		return CALL_DC(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xDE:
		return SBC_DE(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xDF:
		return RST_DF(cpu)
	elif opcode == 0xE0:
		return LDH_E0(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xE1:
		return POP_E1(cpu)
	elif opcode == 0xE2:
		return LD_E2(cpu)
	elif opcode == 0xE5:
		return PUSH_E5(cpu)
	elif opcode == 0xE6:
		return AND_E6(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xE7:
		return RST_E7(cpu)
	elif opcode == 0xE8:
		return ADD_E8(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xE9:
		return JP_E9(cpu)
	elif opcode == 0xEA:
		return LD_EA(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xEE:
		return XOR_EE(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xEF:
		return RST_EF(cpu)
	elif opcode == 0xF0:
		return LDH_F0(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xF1:
		return POP_F1(cpu)
	elif opcode == 0xF2:
		return LD_F2(cpu)
	elif opcode == 0xF3:
		return DI_F3(cpu)
	elif opcode == 0xF5:
		return PUSH_F5(cpu)
	elif opcode == 0xF6:
		return OR_F6(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xF7:
		return RST_F7(cpu)
	elif opcode == 0xF8:
		return LD_F8(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xF9:
		return LD_F9(cpu)
	elif opcode == 0xFA:
		return LD_FA(cpu, (cpu.memory.read_byte(cpu.PC + 2) << 8) + cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xFB:
		return EI_FB(cpu)
	elif opcode == 0xFE:
		return CP_FE(cpu, cpu.memory.read_byte(cpu.PC + 1))
	elif opcode == 0xFF:
		return RST_FF(cpu)
	elif opcode == 0xCB00:
		return RLC_CB00(cpu)
	elif opcode == 0xCB01:
		return RLC_CB01(cpu)
	elif opcode == 0xCB02:
		return RLC_CB02(cpu)
	elif opcode == 0xCB03:
		return RLC_CB03(cpu)
	elif opcode == 0xCB04:
		return RLC_CB04(cpu)
	elif opcode == 0xCB05:
		return RLC_CB05(cpu)
	elif opcode == 0xCB06:
		return RLC_CB06(cpu)
	elif opcode == 0xCB07:
		return RLC_CB07(cpu)
	elif opcode == 0xCB08:
		return RRC_CB08(cpu)
	elif opcode == 0xCB09:
		return RRC_CB09(cpu)
	elif opcode == 0xCB0A:
		return RRC_CB0A(cpu)
	elif opcode == 0xCB0B:
		return RRC_CB0B(cpu)
	elif opcode == 0xCB0C:
		return RRC_CB0C(cpu)
	elif opcode == 0xCB0D:
		return RRC_CB0D(cpu)
	elif opcode == 0xCB0E:
		return RRC_CB0E(cpu)
	elif opcode == 0xCB0F:
		return RRC_CB0F(cpu)
	elif opcode == 0xCB10:
		return RL_CB10(cpu)
	elif opcode == 0xCB11:
		return RL_CB11(cpu)
	elif opcode == 0xCB12:
		return RL_CB12(cpu)
	elif opcode == 0xCB13:
		return RL_CB13(cpu)
	elif opcode == 0xCB14:
		return RL_CB14(cpu)
	elif opcode == 0xCB15:
		return RL_CB15(cpu)
	elif opcode == 0xCB16:
		return RL_CB16(cpu)
	elif opcode == 0xCB17:
		return RL_CB17(cpu)
	elif opcode == 0xCB18:
		return RR_CB18(cpu)
	elif opcode == 0xCB19:
		return RR_CB19(cpu)
	elif opcode == 0xCB1A:
		return RR_CB1A(cpu)
	elif opcode == 0xCB1B:
		return RR_CB1B(cpu)
	elif opcode == 0xCB1C:
		return RR_CB1C(cpu)
	elif opcode == 0xCB1D:
		return RR_CB1D(cpu)
	elif opcode == 0xCB1E:
		return RR_CB1E(cpu)
	elif opcode == 0xCB1F:
		return RR_CB1F(cpu)
	elif opcode == 0xCB20:
		return SLA_CB20(cpu)
	elif opcode == 0xCB21:
		return SLA_CB21(cpu)
	elif opcode == 0xCB22:
		return SLA_CB22(cpu)
	elif opcode == 0xCB23:
		return SLA_CB23(cpu)
	elif opcode == 0xCB24:
		return SLA_CB24(cpu)
	elif opcode == 0xCB25:
		return SLA_CB25(cpu)
	elif opcode == 0xCB26:
		return SLA_CB26(cpu)
	elif opcode == 0xCB27:
		return SLA_CB27(cpu)
	elif opcode == 0xCB28:
		return SRA_CB28(cpu)
	elif opcode == 0xCB29:
		return SRA_CB29(cpu)
	elif opcode == 0xCB2A:
		return SRA_CB2A(cpu)
	elif opcode == 0xCB2B:
		return SRA_CB2B(cpu)
	elif opcode == 0xCB2C:
		return SRA_CB2C(cpu)
	elif opcode == 0xCB2D:
		return SRA_CB2D(cpu)
	elif opcode == 0xCB2E:
		return SRA_CB2E(cpu)
	elif opcode == 0xCB2F:
		return SRA_CB2F(cpu)
	elif opcode == 0xCB30:
		return SWAP_CB30(cpu)
	elif opcode == 0xCB31:
		return SWAP_CB31(cpu)
	elif opcode == 0xCB32:
		return SWAP_CB32(cpu)
	elif opcode == 0xCB33:
		return SWAP_CB33(cpu)
	elif opcode == 0xCB34:
		return SWAP_CB34(cpu)
	elif opcode == 0xCB35:
		return SWAP_CB35(cpu)
	elif opcode == 0xCB36:
		return SWAP_CB36(cpu)
	elif opcode == 0xCB37:
		return SWAP_CB37(cpu)
	elif opcode == 0xCB38:
		return SRL_CB38(cpu)
	elif opcode == 0xCB39:
		return SRL_CB39(cpu)
	elif opcode == 0xCB3A:
		return SRL_CB3A(cpu)
	elif opcode == 0xCB3B:
		return SRL_CB3B(cpu)
	elif opcode == 0xCB3C:
		return SRL_CB3C(cpu)
	elif opcode == 0xCB3D:
		return SRL_CB3D(cpu)
	elif opcode == 0xCB3E:
		return SRL_CB3E(cpu)
	elif opcode == 0xCB3F:
		return SRL_CB3F(cpu)
	elif opcode == 0xCB40:
		return BIT_CB40(cpu)
	elif opcode == 0xCB41:
		return BIT_CB41(cpu)
	elif opcode == 0xCB42:
		return BIT_CB42(cpu)
	elif opcode == 0xCB43:
		return BIT_CB43(cpu)
	elif opcode == 0xCB44:
		return BIT_CB44(cpu)
	elif opcode == 0xCB45:
		return BIT_CB45(cpu)
	elif opcode == 0xCB46:
		return BIT_CB46(cpu)
	elif opcode == 0xCB47:
		return BIT_CB47(cpu)
	elif opcode == 0xCB48:
		return BIT_CB48(cpu)
	elif opcode == 0xCB49:
		return BIT_CB49(cpu)
	elif opcode == 0xCB4A:
		return BIT_CB4A(cpu)
	elif opcode == 0xCB4B:
		return BIT_CB4B(cpu)
	elif opcode == 0xCB4C:
		return BIT_CB4C(cpu)
	elif opcode == 0xCB4D:
		return BIT_CB4D(cpu)
	elif opcode == 0xCB4E:
		return BIT_CB4E(cpu)
	elif opcode == 0xCB4F:
		return BIT_CB4F(cpu)
	elif opcode == 0xCB50:
		return BIT_CB50(cpu)
	elif opcode == 0xCB51:
		return BIT_CB51(cpu)
	elif opcode == 0xCB52:
		return BIT_CB52(cpu)
	elif opcode == 0xCB53:
		return BIT_CB53(cpu)
	elif opcode == 0xCB54:
		return BIT_CB54(cpu)
	elif opcode == 0xCB55:
		return BIT_CB55(cpu)
	elif opcode == 0xCB56:
		return BIT_CB56(cpu)
	elif opcode == 0xCB57:
		return BIT_CB57(cpu)
	elif opcode == 0xCB58:
		return BIT_CB58(cpu)
	elif opcode == 0xCB59:
		return BIT_CB59(cpu)
	elif opcode == 0xCB5A:
		return BIT_CB5A(cpu)
	elif opcode == 0xCB5B:
		return BIT_CB5B(cpu)
	elif opcode == 0xCB5C:
		return BIT_CB5C(cpu)
	elif opcode == 0xCB5D:
		return BIT_CB5D(cpu)
	elif opcode == 0xCB5E:
		return BIT_CB5E(cpu)
	elif opcode == 0xCB5F:
		return BIT_CB5F(cpu)
	elif opcode == 0xCB60:
		return BIT_CB60(cpu)
	elif opcode == 0xCB61:
		return BIT_CB61(cpu)
	elif opcode == 0xCB62:
		return BIT_CB62(cpu)
	elif opcode == 0xCB63:
		return BIT_CB63(cpu)
	elif opcode == 0xCB64:
		return BIT_CB64(cpu)
	elif opcode == 0xCB65:
		return BIT_CB65(cpu)
	elif opcode == 0xCB66:
		return BIT_CB66(cpu)
	elif opcode == 0xCB67:
		return BIT_CB67(cpu)
	elif opcode == 0xCB68:
		return BIT_CB68(cpu)
	elif opcode == 0xCB69:
		return BIT_CB69(cpu)
	elif opcode == 0xCB6A:
		return BIT_CB6A(cpu)
	elif opcode == 0xCB6B:
		return BIT_CB6B(cpu)
	elif opcode == 0xCB6C:
		return BIT_CB6C(cpu)
	elif opcode == 0xCB6D:
		return BIT_CB6D(cpu)
	elif opcode == 0xCB6E:
		return BIT_CB6E(cpu)
	elif opcode == 0xCB6F:
		return BIT_CB6F(cpu)
	elif opcode == 0xCB70:
		return BIT_CB70(cpu)
	elif opcode == 0xCB71:
		return BIT_CB71(cpu)
	elif opcode == 0xCB72:
		return BIT_CB72(cpu)
	elif opcode == 0xCB73:
		return BIT_CB73(cpu)
	elif opcode == 0xCB74:
		return BIT_CB74(cpu)
	elif opcode == 0xCB75:
		return BIT_CB75(cpu)
	elif opcode == 0xCB76:
		return BIT_CB76(cpu)
	elif opcode == 0xCB77:
		return BIT_CB77(cpu)
	elif opcode == 0xCB78:
		return BIT_CB78(cpu)
	elif opcode == 0xCB79:
		return BIT_CB79(cpu)
	elif opcode == 0xCB7A:
		return BIT_CB7A(cpu)
	elif opcode == 0xCB7B:
		return BIT_CB7B(cpu)
	elif opcode == 0xCB7C:
		return BIT_CB7C(cpu)
	elif opcode == 0xCB7D:
		return BIT_CB7D(cpu)
	elif opcode == 0xCB7E:
		return BIT_CB7E(cpu)
	elif opcode == 0xCB7F:
		return BIT_CB7F(cpu)
	elif opcode == 0xCB80:
		return RES_CB80(cpu)
	elif opcode == 0xCB81:
		return RES_CB81(cpu)
	elif opcode == 0xCB82:
		return RES_CB82(cpu)
	elif opcode == 0xCB83:
		return RES_CB83(cpu)
	elif opcode == 0xCB84:
		return RES_CB84(cpu)
	elif opcode == 0xCB85:
		return RES_CB85(cpu)
	elif opcode == 0xCB86:
		return RES_CB86(cpu)
	elif opcode == 0xCB87:
		return RES_CB87(cpu)
	elif opcode == 0xCB88:
		return RES_CB88(cpu)
	elif opcode == 0xCB89:
		return RES_CB89(cpu)
	elif opcode == 0xCB8A:
		return RES_CB8A(cpu)
	elif opcode == 0xCB8B:
		return RES_CB8B(cpu)
	elif opcode == 0xCB8C:
		return RES_CB8C(cpu)
	elif opcode == 0xCB8D:
		return RES_CB8D(cpu)
	elif opcode == 0xCB8E:
		return RES_CB8E(cpu)
	elif opcode == 0xCB8F:
		return RES_CB8F(cpu)
	elif opcode == 0xCB90:
		return RES_CB90(cpu)
	elif opcode == 0xCB91:
		return RES_CB91(cpu)
	elif opcode == 0xCB92:
		return RES_CB92(cpu)
	elif opcode == 0xCB93:
		return RES_CB93(cpu)
	elif opcode == 0xCB94:
		return RES_CB94(cpu)
	elif opcode == 0xCB95:
		return RES_CB95(cpu)
	elif opcode == 0xCB96:
		return RES_CB96(cpu)
	elif opcode == 0xCB97:
		return RES_CB97(cpu)
	elif opcode == 0xCB98:
		return RES_CB98(cpu)
	elif opcode == 0xCB99:
		return RES_CB99(cpu)
	elif opcode == 0xCB9A:
		return RES_CB9A(cpu)
	elif opcode == 0xCB9B:
		return RES_CB9B(cpu)
	elif opcode == 0xCB9C:
		return RES_CB9C(cpu)
	elif opcode == 0xCB9D:
		return RES_CB9D(cpu)
	elif opcode == 0xCB9E:
		return RES_CB9E(cpu)
	elif opcode == 0xCB9F:
		return RES_CB9F(cpu)
	elif opcode == 0xCBA0:
		return RES_CBA0(cpu)
	elif opcode == 0xCBA1:
		return RES_CBA1(cpu)
	elif opcode == 0xCBA2:
		return RES_CBA2(cpu)
	elif opcode == 0xCBA3:
		return RES_CBA3(cpu)
	elif opcode == 0xCBA4:
		return RES_CBA4(cpu)
	elif opcode == 0xCBA5:
		return RES_CBA5(cpu)
	elif opcode == 0xCBA6:
		return RES_CBA6(cpu)
	elif opcode == 0xCBA7:
		return RES_CBA7(cpu)
	elif opcode == 0xCBA8:
		return RES_CBA8(cpu)
	elif opcode == 0xCBA9:
		return RES_CBA9(cpu)
	elif opcode == 0xCBAA:
		return RES_CBAA(cpu)
	elif opcode == 0xCBAB:
		return RES_CBAB(cpu)
	elif opcode == 0xCBAC:
		return RES_CBAC(cpu)
	elif opcode == 0xCBAD:
		return RES_CBAD(cpu)
	elif opcode == 0xCBAE:
		return RES_CBAE(cpu)
	elif opcode == 0xCBAF:
		return RES_CBAF(cpu)
	elif opcode == 0xCBB0:
		return RES_CBB0(cpu)
	elif opcode == 0xCBB1:
		return RES_CBB1(cpu)
	elif opcode == 0xCBB2:
		return RES_CBB2(cpu)
	elif opcode == 0xCBB3:
		return RES_CBB3(cpu)
	elif opcode == 0xCBB4:
		return RES_CBB4(cpu)
	elif opcode == 0xCBB5:
		return RES_CBB5(cpu)
	elif opcode == 0xCBB6:
		return RES_CBB6(cpu)
	elif opcode == 0xCBB7:
		return RES_CBB7(cpu)
	elif opcode == 0xCBB8:
		return RES_CBB8(cpu)
	elif opcode == 0xCBB9:
		return RES_CBB9(cpu)
	elif opcode == 0xCBBA:
		return RES_CBBA(cpu)
	elif opcode == 0xCBBB:
		return RES_CBBB(cpu)
	elif opcode == 0xCBBC:
		return RES_CBBC(cpu)
	elif opcode == 0xCBBD:
		return RES_CBBD(cpu)
	elif opcode == 0xCBBE:
		return RES_CBBE(cpu)
	elif opcode == 0xCBBF:
		return RES_CBBF(cpu)
	elif opcode == 0xCBC0:
		return SET_CBC0(cpu)
	elif opcode == 0xCBC1:
		return SET_CBC1(cpu)
	elif opcode == 0xCBC2:
		return SET_CBC2(cpu)
	elif opcode == 0xCBC3:
		return SET_CBC3(cpu)
	elif opcode == 0xCBC4:
		return SET_CBC4(cpu)
	elif opcode == 0xCBC5:
		return SET_CBC5(cpu)
	elif opcode == 0xCBC6:
		return SET_CBC6(cpu)
	elif opcode == 0xCBC7:
		return SET_CBC7(cpu)
	elif opcode == 0xCBC8:
		return SET_CBC8(cpu)
	elif opcode == 0xCBC9:
		return SET_CBC9(cpu)
	elif opcode == 0xCBCA:
		return SET_CBCA(cpu)
	elif opcode == 0xCBCB:
		return SET_CBCB(cpu)
	elif opcode == 0xCBCC:
		return SET_CBCC(cpu)
	elif opcode == 0xCBCD:
		return SET_CBCD(cpu)
	elif opcode == 0xCBCE:
		return SET_CBCE(cpu)
	elif opcode == 0xCBCF:
		return SET_CBCF(cpu)
	elif opcode == 0xCBD0:
		return SET_CBD0(cpu)
	elif opcode == 0xCBD1:
		return SET_CBD1(cpu)
	elif opcode == 0xCBD2:
		return SET_CBD2(cpu)
	elif opcode == 0xCBD3:
		return SET_CBD3(cpu)
	elif opcode == 0xCBD4:
		return SET_CBD4(cpu)
	elif opcode == 0xCBD5:
		return SET_CBD5(cpu)
	elif opcode == 0xCBD6:
		return SET_CBD6(cpu)
	elif opcode == 0xCBD7:
		return SET_CBD7(cpu)
	elif opcode == 0xCBD8:
		return SET_CBD8(cpu)
	elif opcode == 0xCBD9:
		return SET_CBD9(cpu)
	elif opcode == 0xCBDA:
		return SET_CBDA(cpu)
	elif opcode == 0xCBDB:
		return SET_CBDB(cpu)
	elif opcode == 0xCBDC:
		return SET_CBDC(cpu)
	elif opcode == 0xCBDD:
		return SET_CBDD(cpu)
	elif opcode == 0xCBDE:
		return SET_CBDE(cpu)
	elif opcode == 0xCBDF:
		return SET_CBDF(cpu)
	elif opcode == 0xCBE0:
		return SET_CBE0(cpu)
	elif opcode == 0xCBE1:
		return SET_CBE1(cpu)
	elif opcode == 0xCBE2:
		return SET_CBE2(cpu)
	elif opcode == 0xCBE3:
		return SET_CBE3(cpu)
	elif opcode == 0xCBE4:
		return SET_CBE4(cpu)
	elif opcode == 0xCBE5:
		return SET_CBE5(cpu)
	elif opcode == 0xCBE6:
		return SET_CBE6(cpu)
	elif opcode == 0xCBE7:
		return SET_CBE7(cpu)
	elif opcode == 0xCBE8:
		return SET_CBE8(cpu)
	elif opcode == 0xCBE9:
		return SET_CBE9(cpu)
	elif opcode == 0xCBEA:
		return SET_CBEA(cpu)
	elif opcode == 0xCBEB:
		return SET_CBEB(cpu)
	elif opcode == 0xCBEC:
		return SET_CBEC(cpu)
	elif opcode == 0xCBED:
		return SET_CBED(cpu)
	elif opcode == 0xCBEE:
		return SET_CBEE(cpu)
	elif opcode == 0xCBEF:
		return SET_CBEF(cpu)
	elif opcode == 0xCBF0:
		return SET_CBF0(cpu)
	elif opcode == 0xCBF1:
		return SET_CBF1(cpu)
	elif opcode == 0xCBF2:
		return SET_CBF2(cpu)
	elif opcode == 0xCBF3:
		return SET_CBF3(cpu)
	elif opcode == 0xCBF4:
		return SET_CBF4(cpu)
	elif opcode == 0xCBF5:
		return SET_CBF5(cpu)
	elif opcode == 0xCBF6:
		return SET_CBF6(cpu)
	elif opcode == 0xCBF7:
		return SET_CBF7(cpu)
	elif opcode == 0xCBF8:
		return SET_CBF8(cpu)
	elif opcode == 0xCBF9:
		return SET_CBF9(cpu)
	elif opcode == 0xCBFA:
		return SET_CBFA(cpu)
	elif opcode == 0xCBFB:
		return SET_CBFB(cpu)
	elif opcode == 0xCBFC:
		return SET_CBFC(cpu)
	elif opcode == 0xCBFD:
		return SET_CBFD(cpu)
	elif opcode == 0xCBFE:
		return SET_CBFE(cpu)
	elif opcode == 0xCBFF:
		return SET_CBFF(cpu)

def fetch_opcode(cpu):
	opcode = cpu.memory.read_byte(cpu.PC)
	if opcode == 0xCB:  # Prefix CB instruction
		opcode = 0xCB00 | cpu.memory.read_byte(cpu.PC + 1)
	return opcode

