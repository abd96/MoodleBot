{- LAYOUT
module Layout where

f b = case b of
  True -> 1
  False -> 0

g :: Int -> Int
g x = let
    y :: Int
    y = 3 in x + y

h x = x + y where y :: Int; y = 3

m = do x <- Just 3
       y <- Just 4
       return (x+y)
- LAYOUT -}









{- GENERIERT/IMPLIZIT
module Layout where

{f b = case b of
  {True -> 1
  ;False -> 0

};g :: Int -> Int
;g x = let
  {y :: Int
  ;y = 3 }in x + y

;h x = x + y where {y :: Int; y = 3

};m = do {x <- Just 3
        ;y <- Just 4
        ;return (x+y)
}
- GENERIERT/IMPLIZIT -}




{- EXPLIZIT -}
module Layout where {
  f b = case b of {
    True -> 1;
    False -> 0
  };

  g :: Int -> Int;
  g x = let {
          y :: Int;
          y = 3
      } in x + y;

  h x = x + y where {y :: Int; y = 3};

  m = do {
    x <- Just 3;
    y <- Just 4;
    return (x+y)
  }
}
{- EXPLIZIT -}





{- EINZEILER
module Layout where {  f b = case b of {    True -> 1;    False -> 0  };  g :: Int -> Int;  g x = let {          y :: Int;          y = 3      } in x + y;  h x = x + y where {y :: Int; y = 3};  m = do {    x <- Just 3;    y <- Just 4;    return (x+y)  }}
- EINZEILER -}