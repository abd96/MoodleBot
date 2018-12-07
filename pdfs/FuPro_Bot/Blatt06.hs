module Blatt06 where

-- Vorgegebene Datentypen dürfen nicht geändert werden.
data Nat = Zero | Succ Nat deriving Show
data PosNat = One | Succ' PosNat deriving Show
data Int' = Zero' | Plus PosNat | Minus PosNat deriving Show
data Colist a = Colist {split :: Maybe (a,Colist a)}
data Stream a = (:<) {hd :: a, tl :: Stream a}
infixr 5 :<
-- Angepasste Ausgabefunktionen für bessere Test- und Beispielausgaben.
instance Show a => Show (Colist a) where
  show (Colist Nothing) = "[]"
  show s = "Colist [" ++ tail (show' s) where
    show' s = case split s of
      Just (a,as) -> ',' : (show a ++ show' as)
      Nothing     -> "]"
instance Show a => Show (Stream a) where
  show s = "Stream [" ++ show' 8 s ++ "...]" where
    show' 0 _ = ""
    show' n (a:<as) = show a ++ "," ++ show' (n-1) as
-- Beispiele
nil :: Colist a
nil = Colist Nothing
co123 :: Colist Int
co123 = Colist (Just (1,Colist (Just (2,Colist (Just (3,Colist Nothing))))))
blink :: Stream Int
blink = 0:<1:<blink
nats :: Stream Int
nats = nats' 0 where
  nats' n = n :< nats' (n+1)




-- Aufgabe 6.1 a)
drei :: Nat
drei = undefined -- Durch Lösung ersetzen.

-- Aufgabe 6.1 b)
zwei :: PosNat
zwei = undefined -- Durch Lösung ersetzen.

-- Aufgabe 6.1 c)
mzwei :: Int'
mzwei = undefined -- Durch Lösung ersetzen.

-- Aufgabe 6.1 d)
data Rat
  = ?? -- Durch Lösung ersetzen.
  deriving Show

-- Aufgabe 6.1 e)
c :: Rat
c = undefined -- Durch Lösung ersetzen.

-- Aufgabe 6.1 f)
c' :: Rat
c' = undefined -- Durch Lösung ersetzen.



-- Aufgabe 6.2 a)
natTake :: Nat -> [a] -> [a]
natTake  = undefined -- Durch Lösung ersetzen.

-- Aufgabe 6.2 b)
natHoch :: (a -> a) -> Nat -> a -> a
natHoch = undefined -- Durch Lösung ersetzen.

-- Aufgabe 6.2 c)
colistConc :: Colist a -> Colist a -> Colist a
colistConc = undefined -- Durch Lösung ersetzen.

-- Aufgabe 6.2 d)
colistReverse :: Colist a -> Colist a
colistReverse = undefined -- Durch Lösung ersetzen.

-- Aufgabe 6.2 e)
stTakeWhile :: (a -> Bool) -> Stream a -> [a]
stTakeWhile  = undefined -- Durch Lösung ersetzen.

-- Aufgabe 6.2 f)
stZipWith :: (a -> b -> c) -> Stream a -> Stream b -> Stream c
stZipWith = undefined -- Durch Lösung ersetzen.
