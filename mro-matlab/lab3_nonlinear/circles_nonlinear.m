function [ output_args ] = circles_nonlinear(no_dims, kernel)
% Possible kernel functions are 'linear', 'gauss', 'poly', 'subsets', or 'princ_angles' (default = 'gauss')


    theta = 0:5:700;
    c = cosd(theta);
    s = sind(theta);
    r = 1:3;

    x1 = bsxfun(@times,r.',c);
    y1 = bsxfun(@times,r.',s);
    labels = [];
    for i = 1 : size(x1, 2)
       labels = [ labels ; 0 ] ;
    end
    for j = 1 : size(y1, 2)
       labels = [ labels ; 1 ] ;
    end
    data = [ x1' ; y1' ];
    

%     figure
%     plot(x1,y1,'o')
%     axis equal
    
    reds = labels == 0;
    blues = labels == 1;
    
    result = kernel_pca(data, no_dims, kernel);
%     scatter(result(1:end, 1), result(1:end, 2));
    figure
    plot(result(labels == 0, 1), result(labels == 0, 2), 'ro');
    hold on;
    plot(result(labels == 1, 1), result(labels == 1, 2), 'bo');
    axis equal;
end

