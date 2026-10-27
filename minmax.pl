min(X, Y, X) :- X =< Y.
min(X, Y, Y) :- X > Y.

max(X, Y, X) :- X >= Y.
max(X, Y, Y) :- X < Y.

cmd
min(10,20,M).
max(10,20,M).
