module Blatt08 where

import Coalg (Bintree(..),leaf,btree1,btree4)

-- Vorgegebene Datentypen dürfen nicht geändert werden.
data Nat = Zero | Succ Nat
data PosNat = One | Succ' PosNat
data Int' = Zero' | Plus PosNat | Minus PosNat
data Edge = Links | Rechts deriving Show
type Node = [Edge]

-- Aufgabe 8.1 a)
-- Lösung hier einfügen.

-- Aufgabe 8.1 b)
-- Lösung hier einfügen.




-- Aufgabe 8.2 a)
instance Enum Int' where
  toEnum = undefined -- Durch Lösung ersetzen.
  fromEnum = undefined -- Durch Lösung ersetzen.

-- Aufgabe 8.2 b)
instance Num Int' where
  fromInteger = undefined -- Durch Lösung ersetzen.
  negate = undefined -- Durch Lösung ersetzen.
  signum = undefined -- Durch Lösung ersetzen.
  abs = undefined -- Durch Lösung ersetzen.
  (+) = undefined -- Durch Lösung ersetzen.
  (*) = undefined -- Durch Lösung ersetzen.

instance Eq Int' where
  (==) = undefined -- Durch Lösung ersetzen.

instance Ord Int' where
  (<=) = undefined -- Durch Lösung ersetzen.

instance Show Int' where
  show = undefined -- Durch Lösung ersetzen.

-- Aufgabe 8.2 c)
-- Mögliche Lösung von Übungsblatt 5.
-- Kann durch die eigene Lösung ersetzt werden.
-- Ändern Sie den Typ in [(Int',Int',Int')].
solutions :: [(Int,Int,Int)]
solutions = [ (x,y,z) | z <- [0..] , x <- [0..z] , y <- [0..z]
            , 5*x + 3*y^2 + 10 == z ]




-- Aufgabe 8.3 a)
sizeBintree :: Bintree a -> Int
sizeBintree = undefined -- Durch Lösung ersetzen.

-- Aufgabe 8.3 b)
zipBintree :: Bintree a -> Bintree b -> Bintree (a,b)
zipBintree = undefined -- Durch Lösung ersetzen.

-- Aufgabe 8.3 c)
getSubbintree :: Bintree a -> Node -> Maybe (Bintree a)
getSubbintree = undefined -- Durch Lösung ersetzen.
