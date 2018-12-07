import Examples (Point(..))
import Prelude hiding (either)

fib = \n -> case n of
  n | n == 0-> 1
    | n == 1 -> 1
  n -> fib(n-1) + fib(n-2)
--  0 -> 1
--  1 -> 1

data Wrap = WrapInt Int | WrapBool Bool deriving Show

infix 5 :+
data P = (:+) Float Float deriving Show

t = Left (WrapInt 3)

g :: Either Wrap Bool -> String
g = \wrap -> case wrap of
  Left t -> show t
  Right b -> show b

either :: (a -> c) -> (b -> c) -> Either a b -> c
--either f _ (Left a)  = f a
--either _ g (Right b) = g b
either = \f' -> \g' -> \e -> case (f',g',e) of
  (f,_,Left a) -> f a
  (_,g,Right b) -> g b

f = either x succ
test1 = f $ Left $ Point 3 5
test2 = f $ Right 8