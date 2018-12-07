module Blatt07 where

import Expr
  ( Exp(..)
  , BExp(True_,False_,BVar,Or,And,Not,(:=),(:<=))
  , zero
  , one
  , mul
  , Store
  , Arith(..)
  , foldArith
  , evalAlg
  )


-- Aufgabe 1 a)
expr :: Exp String
expr = undefined -- Durch Lösung ersetzen.

-- Aufgabe 1 b)
solutions :: [(Int,Int,Int)]
{-
Es folgt die Beispiellösung von Übungsblatt 5.
Ersetzen Sie die Beispiellösung durch Ihre Lösung für Aufgabe 1 b).
-}
solutions = [ (x,y,z) | z <- [0..] , x <- [0..z] , y <- [0..z]
            , 5*x + 3*y^2 + 10 == z ]

-- Aufgabe 2 a)
bexpr1 :: BExp String
bexpr1 = undefined -- Durch Lösung ersetzen.

-- Aufgabe 2 b)
bexpr2 :: BExp String
bexpr2 = undefined -- Durch Lösung ersetzen.

-- Aufgabe 2 c)
bexpr3 :: BExp String
bexpr3 = undefined -- Durch Lösung ersetzen.


-- Vorgabe Aufgabe 3. Die Vorgabe darf nicht geändert werden.
data PosNat = One | Succ' PosNat deriving Show

toInt :: PosNat -> Int
toInt = foldPosNat intAlg

-- Aufgabe 3 a)
-- Lösung hier einfügen.

-- Aufgabe 3 b)
foldPosNat = undefined -- Durch Lösung ersetzen.

-- Aufgabe 3 c)
intAlg = undefined -- Durch Lösung ersetzen.


-- Vorgabe Aufgabe 4. Die Vorgabe darf nicht geändert werden.
type BStore x = x -> Bool

data BExpSig x exp bexp = BExpSig
  { true :: bexp
  , false :: bexp
  , bvar :: x -> bexp
  , bor :: [bexp] -> bexp
  , band :: [bexp] -> bexp
  , bnot :: bexp -> bexp
  , eq :: exp -> exp -> bexp
  , leq :: exp -> exp -> bexp
  }

foldBExp :: Arith x exp -> BExpSig x exp bexp -> BExp x -> bexp
foldBExp ealg balg bexp = case bexp of
  True_     -> true balg
  False_    -> false balg
  BVar x    -> bvar balg x
  Or bs     -> bor balg $ map foldB bs
  And bs    -> band balg $ map foldB bs
  Not b     -> bnot balg $ foldB b
  e1 := e2  -> eq balg (foldE e1) (foldE e2)
  e1 :<= e2 -> leq balg (foldE e1) (foldE e2)
  where
    foldB = foldBExp ealg balg
    foldE = foldArith ealg

evalB :: Store x -> BStore x -> BExp x -> Bool
evalB st bst bexpr = foldBExp evalAlg evalBAlg bexpr st bst

-- Aufgabe 4
evalBAlg :: BExpSig x (Store x -> Int) (Store x -> BStore x -> Bool)
evalBAlg = undefined -- Durch Lösung ersetzen.
