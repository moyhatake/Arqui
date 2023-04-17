.data
.balign 4
message1: .asciz "Value of n: "
.balign 4
message2: .asciz "Result of the function evaluated with %d: %d\n"
.balign 4
message3: .asciz "%d exceeds the 32 bits result. Try with a number lower than 1861."
.balign 4 @ Format pattern for scanf
scan_pattern: .asciz "%d"
.balign 4 @ Where scanf will store the number read
number_read: .word 0
.balign 4
return: .word 0
.balign 4
return2: .word 0

.text
/* Sum function */
zum:    
    cmp r2, r0     @ compare r2 and r0 (number read)
    bgt end        @ branch if r2 > r0 to end
    mul r3, r2, r2 @ r3 <- r2*r2
    add r4, r4, r3 @ r4 <- r4 + r3
    add r2, r2, #1 @ r2 <- r2 + 1
    b zum

/* Printing function */
end:
    mov r0, r4           @ r0 <- r4
    mov r2, r0           @ r2 <- r0
    ldr r1, =number_read @ r1 <- &number_read
    ldr r1, [r1]         @ r1 <- *r1
    ldr r0, =message2    @ r0 <- &message2
    bl printf            @ call to printf
    ldr lr, =return      @ lr <- &return
    ldr lr, [lr]         @ lr <- *lr
    bx lr                @ return from main using lr
    
brk:
    ldr r8, =number_read @ r8 <- &number_read
    ldr r8, [r8]         @ r8 <- *r8
    ldr r0, =message3    @ r0 <- &message3
    bl printf            @ call to printf
    ldr lr, =return      @ lr <- &return
    ldr lr, [lr]         @ lr <- *lr
    bx lr                @ return from main using lr

.global main
main:
    mov r2, #1            @ r2 <- 1 (iterator)
    mov r3, #0            @ r3 <- 0 (squared)
    mov r4, #0            @ r4 <- 0 (result)
    ldr r1, =return       @ r1 <- &return
    str lr, [r1]          @ *r1 <- lr
    ldr r0, =message1     @ r0 <- &message1
    bl printf             @ call to printf
    ldr r8, =scan_pattern @ r8 <- &scan_pattern
    ldr r9, =number_read  @ r9 <- &number_read
    bl scanf              @ call to scanf
    ldr r8, =number_read  @ r8 <- &number_read
    ldr r8, [r8]          @ r8 <- *r8
    
    @cmp r8, #1860        @ compare r8 and 1860 (number read)
    @bgt brk              @ branch if r8 > 1860 to brk
    mov r0, r8		      @ r0 <- r8
    
    bl zum
    
/* External */
.global printf
.global scanf
