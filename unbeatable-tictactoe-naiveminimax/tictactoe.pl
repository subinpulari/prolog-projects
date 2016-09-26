% Basic Tic-Tac-Toe Code using MinMax in Prolog interfaced with Python. Subin Pulari (c) 2016
% Represent Board Positions like:
% 	[0,2]	[1,2]	[2,2]
%	[0,1]	[1,1]	[2,1]
%	[0,0]	[1,0]	[2,0]
% Board State - Bs is a list like [x/0/2,x/1/1,o/0/0]

% wins(Player,Bs,Depth,val) - val = 10-Depth if x can win now.
position(_/0/0).
position(_/0/1).
position(_/1/0).
position(_/1/1).
position(_/0/2).
position(_/2/0).
position(_/2/2).
position(_/2/1).
position(_/1/2).

%Only if win x and win y fails
drawn(Bs):-
	number(Bs,9).
	
wins(Bs,Player):-
	diagonal_1_win(Player,Bs),!;
	diagonal_2_win(Player,Bs),!;
	horizontal_win(Player,Bs),!;
	vertical_win(Player,Bs),!.

member(X,[X|List]).
member(X,[Y|List]):-
	member(X,List).

number([],0).
number([X|List],N):-
	number(List,N1),
	N is N1+1.

not(Goal):-
  Goal,!, fail
  ; 
  true.
 

%Top Left to Botton Right Diagonal
diagonal_1_win(Player,Bs):-
	member(Player/0/2,Bs),
	member(Player/1/1,Bs),
	member(Player/2/0,Bs).

%Top Right to Botton Left Diagonal
diagonal_2_win(Player,Bs):-
	member(Player/2/2,Bs),
	member(Player/1/1,Bs),
	member(Player/0/0,Bs).

%Horizontal win
horizontal_win(Player,Bs):-
	member(Player/0/0,Bs),member(Player/1/0,Bs),member(Player/2/0,Bs),!;
	member(Player/0/1,Bs),member(Player/1/1,Bs),member(Player/2/1,Bs),!;
	member(Player/0/2,Bs),member(Player/1/2,Bs),member(Player/2/2,Bs),!.

%Vertical win
vertical_win(Player,Bs):-
	member(Player/0/2,Bs),member(Player/0/1,Bs),member(Player/0/0,Bs),!;
	member(Player/1/0,Bs),member(Player/1/1,Bs),member(Player/1/2,Bs),!;
	member(Player/2/0,Bs),member(Player/2/1,Bs),member(Player/2/2,Bs),!.


list_of_moves(Bs,Player,Move_list):-
	bagof(Player/X/Y,(position(Player/X/Y),not(member(_/X/Y,Bs))),Move_list).

get_other_player(x,o).
get_other_player(o,x).

minimax(Bs,_,null,10):-
	wins(Bs,x),!.

minimax(Bs,_,null,-10):-
	wins(Bs,o),!.

minimax(Bs,_,null,-5):-
	drawn(Bs),!.

minimax(Bs,Turn,Move,Val):-
	list_of_moves(Bs,Turn,Move_List),
	choose_best(Bs,Turn,Move_List,Move,Val).

choose_best(Bs,Turn,[Move],Move,Val):-
	get_other_player(Turn,Player2),	
	minimax([Move|Bs],Player2,_,Val).
	
choose_best(Bs,Turn,[Move|Rest_List],Move1,Val1):-
	get_other_player(Turn,Player2),	
	minimax([Move|Bs],Player2,_,Val),
	choose_best(Bs,Turn,Rest_List,Move3,Val3),
	better_move(Turn,Move,Val,Move3,Val3,Move1,Val1).

better_move(Turn,Move1,Val1,Move2,Val2,Move1,Val1):-
	Turn=x,Val1>Val2,!
	;
	Turn=o,Val1<Val2,!.

better_move(Turn,Move1,Val1,Move2,Val2,Move2,Val2).

get_next_move(Bs,Move,Val):-
	minimax(Bs,x,Move,Val),!.




