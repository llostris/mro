function [ ] = spiral(neighbors)

    % draw spiral
    t = [0:0.01:(20*pi)];
    x = ((exp(0.1*t)).*(cos(t)));
    y = ((exp(0.1*t)).*(sin(t)));
    spiral_matrix = [x ; y ]';
    plot(spiral_matrix(:, 1), spiral_matrix(:, 2));
    
    % use pca
    results_pca = pca(spiral_matrix, 1);
    figure(1);
    plot(results_pca);
    
    % use lle - data, num of dimensions, neighbors
    results_lle = lle(spiral_matrix, 1, neighbors);
    figure(2);
    plot(results_lle);

end

