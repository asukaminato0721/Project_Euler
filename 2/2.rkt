#lang racket
(require math/number-theory)
(foldl + 0 (filter  
            (lambda (x) (and (even? x)(< x 4000000)))
            (map fibonacci (range 35))))
