function [ ] = swiss(neighbors)

  data = generate_data('swiss');
%   scatter3(data(:, 1), data(:, 2), data(:, 3));
  
  x = isomap(data, 2, neighbors);
  size(x)
  scatter(x(:, 1), x(:, 2));
end
