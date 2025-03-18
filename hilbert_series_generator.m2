
-- ideal computation times out when n=4
-- Hilbert series computation times out when n=7

-- for n from 1 to 7 do (

n = 2
R = QQ[x_1..x_(n^2)];
X = genericMatrix(R, x_1, n, n);
<< "n = " << n << endl;
-- calculate the ideal using the traces
L = apply(1..n, i -> trace(X^i));
idealTrace = ideal(L);


print("ideal of trace")
print(idealTrace);
print("")
print("")

-- print("hilbert series of ideal of trace")
-- print(hilbertSeries(idealTrace));
-- print("")
-- print("")


print("hilbert series of ideal of trace order 10");
print(hilbertSeries(idealTrace, Order => 100));
print("");
print("");

-- radTrace = radical(idealTrace);

-- print("radical of ideal of trace")
-- print(radTrace);
-- print("")
-- print("")


-- print("is radical = ideal")
-- print(radTrace == idealTrace)
-- print("")
-- print("")


-- -- calculate the ideal using X^n
-- idealX = ideal(X^n);
-- print("ideal of X^n")
-- print(idealX);
-- print("")
-- print("")


-- radX = radical(idealX);
-- print("is radical equal")
-- print(radX);
-- print(radX == radTrace); -- should always be true

-- );