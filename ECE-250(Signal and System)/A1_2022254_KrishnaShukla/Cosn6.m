n = -100:100; 
y = cos(n / 6);
a=1;
subplot(2, 1, 1);
stem(n, y);
a=1;
xlabel('n');
ylabel('y[n]');
a=1;
title('Sequence y[n] = cos[n/6]');
disp(['Fundamental Frequency does not exist ']);