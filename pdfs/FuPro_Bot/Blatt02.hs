module Blatt02 where

import Examples

-- Aufgabe 2.1 a)
{-
-- Lösung hier einfügen.
-}

-- Aufgabe 2.1 b)
{-
-- Lösung hier einfügen.
-}

-- Aufgabe 2.1 c)
{-
-- Lösung hier einfügen.
-}





-- Aufgabe 2.2 a)
f :: ?? -- Typ hier einfügen.
f = \e -> case e of
  -- Fallunterscheidung hier einfügen.

-- Aufgabe 2.2 b)
g :: ?? -- Typ hier einfügen.
g = \t -> case t of
  -- Fallunterscheidung hier einfügen.







-- Aufgabe 2.3 a)
ausdruckA x y z =  x + y + 5 * z
klammernA x y z = x + y + 5 * z -- Klammern hier setzen.
praefixA x y z  = undefined -- Präfixdarstellung hier einfügen.

--Aufgabe 2.3 b)
ausdruckB f g h x = f . g $ h $ f x
klammernB f g h x =  f . g $ h $ f x -- Klammern hier setzen.
praefixB f g h x  = undefined -- Präfixdarstellung hier einfügen.

--Aufgabe 2.3 c)
ausdruckC f = f 5 True 3
klammernC f = f 5 True 3 -- Klammern hier setzen.
praefixC f  = undefined -- Präfixdarstellung hier einfügen.






-- Aufgabe 2.4 a)
{- (||) schrittweise in einen Lambda-Ausdruck umformen.
-}

{-  False || True schrittwiese auswerten.
-}


--Aufgabe 2.4 b)
{- (.) schrittweise in einen Lambda-Ausdruck umformen.
-}

{-   h . h' schrittwiese auswerten.
-}
