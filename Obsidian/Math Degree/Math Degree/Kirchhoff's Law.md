(From [[Applications of Differential Equations]])
Passive Electrical Circuits consists of the following basic elements.
- An Electromotive force (emf) - $E$, measured in Volts. This is an energy source such as a battery or generator
- A resistor with resistance $R$ measured in ohms ($\Omega$). This uses energy, light bulb etc.
- A inductor having inductance $L$ measured in Henry. This is an element which opposes change in current such as a coil.
- A capacitor having capacitance $C$ measured in Farads.
- A key or switch: Turns the device on or off.

Other variables associated with circuits are: 
- Charge $Q$, measured in coulombs.
- Current flow, $I$, measured in amperes, equal to $\frac{dQ}{dt}$.

## Experimental Relationships
- The voltage drop through a resistor is proportional to the current passing through the resistor. (Ohm's Law) $$E_{r}=RI$$
- The voltage drop across an inductor is proportional to the the rate of change of current: $$E_{L}=L\frac{dI}{dt} $$
- The voltage drop across a capacitor is proportional to the charge stored, $$
E_{c}=\frac{1}{C}Q$$where $C$ is the capacitance.
## The law
The law states simply that the total energy used is the sum of the voltage drop.

## Resistor-Inductor Circuit
For a circuit with a resistor and an inductor connected in series, 
$$E=E_{R}+E_{L}$$
$$E=RI+L \frac{dI}{dt}$$
This is a linear DE given by:
$$\begin{cases}
E=RI+L \frac{dI}{dt}\\
I(t_{0})=I_{0}
\end{cases}$$
## Resistor-Capacitor Circuit
For a circuit with a resistor and capacitor connected in series, 
$$E=E_{C}+E_{R}$$
$$E=\frac{1}{C}Q+R \frac{dQ}{dt}$$
This satisfies a linear FODE:
$$\begin{cases}
E=R \frac{dQ}{dt} + \frac{1}{C}Q\\ \\
Q(t_{0})=Q_{0}
\end{cases}$$
