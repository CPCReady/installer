; struct sp1_update *sp1_GetUpdateStruct(uchar row, uchar col)

SECTION code_clib
SECTION code_temp_sp1

PUBLIC sp1_GetUpdateStruct

EXTERN asm_sp1_GetUpdateStruct

sp1_GetUpdateStruct:

   ld hl,2
   add hl,sp
   ld e,(hl)
   inc hl
   inc hl
   ld d,(hl)
   
;   jp asm_sp1_GetUpdateStruct
   push ix
   call asm_sp1_GetUpdateStruct
   pop ix
   ret

; SDCC bridge for Classic
IF __CLASSIC
PUBLIC _sp1_GetUpdateStruct
defc _sp1_GetUpdateStruct = sp1_GetUpdateStruct
ENDIF

