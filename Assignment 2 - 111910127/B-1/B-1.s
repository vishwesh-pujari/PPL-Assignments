	.file	"B-1.c"
	.text
	.globl	_AddTwo
	.def	_AddTwo;	.scl	2;	.type	32;	.endef
_AddTwo:
	pushl	%ebp
	movl	%esp, %ebp
	addl	$2, 8(%ebp)
	movl	8(%ebp), %eax
	popl	%ebp
	ret
	.def	___main;	.scl	2;	.type	32;	.endef
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
	pushl	%ebp
	movl	%esp, %ebp
	andl	$-16, %esp
	subl	$32, %esp
	call	___main
	movl	$3, 28(%esp)
	movl	28(%esp), %eax
	movl	%eax, (%esp)
	call	_AddTwo
	movl	%eax, 28(%esp)
	movl	28(%esp), %eax
	leave
	ret
	.ident	"GCC: (GNU) 9.2.0"
