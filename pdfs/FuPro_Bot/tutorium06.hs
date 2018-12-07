data Nat = Zero | Succ Nat deriving Show

eins :: Nat
eins = Succ Zero

f :: Nat -> String
f Zero     = "0"
f (Succ n) = f n ++ "+1"

















--  data [a] = [] | (:) { head :: a, tail :: [a]}

data Conat = Conat { prd :: Maybe Conat} deriving Show

eins' = Conat { prd = Just (Conat { prd = Nothing }) }

f' :: Conat -> String
f' n = case prd n of
  Nothing -> "0"
  Just n' -> f' n' ++ "+1"

data Stream a = (:<) { hd :: a, tl :: Stream a }

blink = 0 :< 1 :< blink

infixr 5 :<
instance Show a => Show (Stream a) where
  show st = '[' : show' 10 st ++ "...]" where
    show' 0 _ = ""
    show' n (a:<st) = show a ++ "," ++ show' (n-1) st








newtype Size = Size Int deriving Show

zwei :: Size
zwei = Size 2


newSize :: Int -> Size
newSize i | i >= 0 = Size i