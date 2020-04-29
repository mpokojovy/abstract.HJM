% Copyright   : Michael Pokojovy & Valerii Maltsev (2020)
% Version     : 1.0
% Last edited : 04/19/2020
% License     : Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
%               https://creativecommons.org/licenses/by-sa/4.0/

function [mu_hat, sigma_hat] = Merton_inv_map(T_grid, y_obs)
    dt = T_grid(2) - T_grid(1);
    
    dy = (y_obs(2:end, 1) - y_obs(1:(end - 1), 1));

    mu_hat    = mean(dy)/dt;
    sigma_hat = std(dy)/sqrt(dt);
end