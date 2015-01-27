function [ ] = coil(dimensions, neighbors)

    path = 'mro/nonlinear/coil/';    
    filenames = dir(path);
    fileIndex = find(~[filenames.isdir]);
    pictures = [];
    
    function [] = make_plot(results, dif, with_picture)
        
        scatter(results(1:end, 1), results(1:end, 2));
        if with_picture == 1
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
    end
    
    % create matrix

    for i = 1 : length(fileIndex)
        filename = strcat(path, filenames(fileIndex(i)).name);
        
        pic = imread(filename);
        pic = double(rgb2gray(pic));
        vec = reshape(pic, 1, 128 * 128);
        
        pictures = [ pictures ; vec ];        
    end
    
    % pca
    results_pca = pca(pictures, dimensions);
    results = results_pca;
    dif = 300;
    figure(1); make_plot(results, dif, 0);
    figure(2); make_plot(results, dif, 1);
    
    % use lle - data, num of dimensions, neighbors
    results_lle = lle(pictures, dimensions, neighbors);
    results = results_lle;
    dif = 0.01;
    figure(3); make_plot(results, dif, 0);
    figure(4); make_plot(results, dif, 1);
    
    % use isomaps
    results = isomap(pictures, 2, neighbors);
    dif = 1200; % should be different depending on number of neighbors
    figure(5); make_plot(results, dif, 0);
    figure(6); make_plot(results, dif, 1);
    
end

