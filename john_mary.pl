% Facts
likes(mary, food).
likes(mary, wine).
likes(mary, john).
likes(joseph, joseph).

% Rules
likes(john, X) :- likes(mary, X).
likes(john, X) :- likes(X, wine).
likes(john, X) :- likes(X, X).



cmd
likes(john, X).
likes(X, wine).
likes(john, X), likes(mary, X).
