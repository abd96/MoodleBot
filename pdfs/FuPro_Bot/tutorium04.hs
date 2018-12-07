import Prelude hiding (map,zip)

map :: (a -> b) -> [a] -> [b]
map f = \ls -> case ls of
  (a:as) -> f a : map f as
  []     -> []

zip :: [a] -> [b] -> [(a,b)]
zip (a:as) (b:bs) = (a,b) : zip as bs
zip _ _ = []