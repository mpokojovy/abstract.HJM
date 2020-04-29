% Copyright   : Michael Pokojovy & Valerii Maltsev (2020)
% Version     : 1.0
% Last edited : 04/19/2020
% License     : Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
%               https://creativecommons.org/licenses/by-sa/4.0/

function sol = Merton_fwd_map(T_grid, y0, mu, sigma, n_rep)
    dt = T_grid(2) - T_grid(1);

    sol = zeros(length(T_grid), n_rep);
    
    for j = 1:n_rep
        dW = [0 randn(1, length(T_grid) - 1)*sqrt(dt)];
        
        sol(:, j) = y0 + mu*cumsum([0 dt*ones(1, length(T_grid) - 1)]) ...
                       + sigma*cumsum(dW);
    end
end