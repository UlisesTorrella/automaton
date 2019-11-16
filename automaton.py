class Automaton:
    states = {}
    sigma  = {}
    initial_state = ""
    final_states  = {}

## delta should return a set of states
    def __init__(self, states, sigma, delta, initial_state, final_states):
        if final_states.issubset(states) and initial_state in states:
            self.states = states
            self.sigma  = sigma
            self.delta  = delta
            self.initial_state = initial_state
            self.final_states  = final_states
        else:
            print("something's wrong... I can feel it")

    def execute(self, q, e):
        assert q.issubset(self.states) and e in self.sigma
        clausura = set()
        for state in q:
            d = self.delta(state, e)
            clausura =clausura.union(d)
        return clausura

    def run(self, word):
        current_state = {self.initial_state}
        for letter in word:
            assert letter in self.sigma, "Unknown letter for sigma"
            #print current_state
            current_state = self.execute(current_state, letter)
        return not current_state.isdisjoint(self.final_states)

    def get_language(self, lenght):
        sigma_list = list(self.sigma)
        size_of_alphabet = len(sigma_list)
        possible_words = size_of_alphabet**lenght
        sigmaS = [""]*(possible_words+1)

        language = set()

        for i in range(possible_words):
            sigmaS[i] = sigmaS[i].join([sigma_list[(i/(size_of_alphabet**j))%size_of_alphabet] for j in range(0, lenght)])
            if self.run(sigmaS[i]):
                language.add(sigmaS[i])
        sigmaS[possible_words] = ""
        if self.run(sigmaS[possible_words]):
            language.add(sigmaS[possible_words])
        return language

    def get_anti_language(self, lenght):
        sigma_list = list(self.sigma)
        size_of_alphabet = len(sigma_list)
        possible_words = size_of_alphabet**lenght
        sigmaS = [""]*(possible_words+1)

        anti_language = set()

        for i in range(possible_words):
            sigmaS[i] = sigmaS[i].join([sigma_list[(i/(size_of_alphabet**j))%size_of_alphabet] for j in range(0, lenght)])
            if not self.run(sigmaS[i]):
                anti_language.add(sigmaS[i])
        sigmaS[possible_words] = ""
        if self.run(sigmaS[possible_words]):
            anti_language.add(sigmaS[possible_words])
        return anti_language
