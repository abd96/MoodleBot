import Examples ((&))
import Prelude

data Point = Point
  { x :: Double
  , y :: Double
  } deriving Show

pt :: Point
pt = Point { y = 5, x = 3}

data TwoElems = One | Two deriving Show
data Wrap = WrapInt Int | WrapBool Bool deriving Show

{-
x :: Int
y :: Int
(x,y) :: (Int,Int)
3 :: Int
Just 3 :: Maybe Int
\(x,y) -> Just 3 :: (Int,Int) -> Maybe Int
(3,3) :: (Int,Int)
(\(x,y) -> Just 3)(3,3) :: Maybe Int
-}