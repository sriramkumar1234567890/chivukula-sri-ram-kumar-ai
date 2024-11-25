person(seetha,"05-11-2005").
person(navya,"28-04-2004").
person(kavya,"05-09-2005").
get_dob(Name,DOB):-
person(Name,DOB).
get_name(DOB,Name):-
person(Name,DOB).
