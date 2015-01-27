function [] = hierarchical( metric, linkage, datafile )
% For testing various version of hierarchical clustering algorithms
% metric = { euclidean, correlations }
% linkage = { 'single', 'complete', 'average' }

    function G =  read_graph(fileName)
        inputfile = fopen(fileName);
        A = [];

        l = 0;
        k = 1;
        while 1
              % Get a line from the input file
              tline = fgetl(inputfile);

              % Quit if end of file
              if ~ischar(tline)
                  break
              end

              nums = regexp(tline,'\d+','match');
              if length(nums)
                  if l == 1
                      l = 0;
                      A(k,2) = str2num(nums{1});  
                      k = k + 1;
                      continue;
                  end
                  A(k,1) = str2num(nums{1});
                  l = 1;
              else
                  l = 0;
                  continue;
              end
        end
        G=[]; 
        for i=1:length(A) 
            G(A(i,1)+1,A(i,2)+1) = 1; 
        end
        
    end
    
    graph = read_graph(datafile);
%     graph = sparse(x(2:end,1)+1, x(2:end,2)+1, 1, x(1,1), x(1,2));
    result = clusterdata(graph, 'cutoff', 20, 'distance', metric, 'linkage', linkage);
%     dendrogram(result);
    
    
    M = pdist(graph, metric);
    M
    N = linkage(M);
    dendrogram(N);
end