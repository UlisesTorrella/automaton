from automaton import Automaton

states = { "q0", "q1", "q2", "q3" }
alphabet = { "a", "b" }
initial_state = "q0"
final_states = {"q0","q2", "q1"}


## Precondition q in states and e in alphabet
def delta0(q, e):
    if q == "q0":
        if e == "a":
            return "q2"
        elif e == "b":
            return "q1"
    elif q == "q1":
        if e == "a":
            return "q3"
        elif e == "b":
            return "q0"
    elif q == "q2":
        if e == "a":
            return "q2"
        elif e == "b":
            return "q1"
    elif q == "q3":
        if e == "a":
            return "q3"
        elif e == "b":
            return "q3"

automata = Automaton(states, alphabet, delta0, initial_state, final_states)

print(automata.execute("q0","a"))

print (automata.get_language(5))
