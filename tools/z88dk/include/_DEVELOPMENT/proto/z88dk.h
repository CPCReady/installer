include(__link__.m4)

#ifndef __Z88DK_H__
#define __Z88DK_H__

#include <arch.h>

// z88dk version

// 1990 = 1.99A
// 1991 = 1.99B
// 1992 = 1.99C
// 2000 = 2.00

#define Z88DK_VERSION  __Z88DK

// section information

#define SECTION_ORG(sec)    ((unsigned int)SECTION_ORG_##sec())
#define SECTION_END(sec)    ((unsigned int)SECTION_END_##sec())
#define SECTION_SIZE(sec)   ((unsigned int)SECTION_SIZE_##sec())

extern unsigned char _CODE_head[];
extern unsigned char _DATA_head[];
extern unsigned char _BSS_head[];

#define SECTION_CODE_ORG()  ((unsigned int)_CODE_head)
#define SECTION_DATA_ORG()  ((unsigned int)_DATA_head)
#define SECTION_BSS_ORG()   ((unsigned int)_BSS_head)

extern unsigned char _CODE_END_tail[];
extern unsigned char _DATA_END_tail[];
extern unsigned char _BSS_UNINITIALIZED_head[];

#define SECTION_CODE_END()  ((unsigned int)_CODE_END_tail)
#define SECTION_DATA_END()  ((unsigned int)_DATA_END_tail)
#define SECTION_BSS_END()   ((unsigned int)_BSS_UNINITIALIZED_head)

#if __CLANG

extern unsigned int SECTION_SIZE_CODE(void);
extern unsigned int SECTION_SIZE_DATA(void);
extern unsigned int SECTION_SIZE_BSS(void);

#endif

#if __SDCC

extern unsigned int SECTION_SIZE_CODE(void) __preserves_regs(a,b,c,d,e,iyl,iyh);
extern unsigned int SECTION_SIZE_DATA(void) __preserves_regs(a,b,c,d,e,iyl,iyh);
extern unsigned int SECTION_SIZE_BSS(void) __preserves_regs(a,b,c,d,e,iyl,iyh);

#endif

#if __SCCZ80

extern unsigned int SECTION_SIZE_CODE(void);
extern unsigned int SECTION_SIZE_DATA(void);
extern unsigned int SECTION_SIZE_BSS(void);

#endif

#define SECTION_CODE_SIZE() SECTION_SIZE_CODE()
#define SECTION_DATA_SIZE() SECTION_SIZE_DATA()
#define SECTION_BSS_SIZE()  SECTION_SIZE_BSS()

#endif
