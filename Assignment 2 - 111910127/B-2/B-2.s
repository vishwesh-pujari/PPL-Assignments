	.file	"B-2.c"
	.text
	.comm	_N, 4, 2
	.def	___main;	.scl	2;	.type	32;	.endef
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
	pushl	%ebp
	movl	%esp, %ebp
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$10, 8(%esp)
	movl	$0, 12(%esp)
	jmp	L2
L3:
	movl	_N, %eax
	addl	%eax, 8(%esp)
	addl	$1, 12(%esp)
L2:
	cmpl	$3, 12(%esp)
	jle	L3
	movl	8(%esp), %eax
	leave
	ret
	.ident	"GCC: (GNU) 9.2.0"
