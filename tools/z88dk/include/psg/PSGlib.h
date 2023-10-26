#ifndef __PSG_PSGLIB_H__
#define __PSG_PSGLIB_H__

#include <sys/compiler.h>

/* **************************************************
   PSGlib - C programming library for the SEGA PSG
   (part of devkitSMS - github.com/sverx/devkitSMS )
   Synchronized March 29, 2017
   ************************************************** */

/* SN76489 library */

#define __PSGLIB_PSG_STOPPED   0
#define __PSGLIB_PSG_PLAYING   1

#define __PSGLIB_SFX_CHANNEL2   0x01
#define __PSGLIB_SFX_CHANNEL3   0x02
#define __PSGLIB_SFX_CHANNELS2AND3   0x03

#define PSG_STOPPED         __PSGLIB_PSG_STOPPED
#define PSG_PLAYING         __PSGLIB_PSG_PLAYING

#define SFX_CHANNEL2        __PSGLIB_SFX_CHANNEL2
#define SFX_CHANNEL3        __PSGLIB_SFX_CHANNEL3
#define SFX_CHANNELS2AND3   __PSGLIB_SFX_CHANNELS2AND3

extern void __LIB__ PSGPlay(void *song) __smallc __z88dk_fastcall;


extern void __LIB__ PSGCancelLoop(void) __smallc;


extern void __LIB__ PSGPlayNoRepeat(void *song) __smallc __z88dk_fastcall;


extern void __LIB__ PSGStop(void) __smallc;


extern unsigned char __LIB__ PSGGetStatus(void) __smallc;


extern void __LIB__ PSGSetMusicVolumeAttenuation(unsigned char attenuation) __smallc __z88dk_fastcall;

extern void __LIB__ PSGSFXPlay(void *sfx,unsigned char channels) __smallc;
extern void __LIB__ PSGSFXPlay_callee(void *sfx,unsigned char channels) __smallc __z88dk_callee;
#define PSGSFXPlay(a,b) PSGSFXPlay_callee(a,b)


extern void __LIB__ PSGSFXPlayLoop(void *sfx,unsigned char channels) __smallc;
extern void __LIB__ PSGSFXPlayLoop_callee(void *sfx,unsigned char channels) __smallc __z88dk_callee;
#define PSGSFXPlayLoop(a,b) PSGSFXPlayLoop_callee(a,b)


extern void __LIB__ PSGSFXCancelLoop(void) __smallc;


extern void __LIB__ PSGSFXStop(void) __smallc;


extern unsigned char __LIB__ PSGSFXGetStatus(void) __smallc;



extern void __LIB__ PSGSilenceChannels(void) __smallc;


extern void __LIB__ PSGRestoreVolumes(void) __smallc;



extern void __LIB__ PSGFrame(void) __smallc;

extern void __LIB__ PSGSFXFrame(void) __smallc;


#endif
