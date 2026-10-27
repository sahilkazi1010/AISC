% Facts
food(burger).
food(sandwich).
food(pizza).

lunch(sandwich).
dinner(pizza).

% Rule
meal(X) :- food(X).

cmd
food(X).
meal(burger).
meal(pizza).
meal(X).
