% Copyright   : Michael Pokojovy & Valerii Maltsev (2020)
% Version     : 1.0
% Last edited : 04/19/2020
% License     : Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
%               https://creativecommons.org/licenses/by-sa/4.0/

function sigma = HJM_inv_map(T_grid, X_grid, Y_obs, pc_var)
    dx = X_grid(2) - X_grid(1);
    dt = T_grid(2) - T_grid(1);

    % Predictor vectors
    pred = zeros(length(T_grid) - 1, length(X_grid));
    
    for i = 2:length(T_grid)
        f1  = Y_obs(i,     :);
        f0  = Y_obs(i - 1, :);
        Af0 = [0 (f0(2:end) - f0(1:(end - 1)))/dx];
        Af1 = [0 (f1(2:end) - f1(1:(end - 1)))/dx];
        
        pred(i - 1, :) = (f1 - f0)/dt - Af0;
        
    end
    
    %% Estimate sigma
    % Transform to D(A)
    for i = 1:(length(T_grid) - 1)
        pred(i, :) = A(pred(i, :));
    end
    
    S = cov(pred);
    [V, D] = eig(S);
    
    V = V/sqrt(dx); % normalize the discrete L^2 norm
    d = diag(D)*dx; % scale the eigenvalues
    
    var_rat = cumsum(flip(d))./sum(d);
    n_mode  = min(find(var_rat >= pc_var));
    
    sigma = diag(sqrt(d((end - n_mode + 1):end)*dt))*V(:, (end - n_mode + 1):end)'; % Note the normalization factor dt
    
    % Transform back to H
    for i = 1:n_mode
        sigma(i, :) = I(sigma(i, :));
    end    
    
    function res = A(y)
        res = [0 (y(2:end) - y(1:(end - 1)))/dx];
    end

    function res = I(y)
        res = dx*cumsum(y);
    end
end