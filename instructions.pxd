# This is a generated file.

import cython
cimport cpu
from cpu cimport CPU
from libc.stdint cimport uint8_t, uint16_t, uint32_t
@cython.locals(t=int)
cdef uint32_t NOP_00(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_01(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t LD_02(CPU cpu)

@cython.locals(t=int)
cdef uint32_t INC_03(CPU cpu)

@cython.locals(t=int)
cdef uint32_t INC_04(CPU cpu)

@cython.locals(t=int)
cdef uint32_t DEC_05(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_06(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t RLCA_07(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_08(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t ADD_09(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_0A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t DEC_0B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t INC_0C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t DEC_0D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_0E(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t RRCA_0F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t STOP_10(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t LD_11(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t LD_12(CPU cpu)

@cython.locals(t=int)
cdef uint32_t INC_13(CPU cpu)

@cython.locals(t=int)
cdef uint32_t INC_14(CPU cpu)

@cython.locals(t=int)
cdef uint32_t DEC_15(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_16(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t RLA_17(CPU cpu)

@cython.locals(t=int)
cdef uint32_t JR_18(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t ADD_19(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_1A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t DEC_1B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t INC_1C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t DEC_1D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_1E(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t RRA_1F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t JR_20(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t LD_21(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t LD_22(CPU cpu)

@cython.locals(t=int)
cdef uint32_t INC_23(CPU cpu)

@cython.locals(t=int)
cdef uint32_t INC_24(CPU cpu)

@cython.locals(t=int)
cdef uint32_t DEC_25(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_26(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t DAA_27(CPU cpu)

@cython.locals(t=int)
cdef uint32_t JR_28(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t ADD_29(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_2A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t DEC_2B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t INC_2C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t DEC_2D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_2E(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t CPL_2F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t JR_30(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t LD_31(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t LD_32(CPU cpu)

@cython.locals(t=int)
cdef uint32_t INC_33(CPU cpu)

@cython.locals(t=int)
cdef uint32_t INC_34(CPU cpu)

@cython.locals(t=int)
cdef uint32_t DEC_35(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_36(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t SCF_37(CPU cpu)

@cython.locals(t=int)
cdef uint32_t JR_38(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t ADD_39(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_3A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t DEC_3B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t INC_3C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t DEC_3D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_3E(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t CCF_3F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_40(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_41(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_42(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_43(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_44(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_45(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_46(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_47(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_48(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_49(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_4A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_4B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_4C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_4D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_4E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_4F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_50(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_51(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_52(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_53(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_54(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_55(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_56(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_57(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_58(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_59(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_5A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_5B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_5C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_5D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_5E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_5F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_60(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_61(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_62(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_63(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_64(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_65(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_66(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_67(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_68(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_69(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_6A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_6B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_6C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_6D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_6E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_6F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_70(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_71(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_72(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_73(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_74(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_75(CPU cpu)

@cython.locals(t=int)
cdef uint32_t HALT_76(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_77(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_78(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_79(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_7A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_7B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_7C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_7D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_7E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_7F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADD_80(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADD_81(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADD_82(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADD_83(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADD_84(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADD_85(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADD_86(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADD_87(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADC_88(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADC_89(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADC_8A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADC_8B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADC_8C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADC_8D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADC_8E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADC_8F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SUB_90(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SUB_91(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SUB_92(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SUB_93(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SUB_94(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SUB_95(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SUB_96(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SUB_97(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SBC_98(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SBC_99(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SBC_9A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SBC_9B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SBC_9C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SBC_9D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SBC_9E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SBC_9F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t AND_A0(CPU cpu)

@cython.locals(t=int)
cdef uint32_t AND_A1(CPU cpu)

@cython.locals(t=int)
cdef uint32_t AND_A2(CPU cpu)

@cython.locals(t=int)
cdef uint32_t AND_A3(CPU cpu)

@cython.locals(t=int)
cdef uint32_t AND_A4(CPU cpu)

@cython.locals(t=int)
cdef uint32_t AND_A5(CPU cpu)

@cython.locals(t=int)
cdef uint32_t AND_A6(CPU cpu)

@cython.locals(t=int)
cdef uint32_t AND_A7(CPU cpu)

@cython.locals(t=int)
cdef uint32_t XOR_A8(CPU cpu)

@cython.locals(t=int)
cdef uint32_t XOR_A9(CPU cpu)

@cython.locals(t=int)
cdef uint32_t XOR_AA(CPU cpu)

@cython.locals(t=int)
cdef uint32_t XOR_AB(CPU cpu)

@cython.locals(t=int)
cdef uint32_t XOR_AC(CPU cpu)

@cython.locals(t=int)
cdef uint32_t XOR_AD(CPU cpu)

@cython.locals(t=int)
cdef uint32_t XOR_AE(CPU cpu)

@cython.locals(t=int)
cdef uint32_t XOR_AF(CPU cpu)

@cython.locals(t=int)
cdef uint32_t OR_B0(CPU cpu)

@cython.locals(t=int)
cdef uint32_t OR_B1(CPU cpu)

@cython.locals(t=int)
cdef uint32_t OR_B2(CPU cpu)

@cython.locals(t=int)
cdef uint32_t OR_B3(CPU cpu)

@cython.locals(t=int)
cdef uint32_t OR_B4(CPU cpu)

@cython.locals(t=int)
cdef uint32_t OR_B5(CPU cpu)

@cython.locals(t=int)
cdef uint32_t OR_B6(CPU cpu)

@cython.locals(t=int)
cdef uint32_t OR_B7(CPU cpu)

@cython.locals(t=int)
cdef uint32_t CP_B8(CPU cpu)

@cython.locals(t=int)
cdef uint32_t CP_B9(CPU cpu)

@cython.locals(t=int)
cdef uint32_t CP_BA(CPU cpu)

@cython.locals(t=int)
cdef uint32_t CP_BB(CPU cpu)

@cython.locals(t=int)
cdef uint32_t CP_BC(CPU cpu)

@cython.locals(t=int)
cdef uint32_t CP_BD(CPU cpu)

@cython.locals(t=int)
cdef uint32_t CP_BE(CPU cpu)

@cython.locals(t=int)
cdef uint32_t CP_BF(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RET_C0(CPU cpu)

@cython.locals(t=int)
cdef uint32_t POP_C1(CPU cpu)

@cython.locals(t=int)
cdef uint32_t JP_C2(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t JP_C3(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t CALL_C4(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t PUSH_C5(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADD_C6(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t RST_C7(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RET_C8(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RET_C9(CPU cpu)

@cython.locals(t=int)
cdef uint32_t JP_CA(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t PREFIX_CB(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t CALL_CC(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t CALL_CD(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t ADC_CE(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t RST_CF(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RET_D0(CPU cpu)

@cython.locals(t=int)
cdef uint32_t POP_D1(CPU cpu)

@cython.locals(t=int)
cdef uint32_t JP_D2(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t CALL_D4(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t PUSH_D5(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SUB_D6(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t RST_D7(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RET_D8(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RETI_D9(CPU cpu)

@cython.locals(t=int)
cdef uint32_t JP_DA(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t CALL_DC(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t SBC_DE(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t RST_DF(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LDH_E0(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t POP_E1(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_E2(CPU cpu)

@cython.locals(t=int)
cdef uint32_t PUSH_E5(CPU cpu)

@cython.locals(t=int)
cdef uint32_t AND_E6(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t RST_E7(CPU cpu)

@cython.locals(t=int)
cdef uint32_t ADD_E8(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t JP_E9(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_EA(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t XOR_EE(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t RST_EF(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LDH_F0(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t POP_F1(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_F2(CPU cpu)

@cython.locals(t=int)
cdef uint32_t DI_F3(CPU cpu)

@cython.locals(t=int)
cdef uint32_t PUSH_F5(CPU cpu)

@cython.locals(t=int)
cdef uint32_t OR_F6(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t RST_F7(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_F8(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t LD_F9(CPU cpu)

@cython.locals(t=int)
cdef uint32_t LD_FA(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t EI_FB(CPU cpu)

@cython.locals(t=int)
cdef uint32_t CP_FE(CPU cpu, int v)

@cython.locals(t=int)
cdef uint32_t RST_FF(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RLC_CB00(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RLC_CB01(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RLC_CB02(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RLC_CB03(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RLC_CB04(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RLC_CB05(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RLC_CB06(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RLC_CB07(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RRC_CB08(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RRC_CB09(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RRC_CB0A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RRC_CB0B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RRC_CB0C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RRC_CB0D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RRC_CB0E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RRC_CB0F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RL_CB10(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RL_CB11(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RL_CB12(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RL_CB13(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RL_CB14(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RL_CB15(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RL_CB16(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RL_CB17(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RR_CB18(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RR_CB19(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RR_CB1A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RR_CB1B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RR_CB1C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RR_CB1D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RR_CB1E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RR_CB1F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SLA_CB20(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SLA_CB21(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SLA_CB22(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SLA_CB23(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SLA_CB24(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SLA_CB25(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SLA_CB26(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SLA_CB27(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRA_CB28(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRA_CB29(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRA_CB2A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRA_CB2B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRA_CB2C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRA_CB2D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRA_CB2E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRA_CB2F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SWAP_CB30(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SWAP_CB31(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SWAP_CB32(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SWAP_CB33(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SWAP_CB34(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SWAP_CB35(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SWAP_CB36(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SWAP_CB37(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRL_CB38(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRL_CB39(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRL_CB3A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRL_CB3B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRL_CB3C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRL_CB3D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRL_CB3E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SRL_CB3F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB40(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB41(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB42(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB43(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB44(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB45(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB46(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB47(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB48(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB49(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB4A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB4B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB4C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB4D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB4E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB4F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB50(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB51(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB52(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB53(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB54(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB55(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB56(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB57(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB58(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB59(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB5A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB5B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB5C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB5D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB5E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB5F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB60(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB61(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB62(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB63(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB64(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB65(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB66(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB67(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB68(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB69(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB6A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB6B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB6C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB6D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB6E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB6F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB70(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB71(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB72(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB73(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB74(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB75(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB76(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB77(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB78(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB79(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB7A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB7B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB7C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB7D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB7E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t BIT_CB7F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB80(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB81(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB82(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB83(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB84(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB85(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB86(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB87(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB88(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB89(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB8A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB8B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB8C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB8D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB8E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB8F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB90(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB91(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB92(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB93(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB94(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB95(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB96(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB97(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB98(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB99(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB9A(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB9B(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB9C(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB9D(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB9E(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CB9F(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBA0(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBA1(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBA2(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBA3(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBA4(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBA5(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBA6(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBA7(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBA8(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBA9(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBAA(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBAB(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBAC(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBAD(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBAE(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBAF(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBB0(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBB1(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBB2(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBB3(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBB4(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBB5(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBB6(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBB7(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBB8(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBB9(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBBA(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBBB(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBBC(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBBD(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBBE(CPU cpu)

@cython.locals(t=int)
cdef uint32_t RES_CBBF(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBC0(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBC1(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBC2(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBC3(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBC4(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBC5(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBC6(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBC7(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBC8(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBC9(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBCA(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBCB(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBCC(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBCD(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBCE(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBCF(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBD0(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBD1(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBD2(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBD3(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBD4(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBD5(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBD6(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBD7(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBD8(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBD9(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBDA(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBDB(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBDC(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBDD(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBDE(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBDF(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBE0(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBE1(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBE2(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBE3(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBE4(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBE5(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBE6(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBE7(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBE8(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBE9(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBEA(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBEB(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBEC(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBED(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBEE(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBEF(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBF0(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBF1(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBF2(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBF3(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBF4(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBF5(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBF6(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBF7(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBF8(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBF9(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBFA(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBFB(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBFC(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBFD(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBFE(CPU cpu)

@cython.locals(t=int)
cdef uint32_t SET_CBFF(CPU cpu)

cdef uint32_t execute_opcode(CPU cpu, uint16_t opcode)

@cython.locals(opcode=uint16_t)
cdef uint16_t fetch_opcode(CPU cpu)

