; We follow the MSX naming convention, so confusingly this is VDP mode 0 - 32x24

SECTION code_video_vdp

PUBLIC  __vdp_mode1


; VDP map definitions
defc    COLOUR_TABLE      = $2000
defc    PATTERN_NAME      = $1800
defc    PATTERN_GENERATOR = $0000

defc    SPRITE_GENERATOR  = $3800
defc    SPRITE_ATTRIBUTE  = $1b00


defc    COLUMNS = 32


EXTERN  __tms9918_set_font
EXTERN  __tms9918_clear_vram
EXTERN  __tms9918_attribute
EXTERN  __tms9918_border
EXTERN  __tms9918_CAPS_MODE1
EXTERN  __tms9918_set_tables

EXTERN  VDPreg_Write
EXTERN  FILVRM


SECTION rodata_video_vdp


; Table adderesses
mode1_addresses:
    defb     COLUMNS ;columns
    defb     24      ;rows
    defb     64-1    ;Graphics w
    defb     48-1    ;Graphic h
    defb     1       ;Sprite mode
    defb     __tms9918_CAPS_MODE1  ; Console capabilities

    defb    0         ;register 0:   -     -  -    -  -  - M2 EXTVID
    defb    $E0       ;register 1:   4/16K BL GINT M1 M3 - SI MAG
    defw    PATTERN_NAME
    defb    +((PATTERN_NAME >> 10) & 0x7F)
    defw    COLOUR_TABLE
    defb    +((COLOUR_TABLE >> 6) & 0xFF)       ;register 3
    defw    PATTERN_GENERATOR
    defb    +((PATTERN_GENERATOR >> 11) & 0x3F) ;register 4
    defw    SPRITE_ATTRIBUTE
    defw    SPRITE_GENERATOR
    defb    $ff             ;endmarker


SECTION code_video_vdp

; Initialises the display + returns terminal structure
; Entry: a = screenmode
__vdp_mode1:
    push    af
    call    __tms9918_clear_vram
    pop     af

    ld      hl, mode1_addresses
    call    __tms9918_set_tables

    ; Set the screen colour
    ld      a,(__tms9918_border)
    and     15
    ld      e,7
    call    VDPreg_Write    ; reg7  -  INK & PAPER-/BACKDROPCOL.


    ld      hl,PATTERN_NAME
    ld      bc,768
    ld      a,65
    call    FILVRM

    ; Set the colour for all characters
    ld      a,(__tms9918_attribute)
    ld      hl,COLOUR_TABLE
    ld      bc,32
    call    FILVRM

    ; Set the font
    jp      __tms9918_set_font