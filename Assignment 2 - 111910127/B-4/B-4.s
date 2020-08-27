	.file	"B-4.c"
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
	movl	12(%esp), %edx
	movl	8(%esp), %eax
	addl	%eax, %edx
	movl	4(%esp), %eax
	leal	(%edx,%eax), %ecx
	movl	8(%esp), %edx
	movl	12(%esp), %eax
	addl	%edx, %eax
	imull	%ecx, %eax
	movl	%eax, 4(%esp)
	movl	4(%esp), %eax
	leave
	ret
	.ident	"GCC: (GNU) 9.2.0"
