; unsigned char esx_f_chdir(unsigned char *pathname)

SECTION code_esxdos

PUBLIC _esx_f_chdir_fastcall

EXTERN asm_esx_f_chdir

_esx_f_chdir_fastcall:

   push iy
   
   call asm_esx_f_chdir

   pop iy
   ret
