from signal_ICT_Shivang_92510133024 import unitary_signal as us, trigonometric_signal as ts, operations as op

# Generate signals
n, step = us.unit_step(20)
n, impulse = us.unit_impulse(20)
ramp = us.ramp_signal(20)
t, sine = ts.sine(A=2, f=5, length=100)
t, cosine = ts.cosine(A=2, f=5, length=100)
expo = ts.exponential_signal(A=1, a=0.1, t=t)


# Operations
add_result = op.signal_addition(sine, cosine)
mul_result = op.signal_multiplication(sine, cosine)
shift_result = op.time_shift(sine, 5)
scale_result = op.time_scale(sine, 2)  

print("All signals generated and plots saved in 'plots/' folder.")