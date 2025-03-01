.ifndef REGS_INC
REGS_INC = 1

.feature c_comments 		; we always want to be able to use /* .... */

; Zero page scratch area
ZEROPAGE_SCRATCH     = $22
ZEROPAGE_SCRATCH_END = $80

BANK 		= $00		; ram bank
ROM_BANK 	= $01		; rom bank

KERNAL_VERSION = $FF80	; address of the kernal version

;r0-r5: 	argument registers
;r11-r15: 	scratch registers

; Zero page pseudo registers
r0		= $02
r0L		= $02
r0H		= $03
r1		= $04
r1L		= $04
r1H		= $05
r2		= $06
r2L		= $06
r2H		= $07
r3		= $08
r3L		= $08
r3H		= $09
r4		= $0a
r4L		= $0a
r4H		= $0b
r5		= $0c
r5L		= $0c
r5H		= $0d
r6		= $0e
r6L		= $0e
r6H		= $0f
r7		= $10
r7L		= $10
r7H		= $11
r8		= $12
r8L		= $12
r8H		= $13
r9		= $14
r9L		= $14
r9H		= $15
r10		= $16
r10L	= $16
r10H	= $17
r11		= $18
r11L	= $18
r11H	= $19
r12		= $1a
r12L	= $1a
r12H	= $1b
r13		= $1c
r13L	= $1c
r13H	= $1d
r14		= $1e
r14L	= $1e
r14H	= $1f
r15		= $20
r15L	= $20
r15H	= $21

R0		= $02
R0L		= $02
R0H		= $03
R1		= $04
R1L		= $04
R1H		= $05
R2		= $06
R2L		= $06
R2H		= $07
R3		= $08
R3L		= $08
R3H		= $09
R4		= $0A
R4L		= $0A
R4H		= $0B
R5		= $0C
R5L		= $0C
R5H		= $0D
R6		= $0E
R6L		= $0E
R6H		= $0F
R7		= $10
R7L		= $10
R7H		= $11
R8		= $12
R8L		= $12
R8H		= $13
R9		= $14
R9L		= $14
R9H		= $15
R10		= $16
R10L	= $16
R10H	= $17
R11		= $18
R11L	= $18
R11H	= $19
R12		= $1A
R12L	= $1A
R12H	= $1B
R13		= $1C
R13L	= $1C
R13H	= $1D
R14		= $1E
R14L	= $1E
R14H	= $1F
R15		= $20
R15L	= $20
R15H	= $21

.endif