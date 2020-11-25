def or_gate(a, b): # a+b
	return a + b - a * b

def and_gate(a, b): # a.b
	return a * b

def not_gate(a): # a`
	return 1 - a

def xor_gate(a, b): # a`b + ab`
	return or_gate(and_gate(not_gate(a), b), and_gate(a, not_gate(b)))
