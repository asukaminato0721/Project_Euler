Table[{t, x /. FindInstance[{x^2 - t y^2 == 1, x > 0, y > 0}, {x, y}, Integers]}, {t, 1, 1000}] /. {_, x} :> Nothing // Map[Flatten] // MaximalBy[Last]
