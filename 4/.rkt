#lang racket
(require srfi/13)
(define (=? a)(string=? (string-reverse (~a a)) (~a a)))
(foldl (lambda (a b) (max a b))
       1
       (filter =? (map (lambda (a) (* (car a) (cadr a)))
                       (cartesian-product (range 999 100 -1) (range 999 100 -1)))))
