function [ ] = coil(no_dims, kernel)
% Possible kernel functions are 'linear', 'gauss', 'poly', 'subsets', or 'princ_angles' (default = 'gauss')

    path = 'mro/nonlinear/coil/';    
    filenames = dir(path);
    fileIndex = find(~[filenames.isdir]);
    pictures = [];
       
    % create matrix

    for i = 1 : length(fileIndex)
        filename = strcat(path, filenames(fileIndex(i)).name);
        
        pic = imread(filename);
        pic = double(rgb2gray(pic));
        vec = reshape(pic, 1, 128 * 128);
        
        pictures = [ pictures ; vec ];        
    end
        
    % use lle - data, num of dimensions, neighbors
    results = kernel_pca(pictures, no_dims, kernel);
    if strcmp(kernel, 'gauss') == 1
        dif = 0.05;
    elseif strcmp(kernel, 'poly') == 1
        dif = 1000 * 1000 * 100000;
    end
    
    figure(1)
    scatter(results(1:end, 1), results(1:end, 2));
    
    figure(2)
    scatter(results(1:end, 1), results(1:end, 2));
    hold on;
    
    for i = 1 : length(fileIndex)
        filename = strcat(path, filenames(fileIndex(i)).name);
        pic = imread(filename);
        pic = imrotate(pic, 180);
        posX = [(results(i, 1) - dif) (results(i, 1) + dif)];
        posY = [(results(i, 2) - dif) (results(i, 2) + dif)];
        image(posX, posY, pic);
    end
end

