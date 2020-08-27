	.file	"B-3.c"
	.text
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC0:
	.ascii "%d%d\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
	pushl	%ebp
	movl	%esp, %ebp
	andl	$-16, %esp
	subl	$32, %esp
	call	___main
	movl	$4, 28(%esp)
	jmp	L2
L5:
	cmpl	$3, 28(%esp)
	jg	L3
	addl	$2, 24(%esp)
	jmp	L4
L3:
	sall	24(%esp)
L4:
	addl	$1, 28(%esp)
L2:
	cmpl	$99, 28(%esp)
	jle	L5
	movl	24(%esp), %eax
	movl	%eax, 8(%esp)
	movl	28(%esp), %eax
	movl	%eax, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	movl	$0, %eax
	leave
	ret
	.ident	"GCC: (GNU) 9.2.0"
	.def	_printf;	.scl	2;	.type	32;	.endef
