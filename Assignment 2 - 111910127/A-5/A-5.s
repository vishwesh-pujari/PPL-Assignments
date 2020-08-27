	.file	"A-5.c"
	.text
	.def	___main;	.scl	2;	.type	32;	.endef
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
	pushl	%ebp
	movl	%esp, %ebp
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$10, 4(%esp)
	movl	(%esp), %eax
	cmpl	4(%esp), %eax
	jle	L2
	movl	$3, 12(%esp)
	movl	$2, 8(%esp)
	jmp	L3
L2:
	movl	$2, 12(%esp)
	movl	$3, 8(%esp)
L3:
	movl	12(%esp), %edx
	movl	8(%esp), %eax
	addl	%edx, %eax
	movl	%eax, (%esp)
	movl	$0, %eax
	leave
	ret
	.ident	"GCC: (GNU) 9.2.0"
