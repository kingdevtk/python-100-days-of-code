us_states = ['Delaware', 'Pennsylvania', 'New York', 'Connecticut']

#changing the name of a state in the list
us_states[1] = 'pennsatucky'

#display the updated state in the list
print(us_states[1])

#adding another state to the list
us_states.append('New Jersey')

#adding another list to the list, adding a list of states
us_states.extend(['Georgia', 'Virginia', 'Alaska', 'Colorado'])

#display the whole list
print(us_states)
