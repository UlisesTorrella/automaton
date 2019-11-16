from automaton import Automaton

states = { "q0", "q1", "q2" }
alphabet = { "a", "b" }
initial_state = "q0"
final_states = {"q0"}


## Precondition q in states and e in alphabet
def delta0(q, e):
    res = set()
    if q == "q0":
        if e == "b":
            res = {"q1","q2"}
    elif q == "q1":
        if e == "a":
            res = {"q2"}
        elif e == "b":
            res = {"q0", "q1"}
    elif q == "q2":
        if e == "a":
            res = {"q0"}
    return res

automata = Automaton(states, alphabet, delta0, initial_state, final_states)

print(automata.execute({"q0"},"b"))

print (automata.get_language(5))
