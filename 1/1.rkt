#lang racket
(foldl + 0 (filter
            (lambda (x) ( or (equal? (modulo x 3) 0) (equal? (modulo x 5) 0)))
            (range 1000)))
