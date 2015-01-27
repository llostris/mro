function [ ] = kmeansfaces( n )
% n = liczba klastrow

    path = 'mro/yaleBfaces/zad1/';
    filename = 'person01_01.png';
    
    files = dir(path);
    fileIndex = find(~[files.isdir]);
    faces = [];
    names = [];
    
    for i = 1 : length(fileIndex)
        filename = strcat(path, files(fileIndex(i)).name);
        
        face = imread(filename);
        face = double(face);
        vec = reshape(face, 1, 2500);
        
        faces = [ faces ; vec ];        
        names = [ names ; files(fileIndex(i)).name ];
    end
    
    size(faces)
    res = kmeans(faces, n);
    for i = 1 : length(names) 
        fprintf('%s %d\n', names(i, :), res(i));
%         fprintf('%d\n', res(i));
    end

end

