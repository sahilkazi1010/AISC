% Facts: Students study subjects
studies(amol, physics).
studies(omkar, physics).
studies(javed, chemistry).
studies(ashwin, mathematics).

% Facts: Professors teach subjects
teaches(karthik, physics).
teaches(chahal, chemistry).
teaches(jasprit, mathematics).
teaches(chahel, biology).

% Rules
professor(X, Y) :- teaches(X, Y).
student(X, Y) :- studies(X, Y).

cmd
studies(amol, X).
teaches(chahal, X).
studies(X, physics).
