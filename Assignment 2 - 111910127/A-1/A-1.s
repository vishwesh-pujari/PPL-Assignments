	.file	"A-1.c"
	.text
	.comm	_Z, 4, 2
	.def	___main;	.scl	2;	.type	32;	.endef
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
	pushl	%ebp
	movl	%esp, %ebp
	andl	$-16, %esp
	subl	$32, %esp
	call	___main
	movl	$6, 28(%esp)
	movl	$10, 24(%esp)
	movl	$20, 20(%esp)
	movl	24(%esp), %eax
	imull	20(%esp), %eax
	addl	$25, %eax
	movl	%eax, 16(%esp)
	movl	$6, 28(%esp)
	movl	_Z, %eax
	movl	%eax, 12(%esp)
	nop
	leave
	ret
	.ident	"GCC: (GNU) 9.2.0"
