Cho DEFINITIONS IMPLICIT TAGS ::= 

BEGIN

ChoCon ::=  CHOICE 
{
  nested Cho2,	
  bool0 [0] BOOLEAN,
  bool1 [1] BOOLEAN,
  int2  [2] INTEGER
}

ChoExp ::=  CHOICE 
{
  int10  [APPLICATION 10] EXPLICIT INTEGER {first(1),last(31)},
  bool11 [APPLICATION 11] EXPLICIT BOOLEAN,
  enum12 [APPLICATION 12] EXPLICIT ENUMERATED {one(1),two(2),three(3)}
}

Cho2 ::= CHOICE
{
  i INTEGER,
  b BOOLEAN
}


END
