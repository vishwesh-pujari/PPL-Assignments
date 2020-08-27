
;; Function main (main, funcdef_no=0, decl_uid=1500, cgraph_uid=1, symbol_order=1)

main ()
{
  int a;
  int i;
  int D.1508;

  a = 10;
  i = 0;
  goto <D.1505>;
  <D.1504>:
  N.0_1 = N;
  a = a + N.0_1;
  i = i + 1;
  <D.1505>:
  if (i <= 3) goto <D.1504>; else goto <D.1506>;
  <D.1506>:
  D.1508 = a;
  goto <D.1509>;
  D.1508 = 0;
  goto <D.1509>;
  <D.1509>:
  return D.1508;
}


