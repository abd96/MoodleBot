module Blatt05 where

-- Aufgabe 5.1 a)
{-
-- Lösung hier einfügen.
-}

-- Aufgabe 5.1 b)
{-
-- Lösung hier einfügen.
-}

-- Aufgabe 5.1 c)
{-
-- Lösung hier einfügen.
-}



-- Aufgabe 5.2 a)
odds :: [Int]
odds = undefined -- Durch Lösung ersetzen.

-- Aufgabe 5.2 b)
alternate :: [Int]
alternate = undefined -- Durch Lösung ersetzen.

-- Aufgabe 5.2 c)
solutions :: [(Int, Int, Int)]
solutions = undefined -- Durch Lösung ersetzen.




-- Funktion von Folie 53.
updRel :: Eq a => [(a,b)] -> a -> b -> [(a,b)]
updRel ((a,b):r) c d = if a == c then (a,d):r else (a,b):updRel r c d
updRel _ a b = [(a,b)]

-- Vorgabe
type ID = Int
type Bank = [(ID,Account)]
data Account = Account { balance :: Int, owner :: Client }
  deriving Show
data Client = Client
  { name :: String
  , surname :: String
  , address :: String
  } deriving Show


-- Aufgabe 5.3 a)
credit :: Int -> ID -> Bank -> Bank
credit = undefined -- Durch Lösung ersetzen.

-- Aufgabe 5.3 b)
debit :: Int -> ID -> Bank -> Bank
debit = undefined -- Durch Lösung ersetzen.

-- Aufgabe 5.3 c)
transfer :: Int -> ID -> ID -> Bank -> Bank
transfer  = undefined -- Durch Lösung ersetzen.