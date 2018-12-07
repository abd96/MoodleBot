import Expr (Exp(..))

-- Singatur
data List a list = List        -- data [a] where
  { nil :: list                --   []  :: [a]
  , cons :: a -> list -> list  --   (:) :: a -> [a] -> [a]
  }

data Arith x exp = Arith       -- data Exp x where
  { con :: Int -> exp          --   Con :: Int -> Exp x
  , var :: x -> exp            --   Var :: x -> Exp x
  , sum_ :: [exp] -> exp       --   Sum :: [Exp x] -> Exp x
  , prod :: [exp] -> exp       --   Prod :: [Exp x] -> Exp x
  , sub :: exp -> exp -> exp   --   (:-) :: Exp x -> Exp x -> Exp x
  , div_ :: exp -> exp -> exp  --   (:/) :: Exp x -> Exp x -> Exp x
  , scal :: Int -> exp -> exp  --   (:*) :: Int -> Exp x -> Exp x
  , expo :: exp -> Int -> exp  --   (:^) :: Exp x -> Int -> Exp x
  }


-- Faltung
foldList :: List a list -> [a] -> list
foldList alg []     = nil alg
foldList alg (a:as) = cons alg a $ foldList alg as

foldArith :: Arith x exp -> Exp x -> exp
foldArith alg exp = case exp of
  Con i -> con alg i
  Var x -> var alg x
  Sum es -> sum_ alg $ map (foldArith alg) es
  Prod es -> prod alg $ map (foldArith alg) es
  e :- e' -> sub alg (foldArith alg e) (foldArith alg e')
  e :/ e' -> div_ alg (foldArith alg e) (foldArith alg e')
  i :* e -> scal alg i $ foldArith alg e
  e :^ i -> expo alg (foldArith alg e) i


-- Algebren
listT :: List a [a] -- Termalgebra
listT = List { nil = [], cons = (:) }

intAlg :: List Int Int
intAlg = List { nil = 0, cons = (+)}

id' = foldList listT
sum' = foldList intAlg
and' = foldList List{nil=True, cons=(&&)}

type Store x = x -> Int

evalAlg :: Arith x (Store x -> Int)
evalAlg = Arith
  { con = \i -> \st -> i
  , var = \x -> \st -> st x
  , sum_ = \bs -> \st -> sum $ map (\b -> b st) bs
  , prod = \bs -> \st -> product $ map  (\b -> b st) bs
  , sub = \b b' -> \st -> b st - b' st
  , div_ = \b b' -> \st -> b st `div` b' st
  , scal = \i b -> \st -> i * b st
  , expo = \b i -> \st -> b st ^ i
  }


-- Beispiele
-- sum :: [Int] -> Int
-- sum []     = 0
-- sum (x:xs) = x + sum xs

ls :: [Int]
ls = 1:2:3:[]

exp1 :: Exp String
exp1 = Sum [Var"x":^4, 5:*(Var"x":^3), 11:*(Var"x":^2), Con 222]

eval :: Store x -> Exp x -> Int
eval st exp = foldArith evalAlg exp st



class Add a where
  add :: a -> a -> a
  add = const

instance Add Int where
  add = (+)

instance Add Bool where
  add = (||)

instance Add Char