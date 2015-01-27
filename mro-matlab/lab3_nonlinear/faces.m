function [ output_args ] = faces( no_dims, neighbors, kernel )

    path = 'mro/yaleBfaces/zad1/';
    filename = 'person01_01.png';
    
    files = dir(path);
    fileIndex = find(~[files.isdir]);
    faces = [];
    names = [];
    y = [];
    
    function [] = make_plot(results, dif, with_picture)
        scatter(results(1:end, 1), results(1:end, 2));
        if with_picture == 1
            hold on;
            for i = 1 : length(fileIndex)
                filename = strcat(path, files(fileIndex(i)).name);
                pic = imread(filename);
                posX = [(results(i, 1) - dif) (results(i, 1) + dif)];
                posY = [(results(i, 2) - dif) (results(i, 2) + dif)];
                image(posX, posY, pic);
            end
        end   
    end
    
    for i = 1 : length(fileIndex)
        filename = strcat(path, files(fileIndex(i)).name);
        
        face = imread(filename);
        face = double(face);
        vec = reshape(face, 1, 2500);
        
        faces = [ faces ; vec ];
        names = [ names ; files(fileIndex(i)).name ]; 
        y = [y ; ceil(i / 19) ];
    end
        
%     results_pca = pca(faces, no_dims);
%     results = results_pca;
    
%     results_lle = lle(faces, no_dims, neighbors);
%     results = results_lle;

    results_kpca = kernel_pca(faces, no_dims, kernel);
    results = results_kpca;
    
    train_set = [];
    test_set = [];
    y_train = [];
    for i = 1 : size(results, 1)
        if ( mod(i, 19) < 10 )
            train_set = [ train_set ; results(i, 1 : end) ];
            y_train = [y_train ; ceil(i / 19) ];
        else
            test_set = [ test_set ; results(i, 1 : end) ];
        end
    end
    
%     size(results)
%     size(y)
%     size(train_set)
%     size(test_set)
%     size(y_train)

    % NN
    mdl = fitcknn(train_set, y_train);
    labels = predict(mdl, test_set)
    
    % closest centroid
end

