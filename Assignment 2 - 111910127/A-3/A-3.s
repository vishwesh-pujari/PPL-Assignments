	.file	"A-3.c"
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
	movl	$0, 12(%esp)
	jmp	L2
L3:
	sall	12(%esp)
L2:
	cmpl	$99, 12(%esp)
	jle	L3
	movl	$0, 8(%esp)
	jmp	L4
L7:
	movl	$0, 4(%esp)
	jmp	L5
L6:
	movl	8(%esp), %eax
	imull	4(%esp), %eax
	addl	%eax, 12(%esp)
	addl	$1, 4(%esp)
L5:
	cmpl	$49, 4(%esp)
	jle	L6
	addl	$1, 8(%esp)
L4:
	cmpl	$24, 8(%esp)
	jle	L7
	movl	$0, %eax
	leave
	ret
	.ident	"GCC: (GNU) 9.2.0"
