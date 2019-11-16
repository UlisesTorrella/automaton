from automaton import Automaton

states = { "q0", "q1", "q2", "q3" }
alphabet = { "a", "b" }
initial_state = "q0"
final_states = {"q0","q2", "q1"}


## Precondition q in states and e in alphabet
def delta0(q, e):
    res = set()
    if q == "q0":
        if e == "a":
            res = {"q2"}
        elif e == "b":
            res = {"q1"}
    elif q == "q1":
        if e == "a":
            res = {"q3"}
        elif e == "b":
            res = {"q0"}
    elif q == "q2":
        if e == "a":
            res = {"q2"}
        elif e == "b":
            res = {"q1"}
    elif q == "q3":
        if e == "a":
            res = {"q3"}
        elif e == "b":
            res = {"q3"}
    return res

automata = Automaton(states, alphabet, delta0, initial_state, final_states)

print(automata.execute({"q0"},"a"))

print (automata.get_anti_language(5))
