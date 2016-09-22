good_standard(jeanluis).
expensive(jeanluis).
good_standard(francesco).
:- op(1200,fx,not).
not(P) :-
	P,!,fail
	;
	true.

reasonable(Restaurant) :-
	not(expensive(Restaurant)).
dosquares :-
	repeat,
	read(X),
	(X = stop,!
	;
	Y is X*X , write(Y),
	fail).
dosquaresonce :-
         read(X),
        ( X = stop, !
        ;
        Y is X*X , write(Y),
        fail).

