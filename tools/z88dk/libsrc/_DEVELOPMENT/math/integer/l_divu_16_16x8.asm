
INCLUDE "config_private.inc"

SECTION code_clib
SECTION code_math

PUBLIC l_divu_16_16x8, l0_divu_16_16x8

   ; compute:  hl = hl / e, e = hl % e
   ; alters :  af, bc, de, hl

   ; alternate entry (l_divu_16_16x8 - 1)
   ; exchanges divisor / dividend

   ; alternate entry (l0_divu_16_16x8)
   ; skips divide by zero check

IF __CPU_KC160__

   EXTERN l_kc160_divu_16_16x8, l0_kc160_divu_16_16x8

   defc l_divu_16_16x8 =  l_kc160_divu_16_16x8
   defc l0_divu_16_16x8 = l0_kc160_divu_16_16x8

ELIF __CLIB_OPT_IMATH <= 50

   EXTERN l_small_divu_16_16x8, l0_small_divu_16_16x8

   defc l_divu_16_16x8 =  l_small_divu_16_16x8
   defc l0_divu_16_16x8 = l0_small_divu_16_16x8

ELIF __CLIB_OPT_IMATH > 50

   EXTERN l_fast_divu_16_16x8, l0_fast_divu_16_16x8

   defc l_divu_16_16x8 =  l_fast_divu_16_16x8
   defc l0_divu_16_16x8 = l0_fast_divu_16_16x8

ENDIF

