.org $080D
.segment "ONCE"
.segment "CODE"

.feature c_comments
.linecont +

   jmp main

.ifndef UNITTESTING_INC
.include "inc/unittesting.inc"
.endif

.import file_open, file_close, file_read

.proc main      
   jsr load_test
   rts
.endproc

filename:
Lstr "testload"

bad_filename:
Lstr "non_exist"

.proc load_test
   prints "file i/o test - load to banked ram", CHR_NL

   LoadW R0, bad_filename
   jsr file_open
   bcc bad_opened_ok
   prints "file open error on bad file - this was expected",CHR_NL
   jsr file_close
   bra open_real_file
bad_opened_ok:
   prints "bad file opened?"
status_and_exit:   
   prints " - something is wrong!",CHR_NL
   jmp exit
open_real_file:
   LoadW R0, filename
   jsr file_open
   bcc opened_ok
   prints "file open error on good file?"
   jmp status_and_exit
opened_ok:   
   LoadW R0, $A000      ; load to banked memory
   LoadW R1, $FF01      ; bank 1, load as much as possible
   LoadW R2, $0000      ; as much as possible
   jsr file_read
   bcc worked
   prints "macptr not happy?"
   bra exit
worked:
   prints "macptr is happy :-) - all loaded"
exit:
   jsr file_close
   rts
.endproc



