syms s

zetas = [0:0.1:1];
n = length(zetas);
for i = 1:n
    zeta = zetas(i);
    G = 1/(s^2 + 2*zeta*s + 1); % Transfer function
    U = 1/s; % Step input
    
    hold on
    y = ilaplace(G*U);
    fplot(y, [0, 12]);
end
xlabel('t')
ylabel('y(t)')
