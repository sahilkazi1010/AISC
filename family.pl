% Gender facts
female(catherine).
female(sophia).
female(elizabeth).

% Anyone who is not female is considered male
male(X) :- \+ female(X).

% Parent facts
parent(james1, charles1).
parent(james1, elizabeth).
parent(charles1, catherine).
parent(charles1, james2).
parent(charles1, charles2).
parent(elizabeth, sophia).
parent(sophia, george).

% Rules
mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).

siblings(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

aunt(X, Y) :-
    female(X),
    parent(Z, Y),
    siblings(X, Z).

uncle(X, Y) :-
    male(X),
    parent(Z, Y),
    siblings(X, Z).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

cousins(X, Y) :-
    parent(A, X),
    parent(B, Y),
    siblings(A, B),
    X \= Y.



    cmd
    mother(X, catherine).
    aunt(X, george).
    uncle(X, george).
    grandparent(X, george).
