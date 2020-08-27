	.file	"A-4.c"
	.text
	.def	___main;	.scl	2;	.type	32;	.endef
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
	pushl	%ebp
	movl	%esp, %ebp
	andl	$-16, %esp
	subl	$32, %esp
	call	___main
	movl	$1, (%esp)
	movl	$2, 4(%esp)
	movl	$3, 8(%esp)
	movl	$0, 28(%esp)
	jmp	L2
L3:
	movl	28(%esp), %eax
	movl	(%esp,%eax,4), %edx
	movl	28(%esp), %eax
	movl	%edx, 12(%esp,%eax,4)
	addl	$1, 28(%esp)
L2:
	cmpl	$2, 28(%esp)
	jle	L3
	leal	12(%esp), %eax
	movl	%eax, 24(%esp)
	movl	24(%esp), %eax
	addl	$8, %eax
	movl	$5, (%eax)
	movl	$0, %eax
	leave
	ret
	.ident	"GCC: (GNU) 9.2.0"
